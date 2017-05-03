from gi.repository import Gtk

builder= Gtk.Builder()
builder.add_from_file("holamundo.glade")
handlers= {
    "terminar_aplicacion": Gtk.main_quit
}
builder.connect_signals(handlers)
window=builder.get_object("ventana_principal")
window.show_all()

Gtk.main()
