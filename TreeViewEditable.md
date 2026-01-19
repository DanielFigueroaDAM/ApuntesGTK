# TreeViewEditable - Documentación del Código

## Descripción General

`TreeViewEditable.py` es un programa Python que utiliza GTK 3.0 para crear una interfaz gráfica con una tabla editable (TreeView) que permite visualizar y manipular datos de usuarios con diferentes características y filtros avanzados.

---

## Estructura General de la Clase

```python
class EjemploTree(Gtk.Window)
```

La clase principal hereda de `Gtk.Window` para crear la ventana principal de la aplicación.

---

## Métodos de la Clase

### 1. `on_celdaFalecido_toogled(self, celda, fila, modelo)`

**Propósito:** Maneja el evento de cambio en las celdas de tipo Toggle (casillas de verificación).

**Parámetros:**
- `celda`: El widget que generó el evento
- `fila`: El índice de la fila donde ocurrió el evento
- `modelo`: El modelo de datos (ListStore)

**Funcionalidad:** Invierte el valor booleano de la columna 4 (Falecido) cuando el usuario hace clic en la casilla.

```python
modelo[fila][4] = not modelo[fila][4]
```

---

### 2. `on_celdaNome_edited(self, celda, fila, cadroTexto, numero, modelo)`

**Propósito:** Maneja la edición de celdas de texto (nombre y DNI).

**Parámetros:**
- `celda`: El widget que generó el evento
- `fila`: El índice de la fila
- `cadroTexto`: El texto ingresado por el usuario
- `numero`: El índice de la columna
- `modelo`: El modelo de datos

**Funcionalidad:** Si el número de columna es 1 (Nombre), actualiza el valor en el modelo.

---

### 3. `on_xenero_changed(self, celda, fila, indx, modeloTab)`

**Propósito:** Maneja el cambio de selección en el ComboBox de género.

**Parámetros:**
- `celda`: El widget ComboBox
- `fila`: La fila donde se realizó el cambio
- `indx`: El índice de la opción seleccionada
- `modeloTab`: El modelo de datos

**Funcionalidad:** Actualiza la columna 3 (Xénero) con el valor seleccionado del modelo combo.

---

### 4. `filtro_usuarios_xenero(self, modelo, fila, datosUsuario)`

**Propósito:** Filtra los usuarios por género.

**Lógica:**
- Si no hay filtro de género (`None` o `"None"`), muestra todos los registros
- Si hay filtro, solo muestra filas que coincidan con el género filtrado

```python
return modelo[fila][3] == self.filtradoXenero
```

---

### 5. `on_xeneroToggled(self, boton, modelo)`

**Propósito:** Maneja los eventos de los botones radio de género.

**Funcionalidad:**
- Cuando se activa un botón radio, establece el filtro de género
- Llama a `modelo.refilter()` para aplicar el filtro

```python
self.filtradoXenero = boton.get_label()
modelo.refilter()
```

---

### 6. `on_rbtEdad_toggled(self, boton, scale, modelo)`

**Propósito:** Maneja los eventos de los botones radio "Mayor de" / "Menor de".

**Funcionalidad:**
- Establece el tipo de filtro de edad (Mayor o Menor)
- Captura el valor actual del slider
- Aplica el filtro

```python
self.filtradoEdad = scale.get_value()
self.filtradoEdadAux = boton.get_label()
modelo.refilter()
```

---

### 7. `on_scaleEdad_changed(self, scale, modelo)`

**Propósito:** Maneja los cambios en el slider de edad.

**Funcionalidad:**
- Captura el nuevo valor del slider
- Aplica inmediatamente el filtro al cambiar el valor

```python
self.filtradoEdad = scale.get_value()
modelo.refilter()
```

---

### 8. `filtro_usuarios_edade(self, modelo, fila, datosUsuario)`

**Propósito:** Filtra los usuarios por edad.

**Lógica:**
- Si no hay filtro activo, muestra todos
- Si el filtro es "Mayor de", muestra solo usuarios con edad mayor que el valor
- Si el filtro es "Menor de", muestra solo usuarios con edad menor que el valor

```python
if self.filtradoEdadAux == "Mayor de":
    return modelo[fila][2] > self.filtradoEdad
else:
    return modelo[fila][2] < self.filtradoEdad
```

---

### 9. `filtros_usuarios(self, modelo, fila, datosUsuario)`

**Propósito:** Combina todos los filtros (género Y edad).

