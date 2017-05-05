def menu():
    print('\n''\n'"""************
CALCULADORA
************
Menu
------------
1)Suma
2)Resta
3)Multiplicacion
4)Division
5)Salir"""'\n')

def Calculadora():
    menu()
    opcion=int(input('\n'"Seleccione una opcion con un numero:"'\n''\n'))

    while opcion<5 and opcion>0:
        n1=int(input('\n'"Ingrese el primer Nro: "))
        n2=int(input('\n'"Ingrese el segundo Nro: "))

        if opcion==1:
            print ('\n'"La suma es: ",n1+n2)
            opcion=int(input('\n'"Seleccione una opcion con un numero:"'\n''\n'))

        elif opcion==2:
            print('\n'"La resta es: ",n1-n2)
            opcion=int(input('\n'"Seleccione una opcion con un numero:"'\n''\n'))

        elif opcion==3:
            print('\n'"La multiplicacion es: ",n1*n2)
            opcion=int(input('\n'"Seleccione una opcion con un numero:"'\n''\n'))

        elif opcion==4:
            print('\n'"La division es: ", float(n1/n2))
            opcion=int(input('\n'"Seleccione una opcion con un numero:"'\n''\n'))
        elif opcion==5:

            exit()

Calculadora()
