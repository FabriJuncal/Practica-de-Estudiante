
print ('\n''\n'"""********************
RADIO DE UN CIRCULO
********************"""'\n')

def radio (respuesta):

    while respuesta=="si":
        r= int(input('\n'"ingrese el radio de su circulo: "'\n''\n'))
        pi=3.14

        print('\n'"La circunferencia es: ",pi*r**2,'\n' )

        respuesta= str(input('\n'"¿Desea seguir calculando?"'\n''\n'))

        while respuesta=="si":
            radio(respuesta)
        else:
            exit

    else :
        exit()

respuesta= str(input('\n'"¿Ingresar radio del circulo?"'\n''\n'))

radio(respuesta)
