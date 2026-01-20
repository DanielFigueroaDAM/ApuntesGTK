# Ejercicios de TreeView, Modelos y Tablas en GTK

## Descripción

Esta colección de ejercicios está diseñada para practicar el uso de **TreeView**, **TreeStore**, **ListStore** y sus diferentes componentes en GTK 3.0 con Python.

---

## Ejercicio 1: Lista de Productos (ListStore Básico)

**Dificultad:** ⭐ Fácil

**Objetivo:** Crear una tabla simple con una lista de productos.

**Requisitos:**
- Crear una ventana con un `ListStore` que tenga 3 columnas: Nombre (str), Precio (float), Stock (int)
- Mostrar al menos 5 productos
- Usar `CellRendererText` para todas las columnas
- La columna de precio debe mostrar el símbolo € al final

**Datos de ejemplo:**
```
Manzanas - 1.50€ - 100
Naranjas - 2.00€ - 75
Plátanos - 1.80€ - 50
Peras - 2.50€ - 30
Uvas - 3.00€ - 45
```

---

## Ejercicio 2: Sistema de Archivos (TreeStore Jerárquico)

**Dificultad:** ⭐⭐ Media

**Objetivo:** Simular una estructura de carpetas y archivos.

**Requisitos:**
- Usar `TreeStore` para crear una estructura jerárquica
- Columnas: Nombre (str), Tipo (str), Tamaño (str)
- Crear al menos 2 carpetas con subcarpetas y archivos dentro
- Los archivos deben tener tamaño, las carpetas mostrar "--"

**Estructura sugerida:**
```
Documentos/
├── Trabajo/
│   ├── informe.pdf (2.5 MB)
│   └── datos.xlsx (1.2 MB)
└── Personal/
    ├── fotos.zip (150 MB)
    └── notas.txt (4 KB)
Descargas/
├── programa.exe (45 MB)
└── musica.mp3 (8 MB)
```

---

## Ejercicio 3: Lista de Tareas con CheckBox (Toggle)

**Dificultad:** ⭐⭐ Media

**Objetivo:** Crear una lista de tareas donde se pueda marcar si están completadas.

**Requisitos:**
- Columnas: Completada (bool), Tarea (str), Prioridad (str)
- Usar `CellRendererToggle` para la columna "Completada"
- Implementar el método para cambiar el estado cuando se hace clic
- Usar `CellRendererCombo` para la prioridad (Alta, Media, Baja)

**Funcionalidad:**
- Al hacer clic en el checkbox, debe cambiar el estado de la tarea
- La prioridad debe ser editable mediante un ComboBox

---

## Ejercicio 4: Catálogo con Progreso (CellRendererProgress)

**Dificultad:** ⭐⭐ Media

**Objetivo:** Mostrar el progreso de descarga de varios archivos.

**Requisitos:**
- Columnas: Archivo (str), Progreso (int), Estado (str)
- Usar `CellRendererProgress` para mostrar el progreso visualmente
- El progreso debe ser un valor entre 0 y 100
- El estado puede ser: "Pendiente", "Descargando", "Completado"

**Datos de ejemplo:**
```
archivo1.zip - 75% - Descargando
archivo2.pdf - 100% - Completado
archivo3.mp4 - 30% - Descargando
archivo4.exe - 0% - Pendiente
```

---

## Ejercicio 5: Organigrama de Empresa (TreeStore Multinivel)

**Dificultad:** ⭐⭐⭐ Difícil

**Objetivo:** Representar la estructura jerárquica de una empresa.

**Requisitos:**
- Usar `TreeStore` con múltiples niveles de profundidad
- Columnas: Nombre (str), Cargo (str), Departamento (str), Salario (int)
- Mínimo 3 niveles: Director → Gerentes → Empleados
- Crear al menos 2 departamentos diferentes

**Estructura sugerida:**
```
Director General
├── Gerente de Ventas
│   ├── Vendedor 1
│   ├── Vendedor 2
│   └── Vendedor 3
├── Gerente de IT
│   ├── Programador 1
│   ├── Programador 2
│   └── Soporte Técnico
└── Gerente de RRHH
    ├── Analista RRHH
    └── Asistente RRHH
```

---

## Ejercicio 6: Tabla Editable Completa

**Dificultad:** ⭐⭐⭐ Difícil

**Objetivo:** Crear una tabla completamente editable de empleados.

