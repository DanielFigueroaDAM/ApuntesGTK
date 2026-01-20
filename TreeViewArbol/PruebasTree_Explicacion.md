# PruebasTree - Documentación del Código

## Descripción General

`PruebasTree.py` es un programa Python que utiliza GTK 3.0 para crear una interfaz gráfica con un **TreeView jerárquico** (en forma de árbol) que permite visualizar datos estructurados en niveles padre-hijo, simulando una estructura familiar de avós (abuelos), pais (padres) y fillos (hijos).

---

## Estructura General de la Clase

```python
class EjemploTree(Gtk.Window)
```

La clase principal hereda de `Gtk.Window` para crear la ventana principal de la aplicación.

---

## Diferencia entre TreeStore y ListStore

| Característica | ListStore | TreeStore |
|----------------|-----------|-----------|
| **Estructura** | Lista plana (tabla) | Árbol jerárquico |
| **Niveles** | Un único nivel | Múltiples niveles anidados |
| **Uso típico** | Tablas simples | Datos con relaciones padre-hijo |
| **Ejemplo** | Lista de usuarios | Árbol genealógico, sistema de archivos |

---

## Importaciones

```python
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject
```

- **gi**: PyGObject, permite usar bibliotecas GNOME desde Python
- **Gtk**: Biblioteca para interfaces gráficas
- **Gdk**: Funciones de bajo nivel para gráficos
- **GObject**: Sistema de objetos base de GTK

---

## Análisis del Constructor `__init__`

### 1. Configuración Inicial de la Ventana

```python
super().__init__()
self.set_title("Ejemplo de Treeview en árbol")
```

- Llama al constructor padre `Gtk.Window`
- Establece el título de la ventana

---

### 2. Contenedor Principal

```python
caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
```

Crea un contenedor vertical (`Gtk.Box`) con:
- **orientation**: Orientación vertical (elementos apilados)
- **spacing**: 6 píxeles de separación entre elementos

---

### 3. Creación del Modelo de Datos (TreeStore)

```python
modelo = Gtk.TreeStore(str, int)
```

**Gtk.TreeStore** es el modelo de datos para árboles jerárquicos:
- **Primer parámetro (`str`)**: Columna 0 - Texto del parentesco
- **Segundo parámetro (`int`)**: Columna 1 - Número de orden

**Diferencia clave con ListStore:**
- `ListStore` → Datos planos (filas simples)
- `TreeStore` → Datos jerárquicos (filas con hijos)

---

### 4. Población del Modelo con Datos Jerárquicos

```python
for avo in range(5):
    punteiroAvo = modelo.append(None, ["Avo %i" % (avo,), avo])
    for pai in range(4):
        punteiroPai = modelo.append(punteiroAvo, ["Pai %i do avó %i" % (pai, avo), pai])
        for fillo in range(3):
            modelo.append(punteiroPai, ["Fillo %i, do pai %i, do avó %i" % (fillo, pai, avo), fillo])
```

#### Estructura del Bucle

**Nivel 1 - Avós (Abuelos):**
```python
punteiroAvo = modelo.append(None, ["Avo %i" % (avo,), avo])
```
- `None` como primer parámetro indica que es un nodo raíz (sin padre)
- Retorna un **puntero/iterador** que identifica esta fila

**Nivel 2 - Pais (Padres):**
```python
punteiroPai = modelo.append(punteiroAvo, ["Pai %i do avó %i" % (pai, avo), pai])
```
- `punteiroAvo` como primer parámetro indica que este nodo es hijo del abuelo
- También retorna un puntero para usarlo como padre

**Nivel 3 - Fillos (Hijos):**
```python
modelo.append(punteiroPai, ["Fillo %i, do pai %i, do avó %i" % (fillo, pai, avo), fillo])
```
- `punteiroPai` como primer parámetro indica que este nodo es hijo del padre

#### Resultado de la Estructura

```
├── Avo 0
│   ├── Pai 0 do avó 0
│   │   ├── Fillo 0, do pai 0, do avó 0
│   │   ├── Fillo 1, do pai 0, do avó 0
│   │   └── Fillo 2, do pai 0, do avó 0
│   ├── Pai 1 do avó 0
│   │   ├── Fillo 0, do pai 1, do avó 0
│   │   └── ...
│   └── ...
├── Avo 1
│   └── ...
└── ...
```

**Total de nodos:** 5 avós × 4 pais × 3 fillos = 60 fillos + 20 pais + 5 avós = **85 nodos**

---

### 5. Creación del TreeView

```python
trvVista = Gtk.TreeView(model=modelo)
```

Crea el widget visual que mostrará los datos del modelo.

---

### 6. Primera Columna - "Parentesco"

