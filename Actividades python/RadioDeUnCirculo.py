
def radio (respuesta):

    while respuesta=="si":
        r= int(input("ingrese el radio de su circulo: "'\n'))
        pi=3.14

        print("La circunferencia es: ",pi*r**2 )

        respuesta= str(input("¿Desea seguir calculando?"'\n'))

        while respuesta=="si":
            radio(respuesta)
        else:
            exit()

    else :
        exit()

respuesta= str(input("¿Ingresar radio del circulo?"'\n'))

radio(respuesta)
