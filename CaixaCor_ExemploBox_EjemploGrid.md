# CaixaCor, ExemploBox y EjemploGrid - Documentación Completa

## Resumen General

Estos tres archivos forman un sistema educativo para aprender layouts en GTK 3.0:

1. **CaixaCor.py** - Componente base que dibuja cajas de color
2. **ExemploBox.py** - Demuestra cómo usar `Gtk.Box` para organizar elementos
3. **EjemploGrid.py** - Demuestra cómo usar `Gtk.Grid` para organizar elementos

---

## 1. CaixaCor.py - Componente Personalizado

### Descripción

`CaixaCor` es una clase personalizada que hereda de `Gtk.DrawingArea` para crear un widget que dibuja un rectángulo de color sólido.

### Código Completo

```python
import  gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject

class CaixaCor(Gtk.DrawingArea):
    def __init__(self,color):
        super().__init__()
        self.set_size_request(50,50)
        rgba = Gdk.RGBA() # RGBA: (r=0.0-1.0, g=0.0-1.0, b=0.0-1.0 a=0.0-1.0) Entre 0.0 y 1.0
        rgba.parse(color)
        self.color = rgba
        self.connect("draw",self.on_draw)

    def on_draw(self,control,cr):
        r,g,b,a = self.color
        cr.set_source_rgba(r,g,b,a)
        cr.paint()
```

### Clase: `CaixaCor`

**Herencia:** `Gtk.DrawingArea`

Una **DrawingArea** es un widget que permite dibujar gráficos directamente en él mediante un contexto Cairo.

### Constructor: `__init__(self, color)`

**Parámetros:**
- `color` (str): Nombre del color en inglés (ej: "red", "blue", "yellow", etc.)

**Proceso:**

1. **Llamada al constructor padre:**
   ```python
   super().__init__()
   ```

2. **Establecer tamaño mínimo:**
   ```python
   self.set_size_request(50,50)
   ```
   Define un tamaño de 50x50 píxeles para la caja

3. **Parsear el color:**
   ```python
   rgba = Gdk.RGBA()
   rgba.parse(color)
   self.color = rgba
   ```
   - Crea un objeto `Gdk.RGBA()` que representa un color
   - `parse()` convierte el nombre del color a valores RGBA (0.0 a 1.0)
   - Almacena el color en `self.color`

4. **Conectar el evento de dibujo:**
   ```python
   self.connect("draw", self.on_draw)
   ```
   Cuando GTK necesita redibujar el widget, llama a `on_draw`

### Método: `on_draw(self, control, cr)`

**Parámetros:**
- `control`: El widget que generó el evento
- `cr`: Contexto de Cairo para dibujar

**Proceso:**

1. **Extraer componentes RGBA:**
   ```python
   r,g,b,a = self.color
   ```

2. **Establecer color de relleno:**
   ```python
   cr.set_source_rgba(r,g,b,a)
   ```

3. **Pintar toda el área:**
   ```python
   cr.paint()
   ```
   Rellena toda la DrawingArea con el color establecido

### Uso

```python
caja_roja = CaixaCor("red")     # Caja roja 50x50
caja_azul = CaixaCor("blue")    # Caja azul 50x50
caja_verde = CaixaCor("green")  # Caja verde 50x50
```

### Colores Soportados

GTK soporta nombres de colores estándar de CSS:
- Básicos: `red`, `green`, `blue`, `yellow`, `orange`, `purple`, `pink`, `brown`, `black`, `white`, etc.
- También soporta notación hexadecimal: `#FF0000`, `#00FF00`, etc.

---

## 2. ExemploBox.py - Layouts con Box

### Descripción

Demuestra cómo usar `Gtk.Box` para organizar widgets en disposiciones lineales (horizontal o vertical).

### Código Completo

```python
import  gi
import CaixaCor
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject

class EjemplosBoxColor(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de uso de box layout")

        caixa = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 10)

        caixav1 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        caixav1.pack_start(CaixaCor.CaixaCor("red"),True,True,5)
        caixav1.pack_start(CaixaCor.CaixaCor("purple"),True,True,5)
        caixav1.pack_start(CaixaCor.CaixaCor("yellow"),True,True,5)
        caixa.pack_start(caixav1,True,True,5)

        caixa.pack_start(CaixaCor.CaixaCor("green"),True,True,5)

        caixav2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixav2.pack_start(CaixaCor.CaixaCor("red"),True,True,5)
        caixav2.pack_start(CaixaCor.CaixaCor("purple"),True,True,5)
        caixa.pack_start(caixav2,True,True,5)

        self.add(caixa)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemplosBoxColor()
    Gtk.main()
```

### Clase: `EjemplosBoxColor`

**Herencia:** `Gtk.Window`

### Estructura del Layout

```
┌─────────────────────────────────────────────┐
│  caixa (HORIZONTAL, spacing=10)             │
├───────────────────────┬─────────┬───────────┤
│ caixav1 (VERTICAL)    │  Green  │caixav2    │
│  - Red                │         │ (VERTICAL)│
│  - Purple             │         │  - Red    │
│  - Yellow             │         │  - Purple │
└───────────────────────┴─────────┴───────────┘
```

