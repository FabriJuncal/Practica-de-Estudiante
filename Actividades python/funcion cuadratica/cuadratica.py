import math

def menu():
    print('\n''\n'"""     ************
         MENU
     ************
 Pasos para el ejercicio
 ------------------------
 1)Ingrese los valores de A,B,C para la funcion cuadratica.
 2)Ingrese cuantos numeros utilizará para construir la tabla.
 3)Ingrese los valores para la tabla.
 4)Decida si continuará haciendo ejercicios.
"""'\n')

def valores_funcion():
    print('\n''\n'"""    ***********************************************************
    1) Ingresa valores para la función
    ***********************************************************"""'\n''\n')


    a=(input('\n'" valor para A: "))
    if a=="":
        while True:
            a= (input(" Ingrese un valor para A: "))

            if a !="":
                break

    a=int(a)
    b=(input('\n'" valor para B: "))
    if b=="":
        while True:
            b= (input(" Ingrese un valor para B: "))

            if b !="":
                break

    b=int(b)
    c=(input('\n'" valor para C: "))
    if c=="":
        while True:
            c= (input(" Ingrese un valor para C: "))

            if c !="":
                break

    c=int(c)

    print('\n''\n')

    if ((b**2)-4*a*c<0):
        print('\n''\n'"    No se puede calcular por el momento por tener raices complejas."'\n''\n')
        pregunta()

    cantidad_valores(a,b,c)
    cuadratica(a,b,c)


def cantidad_valores(a1,b1,c1):
    print('\n''\n'"""    ***********************************************************
    2) Ingresa la cantidad de valores que tendra la tabla
    ***********************************************************"""'\n''\n')


    i=(input(" Cantidad de valores: "))
    if i=="":
        while True:
            i= (input(" Ingrese la cantidad de valores que tendra la tabla: "))

            if i !="":
                break

    i=int(i)


    tabla(i,a1,b1,c1)


def tabla(x,a,b,c):

    print('\n''\n'"""    ***********************************************************
    3) Ingrese los valores para la tabla
    ***********************************************************"""'\n''\n')

    print("     x  |  fx")
    print("    -----------")
    #print("\n")
    i=1
    for i in range(x):
        #print(str(i)+")")

        i=(input (" "+str(i+1)+") "))
        if i=="":
            while True:
                i= (input(" "+str(i)+") "))
                if i =="":
                    print("\t"+"|"+"\t")
                if i !="":
                    break

        i=int(i)
        print("\t"+"|"+"\t" + str(a*(i**2)+b*i+c))



        #print(str(i)+"\t"+"|"+"\t" + str(a*x**2+b*x+c))
    #for i in range (x,2):



        #print(str(i)+"\t"+"|"+"\t" + str(a*x**2+b*x+c))
        #print repr(x).rjust(3), repr(a*x*x+b*x+c).rjust(3),




def cuadratica(a2,b2,c2):

    k=(b2**2)
    l=-4*a2*c2
    s=k+l
    s=math.sqrt(s)
    #s=math.sqrt((b2**2)(-4*a2*c2))

    xUNO = (-b2-s)/(2*a2)
    xDOS = (-b2+s)/(2*a2)

    verX= ((xUNO+xDOS)/2)
    verY= (a2*verX**2+b2*verX+c2)

    resultado_cuadratica(a2,b2,c2,xUNO,xDOS,verX,verY)

def resultado_cuadratica(a,b,c,x1,x2,vx,vy):


    print('\n''\n'"""    **********************
     FUNCIÓN CUADRATICA
    **********************"""'\n''\n')

    print( "     y= " + str(a) +" x^2 + " + str(b) + " x + " +str(c))
    print('\n''\n')
    print(" La ordenada al origen es: "+ str(c) )
    print(" La raiz x1= "+ str(x1))
    print(" La raiz x2= "+str(x2))
    print(" El vertice de la función es:  " +"(" +(str(vx)+ " ; "+str(vy)+")"))
    print(" La funcion cuadratica tiene Dominio: (Reales)")

    pregunta()


def pregunta():
    print('\n''\n'"""    ***********************************************************
    4) ¿Desea seguir haciendo ejercicios?
    ***********************************************************"""'\n''\n')

    p=str(input(" "))

    if p== "si":
        valores_funcion()

    else:
        exit()




menu()
valores_funcion()
