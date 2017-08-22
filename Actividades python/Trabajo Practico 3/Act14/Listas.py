#!/usr/bin/env python
#-*- coding: utf-8 -*-

#         LISTA

# Las listas son conjuntos ordenados de elementos (números, cadenas, listas, etc). 
# Las listas se delimitan por corchetes ([ ]) y los elementos se separan por comas.
# Las listas pueden contener elementos del mismo tipo:

primos = [2, 3, 5, 7, 11, 13]
diasLaborables = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]


# O pueden contener elementos de tipos distintos:

fecha = ["Lunes", 27, "Octubre", 1997]

# O pueden contener listas:

peliculas = [ ["Senderos de Gloria", 1957], ["Hannah y sus hermanas", 1986]]

# Las listas pueden tener muchos niveles de anidamiento:

directores = [ ["Stanley Kubrick", ["Senderos de Gloria", 1957]], ["Woody Allen", ["Hannah y sus hermanas", 1986]] ]

# Las variables de tipo lista hacen referencia a la lista completa.

lista = [1, "a", 45]

# Una lista que no contiene ningún elemento se denomina lista vacía:

lista = [ ]

# Al definir una lista se puede hacer referencia a otras variables.

nombre = "Pepe"
edad = 25
lista = [nombre, edad]

# Una lista puede contener listas (que a su vez pueden contener listas, que a su vez etc.):

persona1 = ["Ana", 25]
persona2 = ["Benito", 23]
lista = [persona1, persona2]

# Se puede acceder a cualquier elemento de una lista escribiendo el nombre de la lista y entre corchetes el número de orden en la lista.
# El primer elemento de la lista es el número 0.

lista = [10, 20, 30, 40]
lista[2] # 30
lista[0] # 10 
lista[1] # 20
lista[3] # 40
# [10, 20, 30, 40]

# Para cambiar una componente de una lista, se selecciona la componente mediante su índice y se le asigna el nuevo valor.

lista = [10, 20, 30, 40]
lista[2]  = "A"
lista[0] # 10 
lista[1] = "B"
lista[3] # 40
# [10, "B", "A", 40]

#--------------------------------------------------------------------------------------------------------------------------------------------#

# Desempaquetamiento o unpacking

# Hace referencia al método de asignar valores de una lista a un conjunto de objetos.

Elemento1, Elemento2, Elemento3, Elemento4, Elemento5, Elemento6 = NyL

# Esta expresión es equivalente a:


Elemento1 = NyL[0]
Elemento2 = NyL[1]
Elemento3 = NyL[2]
Elemento4 = NyL[3]
Elemento5 = NyL[4]
Elemento6 = NyL[5]

#      NOTA
# Se podra asignar valores mientras se declaren la misma cantidad de objetos o sino saldra un error.

#--------------------------------------------------------------------------------------------------------------------------------------------#

#      Concatenar listas

# Se pueden concatenar dos listas utilizando la operación suma(+):


# 1er Ejemplo:

lista1 = [10, 20, 30, 40]
lista2 = [30, 20]
lista = lista1 + lista2 + lista1

# 2do Ejemplo:

vocales = ["E", "I", "O"]
vocales = vocales + ["U"]
vocales = ["A"] + vocales

# También se puede utilizar el operador += para añadir elementos a una lista:

vocales += ["E"]

#Aunque en estos ejemplos, los operadores + y += den el mismo resultado, no son equivalentes.

#--------------------------------------------------------------------------------------------------------------------------------------------#

#       Manipular elementos individuales de una lista

# Cada elemento se identifica por su posición en la lista, teniendo en cuenta que se empieza a contar por 0.


fecha = [27, "Octubre", 1997]

fecha[0] # 27
fecha[1] # Octubre
fecha[2] # 1997

# Se puede modificar cualquier elemento de una lista haciendo referencia a su posición:

fecha = [27, "Octubre", 1997]
fecha[2] = 1998
fecha[0] # 27
fecha[1] # Octubre
fecha[2] # 1997