### Método: `__init__(self)`

#### 1. Crear contenedor principal HORIZONTAL

```python
caixa = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10)
```

- **orientation**: Los elementos se organizan de izquierda a derecha
- **spacing**: 10 píxeles de separación entre elementos

#### 2. Crear primer contenedor vertical (izquierda)

```python
caixav1 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
caixav1.pack_start(CaixaCor.CaixaCor("red"),True,True,5)
caixav1.pack_start(CaixaCor.CaixaCor("purple"),True,True,5)
caixav1.pack_start(CaixaCor.CaixaCor("yellow"),True,True,5)
```

Contiene 3 cajas apiladas verticalmente: rojo, púrpura, amarillo

**Parámetros de `pack_start()`:**
- Widget a añadir
- `True` = Expandir (llenar espacio disponible)
- `True` = Llenar (ocupar todo el espacio asignado)
- `5` = Espaciado interno (padding)

#### 3. Añadir caixa vertical al contenedor principal

```python
caixa.pack_start(caixav1,True,True,5)
```

#### 4. Añadir caja verde directamente al contenedor principal

```python
caixa.pack_start(CaixaCor.CaixaCor("green"),True,True,5)
```

#### 5. Crear segundo contenedor vertical (derecha)

```python
caixav2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
caixav2.pack_start(CaixaCor.CaixaCor("red"),True,True,5)
caixav2.pack_start(CaixaCor.CaixaCor("purple"),True,True,5)
caixa.pack_start(caixav2,True,True,5)
```

Contiene 2 cajas apiladas verticalmente: rojo, púrpura

### Conceptos Clave de Box

| Concepto | Descripción |
|----------|------------|
| **Orientación** | `HORIZONTAL` (izq-derecha) o `VERTICAL` (arriba-abajo) |
| **Spacing** | Espacio automático entre elementos |
| **pack_start()** | Añade elemento desde el inicio del box |
| **pack_end()** | Añade elemento desde el final del box |
| **expand** | El widget expande para llenar espacio disponible |
| **fill** | El widget llena todo el espacio que se le asigna |
| **padding** | Espaciado interno del widget |

---

## 3. EjemploGrid.py - Layouts con Grid

### Descripción

Demuestra cómo usar `Gtk.Grid` para organizar widgets en una estructura de rejilla (filas y columnas).

### Código Completo

```python
import  gi
from EjemploEssemtia.CaixaCor import CaixaCor
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject

"""Diseño

rojo-marron-amarillo-naranja
rojo-verde-verde-morado
azul-azul-rosa-negro

"""

class EjemplosBoxColor(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de uso de grid layout")

        rojo = CaixaCor("red")
        morado = CaixaCor("purple")
        amarillo = CaixaCor("yellow")
        verde = CaixaCor("green")
        azul = CaixaCor("blue")
        rosa = CaixaCor("pink")
        naranja = CaixaCor("orange")
        marron = CaixaCor("brown")
        negro = CaixaCor("black")

        caixa = Gtk.Grid()
        caixa.attach_next_to(rojo,None,Gtk.PositionType.LEFT,1,2)
        caixa.attach_next_to(marron,rojo,Gtk.PositionType.RIGHT,1,1)
        caixa.attach_next_to(verde, marron, Gtk.PositionType.BOTTOM, 2, 1)
        caixa.attach_next_to(azul, rojo, Gtk.PositionType.BOTTOM, 2, 1)

        caixa.attach_next_to(amarillo, marron, Gtk.PositionType.RIGHT, 1, 1)
        caixa.attach_next_to(rosa, azul, Gtk.PositionType.RIGHT, 1, 1)
        caixa.attach_next_to(morado, verde, Gtk.PositionType.RIGHT, 1, 1)

        caixa.attach_next_to(naranja, morado, Gtk.PositionType.TOP, 1, 1)
        caixa.attach_next_to(negro, morado, Gtk.PositionType.BOTTOM, 1, 1)

        self.add(caixa)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemplosBoxColor()
    Gtk.main()
```

### Clase: `EjemplosBoxColor`

**Herencia:** `Gtk.Window`

### Estructura del Layout

El diseño comentado en el código describe la disposición:

```
ROJO        MARRÓN      AMARILLO    NARANJA
ROJO        VERDE       VERDE       MORADO
AZUL        AZUL        ROSA        NEGRO
```

### Visualización Gráfica Paso a Paso

#### Paso 1: Crear Grid y posicionar ROJO

```python
caixa = Gtk.Grid()
caixa.attach_next_to(rojo, None, Gtk.PositionType.LEFT, 1, 2)
```

- Coloca ROJO a la izquierda (`LEFT`)
- Ocupa 1 columna × 2 filas

```
ROJO
ROJO
```

#### Paso 2: Posicionar MARRÓN a la derecha de ROJO

```python
caixa.attach_next_to(marron, rojo, Gtk.PositionType.RIGHT, 1, 1)
```

```
ROJO  MARRÓN
ROJO
```

#### Paso 3: Posicionar VERDE debajo de MARRÓN (2×1)