**Requisitos:**
- Columnas: ID (str), Nombre (str), Edad (int), Departamento (str), Activo (bool)
- `CellRendererText` editable para ID, Nombre y Edad
- `CellRendererCombo` para Departamento
- `CellRendererToggle` para Activo
- Implementar todos los métodos de edición necesarios

**Funcionalidades:**
- Editar nombre haciendo doble clic
- Cambiar departamento con ComboBox (Ventas, IT, RRHH, Contabilidad)
- Toggle para cambiar estado activo/inactivo

---

## Ejercicio 7: Filtrado por Múltiples Criterios

**Dificultad:** ⭐⭐⭐⭐ Muy Difícil

**Objetivo:** Implementar un sistema de filtrado avanzado.

**Requisitos:**
- Crear una tabla de productos con: Nombre, Categoría, Precio, Disponible
- Implementar filtro por categoría usando RadioButtons
- Implementar filtro por rango de precio usando Scale
- Combinar ambos filtros simultáneamente

**Categorías:** Electrónica, Ropa, Hogar, Deportes

**Funcionalidades:**
- RadioButtons para filtrar por categoría
- Scale para filtrar por precio máximo
- Un botón "Mostrar todos" para quitar filtros

---

## Ejercicio 8: Árbol con Ordenación Personalizada

**Dificultad:** ⭐⭐⭐⭐ Muy Difícil

**Objetivo:** Implementar ordenación personalizada en un TreeView.

**Requisitos:**
- Crear una lista de estudiantes: Nombre, Nota (0-10), Grupo
- Implementar ordenación por nota usando `set_sort_func`
- La columna de nota debe ser clickeable para ordenar
- Ordenar ascendente y descendente

**Funcionalidades:**
- Click en cabecera de columna para ordenar
- Función de comparación personalizada para notas
- Indicador visual de ordenación (flecha arriba/abajo)

---

## Ejercicio 9: Árbol Genealógico Completo

**Dificultad:** ⭐⭐⭐⭐⭐ Experto

**Objetivo:** Crear un árbol genealógico interactivo.

**Requisitos:**
- Usar `TreeStore` con estructura: Nombre, Año Nacimiento, Año Fallecimiento, Relación
- Mínimo 4 generaciones de profundidad
- `CellRendererText` para datos personales
- `CellRendererToggle` para indicar si la persona sigue viva
- Implementar búsqueda por nombre

**Funcionalidades:**
- Expandir/colapsar ramas del árbol
- Mostrar años como "1950 - 2020" o "1990 - presente"
- Campo de entrada para buscar personas

---

## Ejercicio 10: Gestor de Inventario Completo

**Dificultad:** ⭐⭐⭐⭐⭐ Experto

**Objetivo:** Crear un sistema de gestión de inventario con todas las funcionalidades aprendidas.

**Requisitos:**
- Estructura jerárquica: Categoría → Subcategoría → Producto
- Columnas: Nombre, Código, Stock, Precio, Estado
- `CellRendererProgress` para mostrar nivel de stock (0-100%)
- `CellRendererCombo` para estado (Disponible, Agotado, Pedido)
- `CellRendererToggle` para marcar productos destacados
- Filtros por categoría y estado
- Ordenación por precio y stock
- Edición inline de todos los campos

**Funcionalidades adicionales:**
- Botones para añadir/eliminar productos
- Cálculo automático de valor total del inventario
- Alerta visual cuando stock < 10%

---

## Consejos Generales

1. **Siempre importar correctamente:**
   ```python
   import gi
   gi.require_version("Gtk", "3.0")
   from gi.repository import Gtk, Gdk, GObject
   ```

2. **Estructura básica de la clase:**
   ```python
   class MiVentana(Gtk.Window):
       def __init__(self):
           super().__init__()
           # Tu código aquí
           self.connect("delete_event", Gtk.main_quit)
           self.show_all()
   ```

3. **Patrón para CellRenderer editables:**
   ```python
   celda.set_property("editable", True)
   celda.connect("edited", self.on_celda_edited, modelo)
   ```

4. **Patrón para filtros:**
   ```python
   modeloFiltrado = modelo.filter_new()
   modeloFiltrado.set_visible_func(self.mi_filtro)
   ```

---

## Entrega

Para cada ejercicio, crear un archivo `.py` independiente siguiendo la nomenclatura:
- `Ejercicio01_ListaProductos.py`
- `Ejercicio02_SistemaArchivos.py`
- etc.

¡Buena suerte! 🚀
