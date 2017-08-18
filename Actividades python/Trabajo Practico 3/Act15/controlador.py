#!/usr/bin/env python
#-*- coding: utf-8 -*-
from modelo import *
from vista import *

R = RegistroAlumnos()

class Controlador():
    def __init__(self):
      self.opcion = ""
        
    def Registrar(self):  
     
        Datos = I.RegistrarAlumno("Datos del Alumno")
        Carrera = I.RegistrarAlumno("Carrera a Inscribir") 
        Anio = I.RegistrarAlumno("Anio Entrante del Alumno", Carrera[0])

        Registro = {

            "Nombre": Datos[0],
            "Apellido": Datos[1],
            "Edad": Datos[2],
            "Carrera":Carrera[1],
            "Anio": Anio

        }
        R.AgregarRegistro(Registro)


    def MostrarRegistros(self, Filtro, Ordenamiento):

        I.MostrarTabla()
        R.MostrarTabla(Filtro, Ordenamiento)


    def Arranque(self):
      
      I = Interfaz("Menu Principal")
      self.opcion = I.MostrarMenu()
      
      if self.opcion == "1":
        I = Interfaz("Inscripcion")
        self.opcion = I.MostrarMenu()
        C.Registrar()
        C.Arranque()


      elif self.opcion =="2":
        I = Interfaz("Tabla de Alumnos")
        self.opcion = I.MostrarMenu()
        #C.MostrarRegistros("Nombre","Creciente")

        while self.opcion != "11":
            if self.opcion == "1":
                C.MostrarRegistros("Nombre","Creciente")
            elif self.opcion == "2":
                C.MostrarRegistros("Nombre","Decreciente")
            elif self.opcion == "3":
                C.MostrarRegistros("Apellido","Creciente")
            elif self.opcion == "4":
                C.MostrarRegistros("Apellido","Decreciente")
            elif self.opcion == "5":
                C.MostrarRegistros("Edad","Creciente")
            elif self.opcion == "6":
                C.MostrarRegistros("Edad","Decreciente")
            elif self.opcion == "7":
                C.MostrarRegistros("Carrera","Creciente")
            elif self.opcion == "8":
                C.MostrarRegistros("Carrera","Decreciente")
            elif self.opcion == "9":
                C.MostrarRegistros("Anio","Creciente")
            elif self.opcion == "10":
                C.MostrarRegistros("Anio","Decreciente")

            C.Arranque()

      elif self.opcion == "3":
        exit()


C = Controlador()
C.Arranque()