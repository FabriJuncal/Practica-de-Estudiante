from Luz import *
import virtualenv
from flask import Flask


app = Flask(__name__)

Luces = {} # Crear un diccionario para almacenar y hacer globales las instancias.

@app.route('/')
def ControlLuces():
		return 'Controlando Luces'

@app.route('/NuevaLuz/<int:Nid>')
def NuevaLuz(Nid):
	# Instancia un nuevo objeto y lo guarda dentro del diccionario llamado "Luces"
	Luces[Nid] = Luz(Nid)
	print Luces[Nid]    # Muestra en la consola la instancia 
	return ("Luz  L%s Creada!!" % Nid)

@app.route('/Prender/<int:Nid>')
def PrenderLuz(Nid):
	# Prende la luz seleccionada mediante el "id" (Nid)
	try:
		LuzPrendida = Luces[Nid].prender()
		print LuzPrendida   # Muestra en la consola el retorno del id y el estado de la luz (Prendido/Apagado- 1/0)
		return ("Luz  L%s Prendida!" % Nid)
	
	except KeyError:
		return("Ah ocurrido un error, no existe luz con el ID: %s" % Nid)
	
	except:
		return("Ah ocurrido un error inesperado, intente otra vez")
	
	
@app.route('/Apagar/<int:Nid>')
def ApagarLuz(Nid):
	# Apaga la luz seleccionada mediante el "id" (Nid)
	try:
		LuzApagada = Luces[Nid].apagar()
		print LuzApagada # Muestra en la consola el retorno del id y el estado de la luz (Prendido/Apagado- 1/0)
		return ("Luz L%s Apagada!" % Nid)	
	
	except KeyError:
		return("Ah ocurrido un error, no existe luz con el ID: %s" % Nid)
	
	except:
		return("Ah ocurrido un error inesperado, intente otra vez")
	
if __name__ == '__main__':
	app.run( host="0.0.0.0",port=int("5000"))