**Funcionalidad:** Retorna `True` solo si la fila cumple con AMBOS filtros.

```python
edad = self.filtro_usuarios_edade(modelo, fila, datosUsuario)
xenero = self.filtro_usuarios_xenero(modelo, fila, datosUsuario)
return (edad and xenero)
```

---

### 10. `compara_edades(self, modelo, fila1, fila2, datosUsuarios)`

**Propósito:** Función de comparación personalizada para ordenar por edad.

**Funcionalidad:**
- Obtiene el valor de edad de dos filas
- Retorna 1 si edad1 > edad2
- Retorna -1 si edad1 < edad2
- Retorna 0 si son iguales

Esta función se utiliza con `modelo.set_sort_func()` para permitir ordenamiento personalizado.

---

### 11. `__init__(self)`

**Propósito:** Constructor que inicializa toda la interfaz gráfica.

#### Inicialización de Variables

```python
self.filtradoXenero = None
self.filtradoEdad = None
self.filtradoEdadAux = "Mayor de"
```

#### Creación del Modelo de Datos

```python
modelo = Gtk.ListStore(str, str, int, str, bool)
```

Crea un modelo con 5 columnas:
1. **str** - DNI
2. **str** - Nombre
3. **int** - Edad
4. **str** - Género
5. **bool** - Falecido

#### Datos de Ejemplo

Se insertan 5 usuarios de prueba en el modelo.

#### Configuración del Filtro

```python
modeloFiltrado = modelo.filter_new()
modeloFiltrado.set_visible_func(self.filtros_usuarios)
```

Se crea un modelo filtrado que utiliza la función `filtros_usuarios` para determinar qué filas mostrar.

#### Creación del TreeView

El TreeView se rellena con 5 columnas:

| Columna | Tipo | Descripción |
|---------|------|-------------|
| DNI | Texto editable | Identificador del usuario |
| Nombre | Texto editable | Nombre del usuario |
| Edad | Barra de progreso | Edad mostrada como barra (0-135) |
| Género | ComboBox | Dropdown con opciones (Home, Muller, Outros) |
| Falecido | Toggle | Casilla de verificación booleana |

#### Controles de Filtrado

**Filtro de Género:**
- 3 botones radio: Home, Muller, Outros
- Conectados a `on_xeneroToggled`

**Filtro de Edad:**
- Botones radio: "Mayor de" / "Menor de"
- Slider de 1 a 135 años
- El slider está conectado a `on_scaleEdad_changed`
- Los botones radio están conectados a `on_rbtEdad_toggled`

---

## Estructura de Datos del Usuario

Cada usuario en la lista tiene la siguiente estructura:

```python
(DNI, Nombre, Edad, Género, Falecido)
```

**Ejemplo:**
```python
('1234H', 'Ana Perez', 34, 'Muller', False)
```

---

## Flujo de Ejecución

1. Se crea la ventana con título "Ejemplo de Treeview en árbol"
2. Se construye el modelo con 5 usuarios
3. Se aplica un filtro visible basado en género y edad
4. Se crea el TreeView y se añaden 5 columnas con diferentes tipos de celdas
5. Se añaden controles interactivos (botones radio, slider)
6. Se conectan todos los eventos
7. Se muestra la interfaz completa
8. Se inicia el bucle principal de GTK

---

## Características Principales

✅ **Tabla editable** - Los usuarios pueden modificar DNI y Nombre directamente  
✅ **Filtrado múltiple** - Combina filtros de género y edad  
✅ **Ordenamiento personalizado** - Edad se ordena con función personalizada  
✅ **Controles interactivos** - Botones radio, slider y combo boxes  
✅ **Toggle de estado** - Casilla para marcar si el usuario ha fallecido  

---

## Requisitos

- Python 3.x
- GTK 3.0
- PyGObject

### Instalación

```bash
pip install PyGObject
```

En Ubuntu/Debian:
```bash
sudo apt-get install python3-gi gir1.2-gtk-3.0
```

---

## Ejecución

```bash
python TreeViewEditable.py
```

La ventana se cerrará cuando el usuario haga clic en el botón de cerrar.

---

## Notas Importantes

- Los filtros se aplican en **tiempo real** mientras se interactúa con los controles
- El modelo filtrado permite ver/ocultar filas sin eliminar datos
- La función `refilter()` recalcula qué filas son visibles
- El ordenamiento por edad es personalizado mediante una función comparadora
