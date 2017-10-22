from Luz import *
from Servo import *
import virtualenv
from flask import Flask


app = Flask(__name__)

Luces = {} # Se crea un diccionario para almacenar y hacer globales las instancias de Luz.

servos={}# Se crea un diccionario para almacenar y hacer globales las instancias de Servo.


#    Control de Luz

@app.route('/')
def ControlLuces():
		return 'Controlando Luces y Servos'

@app.route('/NuevaLuz/<int:Nid>')
def NuevaLuz(Nid):
	# Instancia un nuevo objeto y lo guarda dentro del diccionario llamado "Luces"
	Luces[Nid] = Luz(Nid)
	print Luces[Nid]    # Muestra en la consola la instancia 
	return ("Luz  L%s Creada!!" % Nid)

@app.route('/Luz/Prender/<int:Nid>')
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
	
	
@app.route('/Luz/Apagar/<int:Nid>')
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
#----------------------------------------------------------------------------------------------------------------------------------------------------------	

#     Control de Servo

@app.route('/NuevoServo/<int:Nid>') #se crea la instancia de servo con el id
def NuevoServo(Nid):
    servos[Nid]=Servo(Nid)
    return ('Servo ID %s  creado' %Nid)

@app.route('/Servo/<int:Nid>/Mover/<int:angulo>')  # se mueve el servo numero id en un angulo especifico.
def mover(Nid,angulo):
	try:
			mensaje=servos[Nid].mover(angulo)
			print mensaje
			return ('Servo ID %s se movio %s grados' %(Nid, angulo))
	except KeyError:
			return ("Ha ocurrido un error, no exite servo con el ID: %s" %Nid)
	except:
			return ("Ha ocurrido un error inesperado, intente otra vez")	

			
@app.route('/Servo/Abrir/<int:Nid>')  # se abre el servo y quedaria en el angulo 90			
def abrir(Nid):
	try:
			mensaje=servos[Nid].abrir()
			print mensaje
			return ('Servo ID %s  se abrio' %Nid)
	except KeyError:
			return ("Ha ocurrido un error, no exite servo con el ID: %s" %Nid)
	except:
			return ("Ha ocurrido un error inesperado, intente otra vez")

	
@app.route('/Servo/Cerrar/<int:Nid>')	 # se cierra el servo y quedaria en el angulo 0		
def cerrar(Nid):
	try:
			mensaje=servos[Nid].cerrar()
			print mensaje
			return ('Servo ID %s se cerro' %Nid)
	except KeyError:
			return ("Ha ocurrido un error, no exite servo con el ID: %s" %Nid)
	except:
			return ("Ha ocurrido un error inesperado, intente otra vez")	
			
			
if __name__ == '__main__':
	app.run( host="0.0.0.0",port=int("3000"))
