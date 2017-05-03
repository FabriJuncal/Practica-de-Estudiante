from gi.repository import Gtk

def ingresar_registro(button):
    listado_id.append(entrada_id.get_text())
    listado_tiempos.append(int(entrada_tiempo.get_text()))
    entrada_id.set_text("")
    entrada_tiempo.set_text("")
    etq_resultado.set_text("")

def mostrar_resultado(button):
    indice_ganador=listado_tiempos.index(min(listado_tiempos))
    ganador=listado_id[indice_ganador]
    etq_resultado.set_text(ganador)




listado_id= []
listado_tiempos= []

builder= Gtk.Builder()
builder.add_from_file("competencia.glade")
handlers= {
    "terminar_aplicacion": Gtk.main_quit,
    "evento_tiempo": ingresar_registro,
    "evento_ganador": mostrar_resultado,
    
}
builder.connect_signals(handlers)
window=builder.get_object("ventana_principal")
window.show_all()

entrada_id= builder.get_object("entrada_id")
entrada_tiempo= builder.get_object("entrada_tiempo")
etq_resultado= builder.get_object("etq_resultado")

Gtk.main()