# Además, pueden utilizarse índices negativos para comenzar a contar desde el final.
# Por ejemplo, para obtener el último elemento de la lista:

fecha[-1]
# 1997 
#--------------------------------------------------------------------------------------------------------------------------------------------#

#      Slicing

# La traducción más adecuada en Español de slice como un sustantivo sería “un pedazo”, “una porción”, de una lista o tupla. 
# Como un verbo, indicaría “cortar” o “recortar”.

#      Manipular sublistas

# De una lista se pueden extraer sublistas, utilizando la notación nombreDeLista[inicio:límite], 
# donde inicio y límite hacen el mismo papel que en el tipo range(inicio, límite).

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dias[1:4] # Se extrae una lista con los valores 1, 2 y 3

dias[4:5] # Se extrae una lista con el valor 4

dias[4:4] # Se extrae una lista vacía

dias[:4]  # Se extrae una lista hasta el valor 4 (no incluido)

dias[4:]  # Se extrae una lista desde el valor 4 (incluido)

dias[:]   # Se extrae una lista con todos los valores

# Se puede modificar una lista modificando sublistas. 
# De esta manera se puede modificar un elemento o varios a la vez e insertar o eliminar elementos.

letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
letras[1:4] = ["X"]      # Se sustituye la sublista ['B','C','D'] por ['X']

letras[1:4] = ["Y", "Z"] # Se sustituye la sublista ['X','E','F'] por ['Y','Z']

letras[0:1] = ["Q"]      # Se sustituye la sublista ['A'] por ['Q']

letras[3:3] = ["U", "V"] # Inserta la lista ['U','V'] en la posición 3

letras[0:3] = []         # Elimina la sublista ['Q','Y', 'Z']

# Al definir sublistas, Python acepta valores fuera del rango, que se interpretan como extremos (al final o al principio de la lista).

letras = ["D", "E", "F"]
letras[3:3] = ["G", "H"]           # Añade ["G", "H"] al final de la lista

letras[100:100] = ["I", "J"]       # Añade ["I", "J"] al final de la lista

letras[-100:-50] = ["A", "B", "C"] # Añade ["A", "B", "C"] al principio de la lista

#      La palabra reservada del
# La palabra reservada del permite eliminar un elemento o varios elementos a la vez de una lista, e incluso la misma lista.

letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
del letras[4]   # Elimina la sublista ['E']

del letras[1:4] # Elimina la sublista ['B', 'C', 'D']

del letras      # Elimina completamente la lista

# Si se hace referencia a sublistas que contengan valores fuera de rango, python los toma pero lógicamente no se modifican las listas.

letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
del letras[100:200] # No elimina nada

# Además, pueden utilizarse índices negativos para comenzar a contar desde el final. 
# Por ejemplo, para obtener el último elemento de la lista:

letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
letras[-1:]
# H

# Y para obtener todos los elementos a excepción del último.

letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
letras[:-1]
# ["A", "B", "C", "D", "E", "F", "G"]

# O quitando los últimos tres.

letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
letras[:-3]
# ["A", "B", "C", "D", "E"]

# Como indicar cada cuántos elementos se toma un valor.

letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
letras[0:7:2]  # (Rango, CadaCuantosElementosToma)
# ['A', 'C', 'E', 'G']

#--------------------------------------------------------------------------------------------------------------------------------------------#

#           Recorrer una lista

# Se puede recorrer una lista de principio a fin de dos formas distintas:
# Una forma es recorrer directamente los elementos de la lista, es decir, que la variable de control del bucle tome los valores de la lista que estamos recorriendo:

#     Recorrer una lista directamente

letras = ["A", "B", "C"]
for i in letras:
    print(i, end=" ") # A B C

# La otra forma es recorrer indirectamente los elementos de la lista, es decir, 
# que la variable de control del bucle tome como valores los índices de la lista que estamos recorriendo (0,1 ,2 , etc.). 
# En este caso, para acceder a los valores de la lista hay que utilizar letras[i]:

#     Recorrer una lista indirectamente

