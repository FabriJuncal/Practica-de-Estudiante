from gi.repository import Gtk


def pasar_ventana2 (button):

    ventana2.show_all()

def pasar_ventana3(button):

    ventana3.show_all()

def pasar_ventana1(button):

    ventana1.show_all()


builder= Gtk.Builder()
builder.add_from_file("ventanas.glade")
handlers= {
    "terminar_app": Gtk.main_quit,
    "evento_pasarventana2": pasar_ventana2,
    "evento_pasarventana3": pasar_ventana3,
    "evento_pasarventana1": pasar_ventana1,

}
builder.connect_signals(handlers)
ventana1=builder.get_object("ventana1")
ventana2=builder.get_object("ventana2")
ventana3=builder.get_object("ventana3")

ventana1.show_all()

Gtk.main()