```python
caixa.attach_next_to(verde, marron, Gtk.PositionType.BOTTOM, 2, 1)
```

```
ROJO  MARRÓN
ROJO  VERDE  VERDE
```

#### Paso 4: Posicionar AZUL debajo de ROJO (2×1)

```python
caixa.attach_next_to(azul, rojo, Gtk.PositionType.BOTTOM, 2, 1)
```

```
ROJO  MARRÓN
ROJO  VERDE  VERDE
AZUL  AZUL
```

#### Paso 5: Posicionar AMARILLO a la derecha de MARRÓN

```python
caixa.attach_next_to(amarillo, marron, Gtk.PositionType.RIGHT, 1, 1)
```

```
ROJO  MARRÓN  AMARILLO
ROJO  VERDE   VERDE
AZUL  AZUL
```

#### Paso 6: Posicionar ROSA a la derecha de AZUL

```python
caixa.attach_next_to(rosa, azul, Gtk.PositionType.RIGHT, 1, 1)
```

```
ROJO  MARRÓN  AMARILLO
ROJO  VERDE   VERDE
AZUL  AZUL    ROSA
```

#### Paso 7: Posicionar MORADO a la derecha de VERDE

```python
caixa.attach_next_to(morado, verde, Gtk.PositionType.RIGHT, 1, 1)
```

```
ROJO  MARRÓN  AMARILLO
ROJO  VERDE   VERDE     MORADO
AZUL  AZUL    ROSA
```

#### Paso 8: Posicionar NARANJA encima de MORADO

```python
caixa.attach_next_to(naranja, morado, Gtk.PositionType.TOP, 1, 1)
```

```
ROJO  MARRÓN  AMARILLO  NARANJA
ROJO  VERDE   VERDE     MORADO
AZUL  AZUL    ROSA
```

#### Paso 9: Posicionar NEGRO debajo de MORADO

```python
caixa.attach_next_to(negro, morado, Gtk.PositionType.BOTTOM, 1, 1)
```

```
ROJO  MARRÓN  AMARILLO  NARANJA
ROJO  VERDE   VERDE     MORADO
AZUL  AZUL    ROSA      NEGRO
```

### Método: `attach_next_to()`

**Sintaxis:**
```python
grid.attach_next_to(widget, sibling, side, width, height)
```

**Parámetros:**
- `widget`: El widget a añadir
- `sibling`: El widget de referencia (o `None` para la primera posición)
- `side`: Dirección relativa al sibling (`LEFT`, `RIGHT`, `TOP`, `BOTTOM`)
- `width`: Número de columnas que ocupa
- `height`: Número de filas que ocupa

**Posiciones disponibles:**
- `Gtk.PositionType.LEFT` - A la izquierda
- `Gtk.PositionType.RIGHT` - A la derecha
- `Gtk.PositionType.TOP` - Arriba
- `Gtk.PositionType.BOTTOM` - Abajo

---

## Comparación: Box vs Grid

| Aspecto | Box | Grid |
|--------|-----|------|
| **Organización** | Lineal (fila o columna) | 2D (filas y columnas) |
| **Casos de uso** | Barras de herramientas, menús | Formularios, dashboards |
| **Complejidad** | Más simple | Más potente |
| **Anidar layouts** | Fácil | También fácil |
| **Controles repetitivos** | Box anidados | Grid mejor |

---

## Estructura de Proyecto

```
PythonProject/
├── EjemploGrid.py (Layout con Grid)
├── EjemploEssemtia/
│   ├── CaixaCor.py (Componente de caja de color)
│   └── ExemploBox.py (Layout con Box)
└── ...
```

---

## Conceptos de GTK 3.0

### Ciclo de Vida de una Ventana GTK

1. **Crear widget**: `Gtk.Window()`, `Gtk.Box()`, etc.
2. **Configurar propiedades**: `set_title()`, `set_size_request()`, etc.
3. **Conectar señales**: `connect("signal", callback)`
4. **Mostrar**: `show_all()`
5. **Ejecutar bucle principal**: `Gtk.main()`
6. **Procesar eventos**: Espera a que el usuario interactúe
7. **Cerrar**: Cuando se cierra la ventana, se llama a `Gtk.main_quit()`

### Herencia en GTK

```python
class EjemplosBoxColor(Gtk.Window):
    def __init__(self):
        super().__init__()  # Llama al constructor de Gtk.Window
```

---

## Ejecución

### ExemploBox.py

```bash
cd EjemploEssemtia
python ExemploBox.py
```

### EjemploGrid.py

```bash
cd ..
python EjemploGrid.py
```

---

## Requisitos

```bash
pip install PyGObject
```

En Ubuntu/Debian:
```bash
sudo apt-get install python3-gi gir1.2-gtk-3.0
```

---

## Resumen

✅ **CaixaCor** - Componente reutilizable que dibuja cajas de color  
✅ **ExemploBox** - Demuestra layouts lineales con `Gtk.Box`  
✅ **EjemploGrid** - Demuestra layouts 2D con `Gtk.Grid`  

Estos ejemplos son perfectos para aprender cómo estructurar interfaces gráficas en GTK 3.0 de manera modular y eficiente.
