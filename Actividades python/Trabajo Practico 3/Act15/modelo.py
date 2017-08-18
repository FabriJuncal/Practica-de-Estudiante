#!/usr/bin/env python
#-*- coding: utf-8 -*-

class RegistroAlumnos():
    def __init__(self):
        self.Registro = ""
        self.Tabla = []


    def AgregarRegistro(self, Registro):
      self.Tabla.append(Registro)


    def MostrarTabla(self, Filtro, Ordenamiento):
      Tabla = []
      TablaCompleta = False
      contador = 0

      for i in range ((len(self.Tabla))):
        Tabla.append(self.Tabla[i])

      if Filtro == "Anio":
        if Ordenamiento == "Decreciente":
          Tabla.sort(key=lambda Tabla: Tabla[Filtro][1], reverse=True)


        elif Ordenamiento == "Creciente":
          Tabla.sort(key=lambda Tabla: Tabla[Filtro][1], reverse=False)

      else:
        if Ordenamiento == "Decreciente":
          Tabla.sort(key= lambda Tabla: Tabla[Filtro], reverse=True)

        elif Ordenamiento == "Creciente":
          Tabla.sort(key=lambda Tabla: Tabla[Filtro], reverse = False )


      i = 0
      while TablaCompleta != True:

        for j in range(len(self.Tabla)):

            Nombre = Tabla[j]["Nombre"]
            Apellido = Tabla[j]["Apellido"]
            Edad = Tabla[j]["Edad"]
            Carrera = Tabla[j]["Carrera"]
            Anio = Tabla[j]["Anio"]

            print "     %-15s |     %-15s |   %-5s |       %-25s | %-5s" % (
              Nombre, Apellido, Edad, Carrera, Anio[0])

            contador = contador + 1

        if contador == len(self.Tabla):
          TablaCompleta = True

        i = i + 1

      print """
---------------------------------------------------------------------------------------------------      """

R = RegistroAlumnos()   

      
        
     