```python
tvcColumna = Gtk.TreeViewColumn("Parentesco")
trvVista.append_column(tvcColumna)
celda = Gtk.CellRendererText()
tvcColumna.pack_start(celda, True)
tvcColumna.add_attribute(celda, 'text', 0)
```

| Componente | Descripción |
|------------|-------------|
| `TreeViewColumn` | Define una columna visual en el TreeView |
| `append_column()` | Añade la columna al TreeView |
| `CellRendererText` | Renderiza el contenido como texto |
| `pack_start()` | Añade el renderizador a la columna |
| `add_attribute()` | Conecta el atributo 'text' con la columna 0 del modelo |

---

### 7. Segunda Columna - "Orde"

```python
tvcColumna2 = Gtk.TreeViewColumn("Orde")
trvVista.append_column(tvcColumna2)
celda = Gtk.CellRendererText()
tvcColumna.pack_start(celda, True)  # ⚠️ NOTA: Debería ser tvcColumna2
tvcColumna.add_attribute(celda, 'text', 1)  # ⚠️ NOTA: Debería ser tvcColumna2
```

> **⚠️ Bug detectado:** Las líneas usan `tvcColumna` en lugar de `tvcColumna2`, por lo que la segunda columna no mostrará datos correctamente.

**Código corregido:**
```python
tvcColumna2 = Gtk.TreeViewColumn("Orde")
trvVista.append_column(tvcColumna2)
celda = Gtk.CellRendererText()
tvcColumna2.pack_start(celda, True)
tvcColumna2.add_attribute(celda, 'text', 1)
```

---

### 8. Empaquetado y Visualización

```python
caixav.pack_start(trvVista, True, True, 5)
self.add(caixav)
self.connect("delete_event", Gtk.main_quit)
self.show_all()
```

| Método | Descripción |
|--------|-------------|
| `pack_start()` | Añade el TreeView al contenedor vertical |
| `add()` | Añade el contenedor a la ventana |
| `connect("delete_event", ...)` | Cierra la aplicación al cerrar la ventana |
| `show_all()` | Muestra todos los widgets |

---

## Punto de Entrada

```python
if __name__ == "__main__":
    EjemploTree()
    Gtk.main()
```

- Crea una instancia de la ventana
- `Gtk.main()` inicia el bucle de eventos de GTK

---

## Métodos Importantes de TreeStore

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `append(parent, row)` | Añade fila como hija de parent | `modelo.append(padre, ["texto", 1])` |
| `prepend(parent, row)` | Añade fila al inicio | `modelo.prepend(None, ["texto", 1])` |
| `insert(parent, pos, row)` | Inserta en posición específica | `modelo.insert(padre, 0, ["texto", 1])` |
| `remove(iter)` | Elimina una fila | `modelo.remove(iterador)` |
| `clear()` | Elimina todas las filas | `modelo.clear()` |

---

## Métodos de Navegación en TreeStore

| Método | Descripción |
|--------|-------------|
| `get_iter_first()` | Obtiene el primer nodo raíz |
| `iter_children(parent)` | Obtiene el primer hijo de parent |
| `iter_next(iter)` | Obtiene el siguiente hermano |
| `iter_parent(iter)` | Obtiene el padre del nodo |
| `iter_has_child(iter)` | Comprueba si tiene hijos |
| `iter_n_children(iter)` | Cuenta los hijos de un nodo |

---

## Diagrama de Componentes

```
┌─────────────────────────────────────────────────┐
│                  Gtk.Window                      │
│  ┌───────────────────────────────────────────┐  │
│  │              Gtk.Box (Vertical)            │  │
│  │  ┌─────────────────────────────────────┐  │  │
│  │  │           Gtk.TreeView              │  │  │
│  │  │  ┌─────────────┬─────────────────┐  │  │  │
│  │  │  │ Parentesco  │      Orde       │  │  │  │
│  │  │  ├─────────────┼─────────────────┤  │  │  │
│  │  │  │ ▸ Avo 0     │        0        │  │  │  │
│  │  │  │   ▸ Pai 0   │        0        │  │  │  │
│  │  │  │     Fillo 0 │        0        │  │  │  │
│  │  │  │     Fillo 1 │        1        │  │  │  │
│  │  │  │   ▸ Pai 1   │        1        │  │  │  │
│  │  │  │ ▸ Avo 1     │        1        │  │  │  │
│  │  │  └─────────────┴─────────────────┘  │  │  │
│  │  └─────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

---

## Resumen de Conceptos Clave

1. **TreeStore vs ListStore**: TreeStore permite estructuras jerárquicas
2. **Punteros/Iteradores**: Necesarios para establecer relaciones padre-hijo
3. **Niveles de anidación**: Sin límite teórico de profundidad
4. **TreeViewColumn**: Define columnas visuales
5. **CellRenderer**: Define cómo se muestra cada celda
