from gi.repository import Gtk
import random
def convertir(button):
    if combo_conversion.get_active_text()== "Dolar a Peso":
        dolar= int(entrada_conversion.get_text())
        pesos= dolar/tasa_cambio
        etq_conv_resultado.set_text(str(dolar) + " USD son " + str(pesos)+"$" )
    elif combo_conversion.get_active_text()== "Fahrenheit a Celsius":
        fahrenheit = float (entrada_conversion.get_text())
        celsius= (fahrenheit-32)*5/9
        etq_conv_resultado.set_text(str(fahrenheit) + "°F son " + str(celsius) + "°C")
    else:
        etq_conv_resultado.set_text("Debe seleccionar una opcion")

def mostrar_frase (button):
    indice= random.randint(0,len(frases)-1)
    buffer_frase.set_text(frases[indice])

frases= []
frases.append("Vive la vida.")
frases.append("Esta libertadores tambien es de River.")
frases.append("El que no salta es un bostero puto.")
tasa_cambio= 1/17


builder= Gtk.Builder()
builder.add_from_file("cuaderno.glade")
handlers= {
    "terminar_aplicacion": Gtk.main_quit,
    "evento_conversion": convertir,
    "evento_frase": mostrar_frase,

}
builder.connect_signals(handlers)
window=builder.get_object("ventana_principal")
combo_conversion=builder.get_object("combo_conversion")
entrada_conversion= builder.get_object("entrada_conversion")
etq_conv_resultado= builder.get_object("etq_conv_resultado")
buffer_frase=builder.get_object("buffer_frase")

window.show_all()



Gtk.main()
