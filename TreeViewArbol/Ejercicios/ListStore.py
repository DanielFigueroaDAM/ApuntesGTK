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
        # Stock es el tile, celda el renderizador, 2 es el índice de la columna en el modelo
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