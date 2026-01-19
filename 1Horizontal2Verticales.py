import  gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_default_size(800,600)
        self.iniciarView()

    def iniciarView(self):
        caixaHorizontal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        caixaVertical1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixaVertical2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        caixaPadre = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        # meter caja Horizontal en caja padre
        caixaPadre.pack_start(caixaHorizontal, True, True, 5)
        # meter cajas verticales en caja horizontal
        caixaHorizontal.pack_start(caixaVertical1, True, True, 5)
        caixaHorizontal.pack_start(caixaVertical2, True, True, 5)
        #el primer true es para expandir
        #el segundo true es para llenar el espacio asignado
        #el 5 es el espacio entre elementos

        #meter un texto un en la primera la caja horizontal
        etiqueta1 = Gtk.Label(label="Caja Horizontal")
        caixaHorizontal.pack_start(etiqueta1, False, False, 5)
        # meter texto en la caja vertical 1
        etiqueta2 = Gtk.Label(label="Caja Vertical 1")
        caixaVertical1.pack_start(etiqueta2, False, False, 5)
        # meter texto en la caja vertical 2
        etiqueta3 = Gtk.Label(label="Caja Vertical 2")
        caixaVertical2.pack_start(etiqueta3, False, False, 5)

        self.add(caixaPadre)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    MainWindow()
    Gtk.main()

