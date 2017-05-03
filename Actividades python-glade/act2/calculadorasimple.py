from gi.repository import Gtk

def suma (button):
    etiqueta_resultado= builder.get_object("etiqueta_resultado")
    entrada_nro1=builder.get_object("entrada_nro1")
    entrada_nro2=builder.get_object("entrada_nro2")
    nr1= int(entrada_nro1.get_text())
    nr2= int(entrada_nro2.get_text())
    resultado=nr1 + nr2
    etiqueta_resultado.set_text(str(resultado))

builder= Gtk.Builder()
builder.add_from_file("calculadorasimple.glade")
handlers= {
    "terminar_aplicacion": Gtk.main_quit,
    "evento_suma": suma
}
builder.connect_signals(handlers)
window=builder.get_object("ventana_principal")
window.show_all()

Gtk.main()