letras = ["A", "B", "C"]
for i in range(len(letras)):
    print(letras[i], end=" ") # A B C


# La primera forma es más sencilla, pero sólo permite recorrer la lista de principio a fin y utilizar los valores de la lista.
# La segunda forma es más complicada, pero permite más flexibilidad, como muestran los siguientes ejemplos:

#    Recorrer una lista al revés

letras = ["A", "B", "C"]
for i in range(len(letras)-1, -1, -1):
    print(letras[i], end=" ") # C B A


#    modificar los elementos de una lista

# Recorrer y modificar una lista

letras = ["A", "B", "C"]
print(letras)
for i in range(len(letras)):
    letras[i] = "X"
    print(letras)
    
# ['X', 'B', 'C'] (i = 0)
# ['X', 'X', 'C'] (i = 1)
# ['X', 'X', 'X'] (i = 2)

#     Eliminar elementos de la lista

# Para eliminar los elementos de una lista necesitamos recorrer la lista al revés. 
# Si recorremos la lista de principio a fin, al eliminar un valor de la lista, 
# la lista se acorta y cuando intentamos acceder a los últimos valores se produce un error de índice fuera de rango, 
# La solución es recorrer la lista en orden inverso, de manera que aunque se eliminen elementos y la lista se acorte, 
# los valores que todavía no se han recorrido siguen existiendo en la misma posición que al principio.

letras = ["A", "B", "C"]
print(letras)
for i in range(len(letras)-1, -1, -1):
    if letras[i] == "B":
        del letras[i]
    print(letras)

# ['A', 'B', 'C'] (i = 0)
# ['A', 'C']      (i = 1)   
# ['A', 'C']      (i = 2)


#      Saber si un valor está o no en una lista

# Para saber si un valor está en una lista se puede utilizar el operador in. 
# La sintaxis sería "elemento in lista" y devuelve un valor lógico: True si el elemento está en la lista, 
# False si el elemento no está en la lista.

# Por ejemplo, el programa siguiente comprueba si el usuario es una persona autorizada:

