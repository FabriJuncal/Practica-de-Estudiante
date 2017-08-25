#!/usr/bin/env python
#-*- coding: utf-8 -*-

print '\n'"Utilizando una lista y tuplas con la funcion ZIP"'\n'

Nombres = ["Alejandro","Fabricio","Yesica","Erika","Ulises"]
Apellidos = ["Gonzales","Juncal","Nuñez","Klein","Ibañez"]
Edades = [40,20,18,38,15]
Registro = zip(Nombres,Apellidos,Edades)

# [('Alejandro', 'Gonzales', 40), ('Fabricio', 'Juncal', 20), ('Yesica', 'Nuñez', 18), ('Erika', 'Klein', 38), ('Ulises', 'Ibañez', 15)]

# Como utilizar zip con un for.

for nombre, apellido, edad in zip(Nombres, Apellidos, Edades):
  print("%s %s: %d." % (nombre, apellido, edad))

print '\n'"Utilizando un diccionario"'\n'

dia = {
"lunes" : "Hoy hay analisis matematico",
"martes" : "Hoy se programa",
"miércoles" : "Se practica consultas",
"jueves" : "Se vuelve a programar!!",
"viernes" : "Al fin viernes, pero hay estadistica",
"sabado":"Se sale de jodaaa!!",
"Domingo":"Dia de la resaca"
}

for dia, comentario in dia.items():
   print dia, ":", comentario
