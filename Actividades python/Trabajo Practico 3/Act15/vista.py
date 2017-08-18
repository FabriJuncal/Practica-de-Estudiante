#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Interfaz():
  def __init__(self, TipoMenu = ""):
    self.TipoMenu = TipoMenu
    self.Nombre = ""
    self.Apellido = ""
    self.Edad = ""
    self.Carrera = ""
    self.Anio = ""


  
  def MostrarMenu(self):
        opcion = ""
        print """
                ###################################
                          %s
                ###################################
                """'\n' % (self.TipoMenu)
        

        if self.TipoMenu == "Menu Principal":
            print """
1) Registrar Alumno
2) Mostrar Registros
3) Salir
                    """
            opcion = raw_input(" >>> ")
            return(opcion)

        elif self.TipoMenu == "Tabla de Alumnos":
            print """
1) Ordenar por Nombre de la A-Z         6) Ordenar por Edad de mayor a menor
2) Ordenar por Nombre de la Z-A         7) Ordenar por Carrera de la A-Z
3) Ordenar por Apellido de la A-Z       8) Ordenar Por Carrera de la Z-A
4) Ordenar por Apellido de la Z-A       9) Ordenar por Anio de menor a mayor
5) Ordenar por Edad de menor a mayor    10) Ordenar por Anio de mayor a menor
        
        
                  11) Volver al Menu Principal   """
            
            opcion = raw_input("""
                            >>> """)
            return (opcion)

  
  def RegistrarAlumno(self,TipoOpcion, Carrera = ""):
        print """
  %s:
-------------------------------""" % (TipoOpcion)
      
        if TipoOpcion == "Datos del Alumno":
          self.Nombre = raw_input("Nombre: ")
          self.Apellido = raw_input("Apellido: ")
          self.Edad = raw_input("Edad: ")

          return( self.Nombre, self.Apellido, self.Edad)

        elif TipoOpcion == "Carrera a Inscribir":  
          print ("""1) Administracion de Empresa
2) Abogacia
3) Analista de Sistemas
4) Bioseguridad
5) Contador Publico
6) Ingenieria en Electronica
7) Ingenieria Civil
8) Ingenieria en Informatica
9) Nutricionista
10) Medicina
               """)

          opcion = raw_input(">>> ")
        
          if opcion == "1":
            self.Carrera = "Administracion de Empresa"
          elif opcion == "2":
            self.Carrera = "Abogacia"
          elif opcion == "3":
            self.Carrera = "Analista de Sistemas"
          elif opcion == "4":
            self.Carrera = "Bioseguridad"
          elif opcion == "5":
            self.Carrera = "Contador Publico"
          elif opcion == "6":
            self.Carrera = "Ingenieria en Electronica"
          elif opcion == "7":
            self.Carrera = "Ingenieria Civil"
          elif opcion == "8":
            self.Carrera = "Ingenieria en Informatica"
          elif opcion == "9":
            self.Carrera = "Nutricionista"
          elif opcion == "10":
            self.Carrera = "Medicina"

          return(opcion, self.Carrera)
          
        elif TipoOpcion == "Anio Entrante del Alumno":
          if Carrera == "1" or Carrera== "3" or Carrera == "4":
            print """1) Primero
2) Segundo
3) Tercero
              """
            opcion = raw_input(">>> ")

            if opcion == "1":
                 self.Anio = ("Primero", "1")
            elif opcion == "2":
                 self.Anio = ("Segundo", "2")
            elif opcion == "3":
                 self.Anio = ("Tercero", "3")


          elif Carrera == "2" or Carrera == "5" or Carrera == "6" or Carrera == "7" or Carrera == "8" or Carrera == "9":
              print """1) Primero
2) Segundo
3) Tercero
4) Cuarto
5) Quinto
              """
              opcion = raw_input(">>> ")
              if opcion == "1":
                  self.Anio = ("Primero", "1")
              elif opcion == "2":
                  self.Anio = ("Segundo", "2")
              elif opcion == "3":
                  self.Anio = ("Tercero", "3")
              elif opcion == "4":
                  self.Anio = ("Cuarto", "4")
              elif opcion == "5":
                  self.Anio = ("Quinto", "5")

          elif Carrera == "10":
              print """1) Primero
2) Segundo
3) Tercero
4) Cuarto
5) Quinto
6) Sexto
              """
              opcion = raw_input(">>> ")
              if opcion == "1":
                  self.Anio = ("Primero", "1")
              elif opcion == "2":
                  self.Anio = ("Segundo", "2")
              elif opcion == "3":
                  self.Anio = ("Tercero", "3")
              elif opcion == "4":
                  self.Anio = ("Cuarto", "4")
              elif opcion == "5":
                  self.Anio = ("Quinto", "5")
              elif opcion == "6":
                  self.Anio = ("Sexto", "6")

          print '\n'"                     *** Registro Guardado ***"
          return( self.Anio)

    
      
  def MostrarTabla(self):
    print '\n'"""      %-15s|     %-15s |   %-5s |       %-25s | %-5s
---------------------------------------------------------------------------------------------------""" % (
        "Nombres", "Apellidos", "Edad", "Carrera", "Anio")
  
  
      
I = Interfaz()          
              

        
        
        