personas_autorizadas = ["Alberto", "Carmen"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
  print("Está autorizado")
else:
  print("No está autorizado")
  
# Para saber si un valor no está en una lista se pueden utilizar los operadores not in. 
# La sintaxis sería "elemento not in lista" y devuelve un valor lógico: True si el elemento no está en la lista, 
# False si el elemento está en la lista.

# Por ejemplo, el programa siguiente comprueba si el usuario es una persona autorizada:

personas_autorizadas = ["Alberto", "Carmen"]
nombre = input("Dígame su nombre: ")
if nombre not in personas_autorizadas:
  print("No está autorizado")
else:
  print("Está autorizado")
  
#--------------------------------------------------------------------------------------------------------------------------------------------#  
  
#         Las listas en Python tienen muchos métodos que podemos utilizar:

# Utilizaremos la siguiente lista llamada NyL para todos los ejemplos:

NyL = [1,"A",2,"B",3,"C"]

# append()

# No se puede escoger donde se agregará el valor a la lista (se agregará como el último valor). 
# Puede agregar uno o más valores a una lista a la vez. 
# Cada valor agregado a una lista (en una sola instrucción .append) se considerará un elemento

# Ejemplo 1:

NyL = [1,"A",2,"B",3,"C"]
NyL.append(4)
# [1,"A",2,"B",3,"C",4]

# Ejemplo 2:

NyL = [1,"A",2,"B",3,"C"]
NyL.append([4,"D"])
# [1, 'A', 2, 'B', 3, 'C', [4, 'D']]

#--------------------------------------------------------------------------------------------------------------------------------------------#  

# extend()

# No se puede escoger donde se agregará el valor a la lista (se agregará como el último valor). 
# Puede agregar uno o más valores a una lista a la vez. 
# Cada valor agregado a una lista se convertirá en su propio elemento individual.

# Ejemplo 1:

NyL = [1,"A",2,"B",3,"C"]
NyL.extend(4) # TypeError: 'int' object is not iterable
NyL.extend("4") # Forma correcta
# [1, 'A', 2, 'B', 3, 'C', '4']

# Ejemplo 2 :

NyL = [1,"A",2,"B",3,"C"]
NyL.extend([4,"D"])
# [1, 'A', 2, 'B', 3, 'C', 4, 'D']

#--------------------------------------------------------------------------------------------------------------------------------------------#

# insert()

#P uede seleccionar dónde se agregará el valor a la lista. Sólo puede agregar un valor a una lista a la vez. 
# Cada valor que inserte en una lista se considera un elemento.
# Para insertar un nuevo valor en la posición cuyo índice es k (y desplazar un lugar el resto de la lista) se utiliza la operación insert().

NyL = [1,"A",2,"B",3,"C"]
NyL.insert(3, "Python") # (indice, valor)

# [1,"A",2,"B","Python",3,"C",4]

#          NOTA
# Las listas no controlan si se insertan elementos repetidos, si necesitamos exigir unicidad, 
# debemos hacerlo mediante el código de nuestros programas.

#--------------------------------------------------------------------------------------------------------------------------------------------#  
  
# remove()

# Para eliminar un valor de una lista se utiliza la operación remove().

NyL = [1,"A",2,"B",3,"C"]
NyL.remove("Python")

# [1,"A",2,"B",3,"C",4]

#          NOTA
# Si el valor a borrar está repetido, se borra sólo su primera aparición.

#--------------------------------------------------------------------------------------------------------------------------------------------#  
  
# index()

# Para averiguar la posición de un valor dentro de una lista usaremos la operación index().

NyL = [1,"A",2,"B",3,"C"]
NyL.index("C")
# 5

#          NOTA
# Si el valor está repetido, el índice que devuelve es el de la primera aparición.

#--------------------------------------------------------------------------------------------------------------------------------------------#

# len()	

# Devuelve la Cantidad de elementos de la secuencia 

NyL = [1,"A",2,"B",3,"C"]
len(NyL)
# 7

#--------------------------------------------------------------------------------------------------------------------------------------------#

# min() 

# Devuelve el Mínimo elemento de la secuencia 
# Como ejemplo para este metodo utilizaremos dos listas para que se entienda mejor

NyL= [23,55,1,67,100,13,10]
min(NyL)
# 1

NyL= ["G","L","A","Y","R","Z","W","Q"]
min(NyL)
# A

#--------------------------------------------------------------------------------------------------------------------------------------------#

# max()	

# Devuelve el Máximo elemento de la secuencia 
# Como ejemplo para este metodo utilizaremos dos listas para que se entienda mejor

NyL= [23,55,1,67,100,13,10]
max(NyL)
# 100

NyL= ["G","L","A","Y","R","Z","W","Q"]
max(NyL)
# Z
#--------------------------------------------------------------------------------------------------------------------------------------------#

# enumerate()

# Imprime cada indice con su respectivo valor en forma de tupla.


NyL = [1,"A",2,"B",3,"C"]
list(enumerate(NyL))
# [(0, 1), (1, 'A'), (2, 2), (3, 'B'), (4, 3), (5, 'C')] # (índice, valor)

#  Además, puede indicarse el número desde donde comenzará a contarse (0 por defecto).

NyL = [1,"A",2,"B",3,"C"]
list(enumerate(NyL,1))
# [(1, 1), (2, 'A'), (3, 2), (4, 'B'), (5, 3), (6, 'C')] # (índice, valor)

# Al momento de aplicarlo en un bucle, no es necesario convertirlo a una lista.

for indice, item in enumerate(NyL, 1):
  print "Elemento %d: %s." % (indice, str(item))
  
# Elemento 1: 1.
# Elemento 2: A.
# Elemento 3: 2.
# Elemento 4: B.
# Elemento 5: 3.
# Elemento 6: C.  
  
#--------------------------------------------------------------------------------------------------------------------------------------------#

# pop()

# Remueve un ítem indicando su posición y obtiene el valor eliminado.

NyL = [1,"A",2,"B",3,"C"]
eliminado = NyL.pop(3)
# NyL = [1,"A",2,3,"C"]
# eliminado = 'B'

#--------------------------------------------------------------------------------------------------------------------------------------------#

# popleft()
eliminado = NyL.popleft(3)




#          BUSCAR COMO FUNCIONA
































# count()

# Determinar cuántas veces aparece un ítem en la lista.

NyL = [1,"A",2,"B",3,"C",1,"A",2,1,"A"]
NyL.count("A")
# 3

#--------------------------------------------------------------------------------------------------------------------------------------------#

# sort()

# Ejemplo 1:

Numeros = [4, 7, 5, 6, 2, 1, 3]
Numeros.sort()
# [1, 2, 3, 4, 5, 6, 7]

# Ejemplo 2:

# En las cadenas, su valor numérico será determinado
# por el código del primer caracter.

Letras = ["G","L","A","Y","R","Z","W","Q"]
Letras.sort()
# ['A', 'G', 'L', 'Q', 'R', 'W', 'Y', 'Z']


ord("A")
# 65
ord("G")
# 71
ord("L")
# 76
ord("Q")
# 81
ord("R")
# 82
ord("W")
# 87
ord("W")
# 87
ord("Y")
# 89
ord("Z")
# 90

#--------------------------------------------------------------------------------------------------------------------------------------------#

# reverse()

# Invierte el orden de todos los elementos.

NyL= [1, 2, 3, 4, 5]
NyL.reverse()

#--------------------------------------------------------------------------------------------------------------------------------------------#

# zip()

#  Lo que hace es tomar el elemento iésimo de cada lista y unirlos en una tupla.

Nombres = ["Alejandro","Fabricio","Yesica","Erika","Ulises"]
Apellidos = ["Gonzales","Juncal","Nuñez","Klein","Ibañez"]
Edades = [40,20,18,38,15]
Registro = zip(Nombres,Apellidos,Edades)

# [('Alejandro', 'Gonzales', 40), ('Fabricio', 'Juncal', 20), ('Yesica', 'Nuñez', 18), ('Erika', 'Klein', 38), ('Ulises', 'Ibañez', 15)]

# Como utilizar zip con un for.

for nombre, apellido, edad in zip(Nombres, Apellidos, Edades):
  print("%s %s: %d." % (nombre, apellido, edad))

# Alejandro Gonzales: 40.
# Fabricio Juncal: 20.
# Yesica Nuez: 18.
# Erika Klein: 38.
# Ulises Ibaez: 15.  


#--------------------------------------------------------------------------------------------------------------------------------------------#

# sets()

# Un set es un conjunto de elementos únicos y no ordenados. Es decir, un set no puede tener dos o más valores iguales. 
# Tampoco puede accederse a los elementos a través de un índice, tal como es las listas o tuplas, 
# ya que se trata de una colección desordenada de valores.

# Se crea a partir de un iterable (como una lista o tupla). Por ejemplo:

a = [1, 2, 3, 4]
b = set(a)
# b = set([1, 2, 3, 4])

# Si el objeto iterable tiene valores repetidos, serán eliminados.

a = [1, 1, 2, 3, 4, 3, 5, 6, 7, 7, 6]
b = set(a)
# b = set([1, 2, 3, 4, 5, 6, 7])

# Teniendo en cuenta esto, un interesante método para eliminar los valores repetidos de una lista es:

list(set(lista))

#       Otros métodos de los sets:

a = (1, 2, 3, 4, 5)
b = set(a)
# b = set([1, 2, 3, 4, 5])

b.add(6)  # Añadir elemento
# b = set([1, 2, 3, 4, 5, 6])

b.remove(2)  # Eliminar elemento
# b = set([1, 3, 4, 5, 6])

4 in b  # Determinar si existe un elemento
# True
2 in b
# False
0 not in b
# True


#--------------------------------------------------------------------------------------------------------------------------------------------#






























  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
