# Soluciones de los Ejercicios de TreeView, Modelos y Tablas

## Solución Ejercicio 1: Lista de Productos (ListStore Básico)

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ListaProductos(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Lista de Productos")
        self.set_default_size(400, 300)

        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Crear el modelo: Nombre (str), Precio (float), Stock (int)
        modelo = Gtk.ListStore(str, float, int)

        # Datos de productos
        productos = [
            ("Manzanas", 1.50, 100),
            ("Naranjas", 2.00, 75),
            ("Plátanos", 1.80, 50),
            ("Peras", 2.50, 30),
            ("Uvas", 3.00, 45)
        ]

        for producto in productos:
            modelo.append(producto)

        # Crear TreeView
        trvVista = Gtk.TreeView(model=modelo)

        # Columna Nombre
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Nombre", celda, text=0)
        trvVista.append_column(columna)

        # Columna Precio (con formato €)
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Precio")
        columna.pack_start(celda, True)
        columna.set_cell_data_func(celda, self.formato_precio)
        trvVista.append_column(columna)

        # Columna Stock
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Stock", celda, text=2)
        trvVista.append_column(columna)

        caixav.pack_start(trvVista, True, True, 5)
        self.add(caixav)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()

    def formato_precio(self, columna, celda, modelo, fila, datos):
        precio = modelo.get_value(fila, 1)
        celda.set_property("text", f"{precio:.2f}€")


if __name__ == "__main__":
    ListaProductos()
    Gtk.main()
```

---

## Solución Ejercicio 2: Sistema de Archivos (TreeStore Jerárquico)

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SistemaArchivos(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Sistema de Archivos")
        self.set_default_size(500, 400)

        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Crear el modelo jerárquico: Nombre, Tipo, Tamaño
        modelo = Gtk.TreeStore(str, str, str)

        # Carpeta Documentos
        documentos = modelo.append(None, ["Documentos", "Carpeta", "--"])
        trabajo = modelo.append(documentos, ["Trabajo", "Carpeta", "--"])
        modelo.append(trabajo, ["informe.pdf", "PDF", "2.5 MB"])
        modelo.append(trabajo, ["datos.xlsx", "Excel", "1.2 MB"])

        personal = modelo.append(documentos, ["Personal", "Carpeta", "--"])
        modelo.append(personal, ["fotos.zip", "ZIP", "150 MB"])
        modelo.append(personal, ["notas.txt", "Texto", "4 KB"])

        # Carpeta Descargas
        descargas = modelo.append(None, ["Descargas", "Carpeta", "--"])
        modelo.append(descargas, ["programa.exe", "Ejecutable", "45 MB"])
        modelo.append(descargas, ["musica.mp3", "Audio", "8 MB"])

        # Crear TreeView
        trvVista = Gtk.TreeView(model=modelo)

        # Columnas
        for i, titulo in enumerate(["Nombre", "Tipo", "Tamaño"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(titulo, celda, text=i)
            trvVista.append_column(columna)

        # Expandir todas las filas
        trvVista.expand_all()

        caixav.pack_start(trvVista, True, True, 5)
        self.add(caixav)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    SistemaArchivos()
    Gtk.main()
```

---

## Solución Ejercicio 3: Lista de Tareas con CheckBox (Toggle)

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ListaTareas(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Lista de Tareas")
        self.set_default_size(500, 350)

        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Modelo: Completada (bool), Tarea (str), Prioridad (str)
        self.modelo = Gtk.ListStore(bool, str, str)

        tareas = [
            (False, "Comprar leche", "Alta"),
            (True, "Llamar al médico", "Media"),
            (False, "Estudiar Python", "Alta"),
            (False, "Limpiar casa", "Baja"),
            (True, "Pagar facturas", "Alta")
        ]

        for tarea in tareas:
            self.modelo.append(tarea)

        trvVista = Gtk.TreeView(model=self.modelo)

        # Columna Completada (Toggle)
        celda = Gtk.CellRendererToggle()
        celda.connect("toggled", self.on_completada_toggled)
        columna = Gtk.TreeViewColumn("✓", celda, active=0)
        trvVista.append_column(columna)

        # Columna Tarea
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Tarea", celda, text=1)
        trvVista.append_column(columna)

        # Columna Prioridad (ComboBox)
        modeloCombo = Gtk.ListStore(str)
        for prioridad in ["Alta", "Media", "Baja"]:
            modeloCombo.append([prioridad])

        celda = Gtk.CellRendererCombo()
        celda.set_property("editable", True)
        celda.set_property("model", modeloCombo)
        celda.set_property("text-column", 0)
        celda.set_property("has-entry", False)
        celda.connect("changed", self.on_prioridad_changed)
        columna = Gtk.TreeViewColumn("Prioridad", celda, text=2)
        trvVista.append_column(columna)

        caixav.pack_start(trvVista, True, True, 5)
        self.add(caixav)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()

    def on_completada_toggled(self, celda, fila):
        self.modelo[fila][0] = not self.modelo[fila][0]

    def on_prioridad_changed(self, celda, fila, indx):
        self.modelo[fila][2] = celda.props.model[indx][0]


if __name__ == "__main__":
    ListaTareas()
    Gtk.main()
```

---

## Solución Ejercicio 4: Catálogo con Progreso (CellRendererProgress)

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class CatalogoDescargas(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Gestor de Descargas")
        self.set_default_size(500, 300)

        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Modelo: Archivo (str), Progreso (int), Estado (str)
        modelo = Gtk.ListStore(str, int, str)

        descargas = [
            ("archivo1.zip", 75, "Descargando"),
            ("archivo2.pdf", 100, "Completado"),
            ("archivo3.mp4", 30, "Descargando"),
            ("archivo4.exe", 0, "Pendiente"),
            ("archivo5.iso", 50, "Descargando")
        ]

        for descarga in descargas:
            modelo.append(descarga)

        trvVista = Gtk.TreeView(model=modelo)

        # Columna Archivo
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Archivo", celda, text=0)
        trvVista.append_column(columna)

        # Columna Progreso (Progress)
        celda = Gtk.CellRendererProgress()
        columna = Gtk.TreeViewColumn("Progreso", celda, value=1)
        columna.set_min_width(150)
        trvVista.append_column(columna)

        # Columna Estado
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Estado", celda, text=2)
        trvVista.append_column(columna)

        caixav.pack_start(trvVista, True, True, 5)
        self.add(caixav)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    CatalogoDescargas()
    Gtk.main()
```

---

## Solución Ejercicio 5: Organigrama de Empresa (TreeStore Multinivel)

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class OrganigramaEmpresa(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Organigrama de Empresa")
        self.set_default_size(600, 450)

        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Modelo: Nombre, Cargo, Departamento, Salario
        modelo = Gtk.TreeStore(str, str, str, int)

        # Director General
        director = modelo.append(None, ["Carlos Méndez", "Director General", "Dirección", 80000])

        # Gerente de Ventas
        gerenteVentas = modelo.append(director, ["Ana García", "Gerente", "Ventas", 50000])
        modelo.append(gerenteVentas, ["Pedro López", "Vendedor", "Ventas", 25000])
        modelo.append(gerenteVentas, ["María Ruiz", "Vendedor", "Ventas", 25000])
        modelo.append(gerenteVentas, ["Juan Torres", "Vendedor", "Ventas", 24000])

        # Gerente de IT
        gerenteIT = modelo.append(director, ["Luis Fernández", "Gerente", "IT", 55000])
        modelo.append(gerenteIT, ["Sara Díaz", "Programador", "IT", 35000])
        modelo.append(gerenteIT, ["Miguel Sanz", "Programador", "IT", 35000])
        modelo.append(gerenteIT, ["Laura Vega", "Soporte Técnico", "IT", 28000])

        # Gerente de RRHH
        gerenteRRHH = modelo.append(director, ["Carmen Ortiz", "Gerente", "RRHH", 48000])
        modelo.append(gerenteRRHH, ["Pablo Núñez", "Analista RRHH", "RRHH", 30000])
        modelo.append(gerenteRRHH, ["Elena Castro", "Asistente RRHH", "RRHH", 22000])

        trvVista = Gtk.TreeView(model=modelo)

        # Columnas
        titulos = ["Nombre", "Cargo", "Departamento", "Salario"]
        for i, titulo in enumerate(titulos):
            celda = Gtk.CellRendererText()
            if i == 3:  # Salario con formato
                columna = Gtk.TreeViewColumn(titulo)
                columna.pack_start(celda, True)
                columna.set_cell_data_func(celda, self.formato_salario)
            else:
                columna = Gtk.TreeViewColumn(titulo, celda, text=i)
            trvVista.append_column(columna)

        trvVista.expand_all()

        caixav.pack_start(trvVista, True, True, 5)
        self.add(caixav)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()

    def formato_salario(self, columna, celda, modelo, fila, datos):
        salario = modelo.get_value(fila, 3)
        celda.set_property("text", f"{salario:,}€")


if __name__ == "__main__":
    OrganigramaEmpresa()
    Gtk.main()
```

---

## Solución Ejercicio 6: Tabla Editable Completa

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class TablaEditableEmpleados(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Gestión de Empleados")
        self.set_default_size(650, 400)

        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Modelo: ID, Nombre, Edad, Departamento, Activo
        self.modelo = Gtk.ListStore(str, str, int, str, bool)

        empleados = [
            ("E001", "Ana Pérez", 34, "Ventas", True),
            ("E002", "Luis García", 28, "IT", True),
            ("E003", "María López", 45, "RRHH", False),
            ("E004", "Carlos Ruiz", 52, "Contabilidad", True),
            ("E005", "Laura Díaz", 31, "IT", True)
        ]

        for emp in empleados:
            self.modelo.append(emp)

        trvVista = Gtk.TreeView(model=self.modelo)

        # Columna ID (editable)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        celda.connect("edited", self.on_texto_edited, 0)
        columna = Gtk.TreeViewColumn("ID", celda, text=0)
        trvVista.append_column(columna)

        # Columna Nombre (editable)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        celda.connect("edited", self.on_texto_edited, 1)
        columna = Gtk.TreeViewColumn("Nombre", celda, text=1)
        trvVista.append_column(columna)

        # Columna Edad (editable)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        celda.connect("edited", self.on_edad_edited)
        columna = Gtk.TreeViewColumn("Edad", celda, text=2)
        trvVista.append_column(columna)

        # Columna Departamento (ComboBox)
        modeloCombo = Gtk.ListStore(str)
        for dept in ["Ventas", "IT", "RRHH", "Contabilidad"]:
            modeloCombo.append([dept])

        celda = Gtk.CellRendererCombo()
        celda.set_property("editable", True)
        celda.set_property("model", modeloCombo)
        celda.set_property("text-column", 0)
        celda.set_property("has-entry", False)
        celda.connect("changed", self.on_departamento_changed)
        columna = Gtk.TreeViewColumn("Departamento", celda, text=3)
        trvVista.append_column(columna)

        # Columna Activo (Toggle)
        celda = Gtk.CellRendererToggle()
        celda.connect("toggled", self.on_activo_toggled)
        columna = Gtk.TreeViewColumn("Activo", celda, active=4)
        trvVista.append_column(columna)

        caixav.pack_start(trvVista, True, True, 5)
        self.add(caixav)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()

    def on_texto_edited(self, celda, fila, texto, columna):
        self.modelo[fila][columna] = texto

    def on_edad_edited(self, celda, fila, texto):
        try:
            self.modelo[fila][2] = int(texto)
        except ValueError:
            print("Error: Ingrese un número válido para la edad")

    def on_departamento_changed(self, celda, fila, indx):
        self.modelo[fila][3] = celda.props.model[indx][0]

    def on_activo_toggled(self, celda, fila):
        self.modelo[fila][4] = not self.modelo[fila][4]


if __name__ == "__main__":
    TablaEditableEmpleados()
    Gtk.main()
```

---

## Solución Ejercicio 7: Filtrado por Múltiples Criterios

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class FiltradoProductos(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Filtrado de Productos")
        self.set_default_size(600, 450)

        self.filtroCategoria = None
        self.filtroPrecioMax = 1000

        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Modelo: Nombre, Categoría, Precio, Disponible
        self.modelo = Gtk.ListStore(str, str, float, bool)

        productos = [
            ("Laptop HP", "Electrónica", 899.99, True),
            ("Camiseta Nike", "Ropa", 35.00, True),
            ("Sofá 3 plazas", "Hogar", 450.00, False),
            ("Balón fútbol", "Deportes", 25.00, True),
            ("Smartphone Samsung", "Electrónica", 599.00, True),
            ("Pantalón Levi's", "Ropa", 65.00, True),
            ("Mesa comedor", "Hogar", 280.00, True),
            ("Raqueta tenis", "Deportes", 120.00, False),
            ("Auriculares Sony", "Electrónica", 150.00, True),
            ("Zapatillas Adidas", "Deportes", 89.00, True)
        ]

        for prod in productos:
            self.modelo.append(prod)

        # Modelo filtrado
        self.modeloFiltrado = self.modelo.filter_new()
        self.modeloFiltrado.set_visible_func(self.filtrar_productos)

        trvVista = Gtk.TreeView(model=self.modeloFiltrado)

        # Columnas
        for i, titulo in enumerate(["Nombre", "Categoría", "Precio", "Disponible"]):
            if i == 2:
                celda = Gtk.CellRendererText()
                columna = Gtk.TreeViewColumn(titulo)
                columna.pack_start(celda, True)
                columna.set_cell_data_func(celda, self.formato_precio)
            elif i == 3:
                celda = Gtk.CellRendererToggle()
                columna = Gtk.TreeViewColumn(titulo, celda, active=i)
            else:
                celda = Gtk.CellRendererText()
                columna = Gtk.TreeViewColumn(titulo, celda, text=i)
            trvVista.append_column(columna)

        caixav.pack_start(trvVista, True, True, 5)

        # RadioButtons para categoría
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        lbl = Gtk.Label(label="Categoría: ")
        caixaH.pack_start(lbl, False, False, 5)

        rbtTodos = Gtk.RadioButton(label="Todos")
        rbtTodos.connect("toggled", self.on_categoria_toggled)
        caixaH.pack_start(rbtTodos, False, False, 2)

        for cat in ["Electrónica", "Ropa", "Hogar", "Deportes"]:
            rbt = Gtk.RadioButton.new_with_label_from_widget(rbtTodos, label=cat)
            rbt.connect("toggled", self.on_categoria_toggled)
            caixaH.pack_start(rbt, False, False, 2)

        caixav.pack_start(caixaH, False, False, 5)

        # Scale para precio máximo
        caixaH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        lbl = Gtk.Label(label="Precio máximo: ")
        caixaH2.pack_start(lbl, False, False, 5)

        scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 1000, 10)
        scale.set_value(1000)
        scale.connect("value-changed", self.on_precio_changed)
        caixaH2.pack_start(scale, True, True, 5)

        caixav.pack_start(caixaH2, False, False, 5)

        self.add(caixav)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()

    def formato_precio(self, columna, celda, modelo, fila, datos):
        precio = modelo.get_value(fila, 2)
        celda.set_property("text", f"{precio:.2f}€")

    def filtrar_productos(self, modelo, fila, datos):
        filtroCategoria = True
        filtroPrecio = True

        if self.filtroCategoria and self.filtroCategoria != "Todos":
            filtroCategoria = modelo[fila][1] == self.filtroCategoria

        filtroPrecio = modelo[fila][2] <= self.filtroPrecioMax

        return filtroCategoria and filtroPrecio

    def on_categoria_toggled(self, boton):
        if boton.get_active():
            self.filtroCategoria = boton.get_label()
            self.modeloFiltrado.refilter()

    def on_precio_changed(self, scale):
        self.filtroPrecioMax = scale.get_value()
        self.modeloFiltrado.refilter()


if __name__ == "__main__":
    FiltradoProductos()
    Gtk.main()
```

---

## Solución Ejercicio 8: Árbol con Ordenación Personalizada

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ListaEstudiantes(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Lista de Estudiantes")
        self.set_default_size(500, 400)

        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Modelo: Nombre, Nota, Grupo
        self.modelo = Gtk.ListStore(str, float, str)

        estudiantes = [
            ("Ana García", 8.5, "A"),
            ("Luis Pérez", 6.0, "B"),
            ("María López", 9.2, "A"),
            ("Carlos Ruiz", 5.5, "B"),
            ("Laura Díaz", 7.8, "A"),
            ("Pedro Sanz", 4.2, "B"),
            ("Sara Torres", 10.0, "A"),
            ("Miguel Vega", 6.8, "B")
        ]

        for est in estudiantes:
            self.modelo.append(est)

        # Configurar función de ordenación personalizada para columna 1 (Nota)
        self.modelo.set_sort_func(1, self.comparar_notas, None)

        trvVista = Gtk.TreeView(model=self.modelo)

        # Columna Nombre
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Nombre", celda, text=0)
        columna.set_sort_column_id(0)
        trvVista.append_column(columna)

        # Columna Nota (ordenable con función personalizada)
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Nota", celda, text=1)
        columna.set_sort_column_id(1)
        trvVista.append_column(columna)

        # Columna Grupo
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Grupo", celda, text=2)
        columna.set_sort_column_id(2)
        trvVista.append_column(columna)

        caixav.pack_start(trvVista, True, True, 5)

        # Label informativo
        lbl = Gtk.Label(label="Haz clic en las cabeceras de columna para ordenar")
        caixav.pack_start(lbl, False, False, 5)

        self.add(caixav)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()

    def comparar_notas(self, modelo, fila1, fila2, datos):
        columna_ordenar, _ = modelo.get_sort_column_id()
        nota1 = modelo.get_value(fila1, 1)
        nota2 = modelo.get_value(fila2, 1)

        if nota1 > nota2:
            return 1
        elif nota1 < nota2:
            return -1
        else:
            return 0


if __name__ == "__main__":
    ListaEstudiantes()
    Gtk.main()
```

---

## Solución Ejercicio 9: Árbol Genealógico Completo

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ArbolGenealogico(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Árbol Genealógico")
        self.set_default_size(700, 500)

        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Modelo: Nombre, Año Nacimiento, Año Fallecimiento, Relación, Vivo
        self.modelo = Gtk.TreeStore(str, int, int, str, bool)

        # Bisabuelo (Generación 1)
        bisabuelo = self.modelo.append(None, ["Manuel García", 1900, 1985, "Bisabuelo", False])

        # Abuelos (Generación 2)
        abuelo1 = self.modelo.append(bisabuelo, ["Antonio García", 1930, 2010, "Abuelo", False])
        abuelo2 = self.modelo.append(bisabuelo, ["José García", 1935, 0, "Abuelo", True])

        # Padres (Generación 3)
        padre1 = self.modelo.append(abuelo1, ["Carlos García", 1960, 0, "Padre", True])
        padre2 = self.modelo.append(abuelo1, ["María García", 1965, 0, "Tía", True])
        padre3 = self.modelo.append(abuelo2, ["Luis García", 1962, 2020, "Tío", False])

        # Hijos (Generación 4)
        self.modelo.append(padre1, ["Ana García", 1990, 0, "Yo", True])
        self.modelo.append(padre1, ["Pedro García", 1993, 0, "Hermano", True])
        self.modelo.append(padre2, ["Laura García", 1992, 0, "Prima", True])
        self.modelo.append(padre3, ["Miguel García", 1988, 0, "Primo", True])
        self.modelo.append(padre3, ["Sara García", 1995, 0, "Prima", True])

        # Modelo filtrado para búsqueda
        self.modeloFiltrado = self.modelo.filter_new()
        self.textoBusqueda = ""
        self.modeloFiltrado.set_visible_func(self.filtrar_busqueda)

        trvVista = Gtk.TreeView(model=self.modeloFiltrado)

        # Columna Nombre
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Nombre", celda, text=0)
        trvVista.append_column(columna)

        # Columna Años (formato especial)
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Años")
        columna.pack_start(celda, True)
        columna.set_cell_data_func(celda, self.formato_anos)
        trvVista.append_column(columna)

        # Columna Relación
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Relación", celda, text=3)
        trvVista.append_column(columna)

        # Columna Vivo (Toggle)
        celda = Gtk.CellRendererToggle()
        columna = Gtk.TreeViewColumn("Vivo", celda, active=4)
        trvVista.append_column(columna)

        trvVista.expand_all()

        caixav.pack_start(trvVista, True, True, 5)

        # Campo de búsqueda
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        lbl = Gtk.Label(label="Buscar: ")
        caixaH.pack_start(lbl, False, False, 5)

        entrada = Gtk.Entry()
        entrada.connect("changed", self.on_busqueda_changed)
        caixaH.pack_start(entrada, True, True, 5)

        caixav.pack_start(caixaH, False, False, 5)

        self.add(caixav)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()

    def formato_anos(self, columna, celda, modelo, fila, datos):
        nacimiento = modelo.get_value(fila, 1)
        fallecimiento = modelo.get_value(fila, 2)
        vivo = modelo.get_value(fila, 4)

        if vivo or fallecimiento == 0:
            texto = f"{nacimiento} - presente"
        else:
            texto = f"{nacimiento} - {fallecimiento}"
        celda.set_property("text", texto)

    def filtrar_busqueda(self, modelo, fila, datos):
        if not self.textoBusqueda:
            return True
        nombre = modelo[fila][0].lower()
        return self.textoBusqueda.lower() in nombre

    def on_busqueda_changed(self, entrada):
        self.textoBusqueda = entrada.get_text()
        self.modeloFiltrado.refilter()


if __name__ == "__main__":
    ArbolGenealogico()
    Gtk.main()
```

---

## Solución Ejercicio 10: Gestor de Inventario Completo

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GestorInventario(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Gestor de Inventario")
        self.set_default_size(900, 600)

        self.filtroCategoria = None
        self.filtroEstado = None

        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Modelo: Nombre, Código, Stock(%), Precio, Estado, Destacado
        self.modelo = Gtk.TreeStore(str, str, int, float, str, bool)

        # Categoría Electrónica
        electronica = self.modelo.append(None, ["Electrónica", "--", 0, 0.0, "--", False])
        moviles = self.modelo.append(electronica, ["Móviles", "--", 0, 0.0, "--", False])
        self.modelo.append(moviles, ["iPhone 14", "EL001", 75, 999.99, "Disponible", True])
        self.modelo.append(moviles, ["Samsung S23", "EL002", 45, 899.99, "Disponible", False])
        self.modelo.append(moviles, ["Xiaomi 13", "EL003", 5, 599.99, "Agotado", False])

        ordenadores = self.modelo.append(electronica, ["Ordenadores", "--", 0, 0.0, "--", False])
        self.modelo.append(ordenadores, ["MacBook Pro", "EL004", 30, 1999.99, "Disponible", True])
        self.modelo.append(ordenadores, ["Dell XPS", "EL005", 0, 1499.99, "Pedido", False])

        # Categoría Hogar
        hogar = self.modelo.append(None, ["Hogar", "--", 0, 0.0, "--", False])
        muebles = self.modelo.append(hogar, ["Muebles", "--", 0, 0.0, "--", False])
        self.modelo.append(muebles, ["Sofá 3 plazas", "HO001", 60, 450.00, "Disponible", False])
        self.modelo.append(muebles, ["Mesa comedor", "HO002", 8, 280.00, "Disponible", False])

        # Modelo filtrado
        self.modeloFiltrado = self.modelo.filter_new()
        self.modeloFiltrado.set_visible_func(self.filtrar_inventario)

        # Modelo ordenable
        self.modeloOrdenable = Gtk.TreeModelSort(model=self.modeloFiltrado)
        self.modeloOrdenable.set_sort_func(3, self.comparar_precios, None)

        trvVista = Gtk.TreeView(model=self.modeloOrdenable)

        # Columna Nombre (editable)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        celda.connect("edited", self.on_nombre_edited)
        columna = Gtk.TreeViewColumn("Nombre", celda, text=0)
        trvVista.append_column(columna)

        # Columna Código (editable)
        celda = Gtk.CellRendererText()
        celda.set_property("editable", True)
        celda.connect("edited", self.on_codigo_edited)
        columna = Gtk.TreeViewColumn("Código", celda, text=1)
        trvVista.append_column(columna)

        # Columna Stock (Progress)
        celda = Gtk.CellRendererProgress()
        columna = Gtk.TreeViewColumn("Stock", celda, value=2)
        columna.set_sort_column_id(2)
        columna.set_min_width(100)
        trvVista.append_column(columna)

        # Columna Precio (ordenable)
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Precio")
        columna.pack_start(celda, True)
        columna.set_cell_data_func(celda, self.formato_precio)
        columna.set_sort_column_id(3)
        trvVista.append_column(columna)

        # Columna Estado (ComboBox)
        modeloComboEstado = Gtk.ListStore(str)
        for estado in ["Disponible", "Agotado", "Pedido", "--"]:
            modeloComboEstado.append([estado])

        celda = Gtk.CellRendererCombo()
        celda.set_property("editable", True)
        celda.set_property("model", modeloComboEstado)
        celda.set_property("text-column", 0)
        celda.set_property("has-entry", False)
        celda.connect("changed", self.on_estado_changed)
        columna = Gtk.TreeViewColumn("Estado", celda, text=4)
        trvVista.append_column(columna)

        # Columna Destacado (Toggle)
        celda = Gtk.CellRendererToggle()
        celda.connect("toggled", self.on_destacado_toggled)
        columna = Gtk.TreeViewColumn("★", celda, active=5)
        trvVista.append_column(columna)

        trvVista.expand_all()
        self.trvVista = trvVista

        scrolled = Gtk.ScrolledWindow()
        scrolled.add(trvVista)
        caixav.pack_start(scrolled, True, True, 5)

        # Filtros
        caixaFiltros = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        # Filtro por categoría
        lbl = Gtk.Label(label="Categoría: ")
        caixaFiltros.pack_start(lbl, False, False, 5)

        rbtTodos = Gtk.RadioButton(label="Todos")
        rbtTodos.connect("toggled", self.on_filtro_categoria)
        caixaFiltros.pack_start(rbtTodos, False, False, 2)

        for cat in ["Electrónica", "Hogar"]:
            rbt = Gtk.RadioButton.new_with_label_from_widget(rbtTodos, label=cat)
            rbt.connect("toggled", self.on_filtro_categoria)
            caixaFiltros.pack_start(rbt, False, False, 2)

        # Separador
        sep = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        caixaFiltros.pack_start(sep, False, False, 10)

        # Filtro por estado
        lbl = Gtk.Label(label="Estado: ")
        caixaFiltros.pack_start(lbl, False, False, 5)

        rbtEstTodos = Gtk.RadioButton(label="Todos")
        rbtEstTodos.connect("toggled", self.on_filtro_estado)
        caixaFiltros.pack_start(rbtEstTodos, False, False, 2)

        for est in ["Disponible", "Agotado", "Pedido"]:
            rbt = Gtk.RadioButton.new_with_label_from_widget(rbtEstTodos, label=est)
            rbt.connect("toggled", self.on_filtro_estado)
            caixaFiltros.pack_start(rbt, False, False, 2)

        caixav.pack_start(caixaFiltros, False, False, 5)

        # Label con valor total
        self.lblTotal = Gtk.Label()
        self.actualizar_total()
        caixav.pack_start(self.lblTotal, False, False, 5)

        self.add(caixav)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()

    def formato_precio(self, columna, celda, modelo, fila, datos):
        precio = modelo.get_value(fila, 3)
        if precio > 0:
            celda.set_property("text", f"{precio:.2f}€")
        else:
            celda.set_property("text", "--")

    def comparar_precios(self, modelo, fila1, fila2, datos):
        precio1 = modelo.get_value(fila1, 3)
        precio2 = modelo.get_value(fila2, 3)

        if precio1 > precio2:
            return 1
        elif precio1 < precio2:
            return -1
        return 0

    def filtrar_inventario(self, modelo, fila, datos):
        # Solo filtrar productos (tienen código diferente de "--")
        codigo = modelo[fila][1]
        if codigo == "--":
            return True

        filtroCategoria = True
        filtroEstado = True

        if self.filtroEstado and self.filtroEstado != "Todos":
            filtroEstado = modelo[fila][4] == self.filtroEstado

        return filtroCategoria and filtroEstado

    def on_filtro_categoria(self, boton):
        if boton.get_active():
            label = boton.get_label()
            self.filtroCategoria = None if label == "Todos" else label
            self.modeloFiltrado.refilter()

    def on_filtro_estado(self, boton):
        if boton.get_active():
            label = boton.get_label()
            self.filtroEstado = None if label == "Todos" else label
            self.modeloFiltrado.refilter()

    def on_nombre_edited(self, celda, path, texto):
        # Convertir path del modelo ordenable al modelo original
        iter_sort = self.modeloOrdenable.get_iter_from_string(path)
        iter_filter = self.modeloOrdenable.convert_iter_to_child_iter(iter_sort)
        iter_modelo = self.modeloFiltrado.convert_iter_to_child_iter(iter_filter)
        self.modelo.set_value(iter_modelo, 0, texto)

    def on_codigo_edited(self, celda, path, texto):
        iter_sort = self.modeloOrdenable.get_iter_from_string(path)
        iter_filter = self.modeloOrdenable.convert_iter_to_child_iter(iter_sort)
        iter_modelo = self.modeloFiltrado.convert_iter_to_child_iter(iter_filter)
        self.modelo.set_value(iter_modelo, 1, texto)

    def on_estado_changed(self, celda, path, indx):
        iter_sort = self.modeloOrdenable.get_iter_from_string(path)
        iter_filter = self.modeloOrdenable.convert_iter_to_child_iter(iter_sort)
        iter_modelo = self.modeloFiltrado.convert_iter_to_child_iter(iter_filter)
        self.modelo.set_value(iter_modelo, 4, celda.props.model[indx][0])

    def on_destacado_toggled(self, celda, path):
        iter_sort = self.modeloOrdenable.get_iter_from_string(path)
        iter_filter = self.modeloOrdenable.convert_iter_to_child_iter(iter_sort)
        iter_modelo = self.modeloFiltrado.convert_iter_to_child_iter(iter_filter)
        valor_actual = self.modelo.get_value(iter_modelo, 5)
        self.modelo.set_value(iter_modelo, 5, not valor_actual)

    def actualizar_total(self):
        total = 0.0
        def iterar(modelo, path, iter, datos):
            nonlocal total
            precio = modelo.get_value(iter, 3)
            stock = modelo.get_value(iter, 2)
            if precio > 0 and stock > 0:
                total += precio * (stock / 10)  # Estimación simple
        self.modelo.foreach(iterar, None)
        self.lblTotal.set_text(f"Valor estimado del inventario: {total:,.2f}€")


if __name__ == "__main__":
    GestorInventario()
    Gtk.main()
```

---

## Notas Finales

Estos ejercicios cubren progresivamente todos los conceptos de TreeView en GTK:

1. **Básico**: ListStore, CellRendererText
2. **Intermedio**: TreeStore, Toggle, Combo, Progress
3. **Avanzado**: Filtros, Ordenación, Edición completa
4. **Experto**: Combinación de todas las técnicas

¡Practica cada ejercicio y modifícalo para explorar más funcionalidades! 🎓
