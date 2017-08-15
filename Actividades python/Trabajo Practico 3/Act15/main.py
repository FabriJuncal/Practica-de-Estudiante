#!/usr/bin/env python
#-*- coding: utf-8 -*-

class RegistroAlumnos():
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = ""
        self.carrera = ""
        self.anio = ()
        self.registro = []

    def RegistrarAlumno(self):
        print """
Datos del Alumno:
------------------
        """
        self.nombre = raw_input("Nombre: ")
        self.apellido = raw_input("Apellido: ")
        self.edad = raw_input("Edad: ")

        print ("""
 Carrera a Inscribir:
--------------------------------
1) Administracion de Empresa
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
            self.carrera = "Administracion de Empresa"
        elif opcion == "2":
            self.carrera = "Abogacia"
        elif opcion == "3":
            self.carrera = "Analista de Sistemas"
        elif opcion == "4":
            self.carrera = "Bioseguridad"
        elif opcion == "5":
            self.carrera = "Contador Publico"
        elif opcion == "6":
            self.carrera = "Ingenieria en Electronica"
        elif opcion == "7":
            self.carrera = "Ingenieria Civil"
        elif opcion == "8":
            self.carrera = "Ingenieria en Informatica"
        elif opcion == "9":
            self.carrera = "Nutricionista"
        elif opcion == "10":
            self.carrera = "Medicina"

        if opcion == "1" or opcion == "3" or opcion == "4":
           print """
        Año entrante del alumno:
        --------------------------
        1) Primero
        2) Segundo
        3) Tercero
            """
           opcion = raw_input(">>> ")

           if opcion == "1":
               self.anio = ("Primero", "1")
           elif opcion == "2":
               self.anio = ("Segundo", "2")
           elif opcion == "3":
               self.anio = ("Tercero", "3")


        elif opcion == "2" or opcion == "5" or opcion == "6" or opcion == "7" or opcion == "8" or opcion == "9":
            print """
Año entrante del alumno:
--------------------------
1) Primero
2) Segundo
3) Tercero
4) Cuarto
5) Quinto

            """
            opcion = raw_input(">>> ")
            if opcion == "1":
                self.anio = ("Primero", "1")
            elif opcion == "2":
                self.anio = ("Segundo", "2")
            elif opcion == "3":
                self.anio = ("Tercero", "3")
            elif opcion == "4":
                self.anio = ("Cuarto", "4")
            elif opcion == "5":
                self.anio = ("Quinto", "5")

        elif opcion == " 10":
            print """
Año entrante del alumno:
--------------------------
1) Primero
2) Segundo
3) Tercero
4) Cuarto
5) Quinto
6) Sexto
            """
        if opcion == "1":
            self.anio = ("Primero", "1")
        elif opcion == "2":
            self.anio = ("Segundo", "2")
        elif opcion == "3":
            self.anio = ("Tercero", "3")
        elif opcion == "4":
            self.anio = ("Cuarto", "4")
        elif opcion == "5":
            self.anio = ("Quinto", "5")
        elif opcion == "6":
            self.anio = ("Sexto", "6")

        registro = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Edad": self.edad,
            "Carrera": self.carrera,
            "Anio": self.anio
        }

        return(registro)

    def AlmacenarRegistro(self, registro):
        self.registro.append(registro)
        print '\n'"    *** Registro Guardado ***"


    def MostrarRegistros(self):

        print """      %-15s|     %-15s |   %-5s |       %-25s | %-5s
---------------------------------------------------------------------------------------------------""" % (
        "Nombres", "Apellidos", "Edad", "Carrera", "Anio")

        for i in range(len(self.registro)):
            Estudiante = self.registro[i].keys()
            Estudiante.sort()
            Nombre = self.registro[i]["Nombre"]
            Apellido = self.registro[i]["Apellido"]
            Edad = self.registro[i]["Edad"]
            Carrera = self.registro[i]["Carrera"]
            Anio = self.registro[i]["Anio"][0]

            print "     %-15s |     %-15s |   %-5s |       %-25s | %-5s" % (Nombre,Apellido,Edad,Carrera,Anio)

    def OrdenamientoCreciente(self,TipoOrdenamiento):

        Estudiante = []
        Ordenamiento = False
        contador = 0

        print """      %-15s|     %-15s |   %-5s |       %-25s | %-5s
---------------------------------------------------------------------------------------------------""" % (
        "Nombres", "Apellidos", "Edad", "Carrera", "Anio")

        if TipoOrdenamiento == "Anio":
            for i in range(len(self.registro)):
                Estudiante.append(self.registro[i][TipoOrdenamiento][1])

            print Estudiante
            Estudiante.sort()
            print Estudiante

            i = 0
            while Ordenamiento != True:

                for j in range(len(self.registro)):

                    if self.registro[j][TipoOrdenamiento][1] == Estudiante[i]:
                        print i
                        print j
                        Nombre = self.registro[j]["Nombre"]
                        Apellido = self.registro[j]["Apellido"]
                        Edad = self.registro[j]["Edad"]
                        Carrera = self.registro[j]["Carrera"]
                        Anio = self.registro[j]["Anio"][0]
                        contador = contador + 1
                        print "     %-15s |     %-15s |   %-5s |       %-25s | %-5s" % (
                        Nombre, Apellido, Edad, Carrera, Anio)

                    if contador == len(self.registro):
                        Ordenamiento = True

                i = i + 1
        else:
            for i in range(len(self.registro)):
                Estudiante.append(self.registro[i][TipoOrdenamiento])

            Estudiante.sort()
            i = 0
            while Ordenamiento != True:

                for j in range(len(self.registro)):

                    if self.registro[j][TipoOrdenamiento] == Estudiante[i]:
                        Nombre = self.registro[j]["Nombre"]
                        Apellido = self.registro[j]["Apellido"]
                        Edad = self.registro[j]["Edad"]
                        Carrera = self.registro[j]["Carrera"]
                        Anio = self.registro[j]["Anio"][0]
                        contador = contador + 1
                        print "     %-15s |     %-15s |   %-5s |       %-25s | %-5s" % (
                            Nombre, Apellido, Edad, Carrera, Anio)

                    if contador == len(self.registro):
                        Ordenamiento = True

                i = i + 1

    def OrdenamientoDecreciente(self,TipoOrdenamiento):

        Estudiante = []
        Bandera = False
        Ordenamiento = False
        contador = 0

        print """      %-15s|     %-15s |   %-5s |       %-25s | %-5s
---------------------------------------------------------------------------------------------------""" % (
        "Nombres", "Apellidos", "Edad", "Carrera", "Anio")

        if TipoOrdenamiento == "Anio":
            for i in range(len(self.registro)):
                Estudiante.append(self.registro[i][TipoOrdenamiento][1])

            print Estudiante
            Estudiante.sort()
            print Estudiante

            i = 0
            n = len(self.registro) - 1
            while Ordenamiento != True:
                for j in range(len(self.registro)):

                    if self.registro[j][TipoOrdenamiento][1] == Estudiante[n - i]:
                        print (n - i)
                        print j
                        Nombre = self.registro[j]["Nombre"]
                        Apellido = self.registro[j]["Apellido"]
                        Edad = self.registro[j]["Edad"]
                        Carrera = self.registro[j]["Carrera"]
                        Anio = self.registro[j]["Anio"][0]
                        contador = contador + 1
                        print "     %-15s |     %-15s |   %-5s |       %-25s | %-5s" % (
                            Nombre, Apellido, Edad, Carrera, Anio)

                    if contador == len(self.registro):
                        Ordenamiento = True

                i = i + 1

        else:

            for i in range(len(self.registro)):
                Estudiante.append(self.registro[i][TipoOrdenamiento])

            Estudiante.sort()
            i = 0
            while Ordenamiento != True:
                n = len(self.registro) - 1
                for j in range(len(self.registro)):

                    if self.registro[j][TipoOrdenamiento] == Estudiante[n - i]:
                        Nombre = self.registro[j]["Nombre"]
                        Apellido = self.registro[j]["Apellido"]
                        Edad = self.registro[j]["Edad"]
                        Carrera = self.registro[j]["Carrera"]
                        Anio = self.registro[j]["Anio"][0]
                        contador = contador + 1
                        print "     %-15s |     %-15s |   %-5s |       %-25s | %-5s" % (
                        Nombre, Apellido, Edad, Carrera, Anio)

                    if contador == len(self.registro):
                        Ordenamiento = True

                i = i + 1

    def Menu(self, TipoMenu, funcion=""):
        opcion = ""
        print """

                ###################################
                    %s
                ###################################

                """ % (TipoMenu)
        if funcion != "":
            eval("%s" % (funcion))

        if TipoMenu == "Menu Principal":
            print """
        1) Registrar Alumno
        2) Mostrar Registros
        3) Salir
                    """
            opcion = raw_input(" >>> ")
            return(opcion)

        if TipoMenu == "Tabla de Alumnos":
            print """
        1) Ordenar por Nombre de la A-Z
        2) Ordenar por Nombre de la Z-A
        3) Ordenar por Apellido de la A-Z
        4) Ordenar por Apellido de la Z-A
        5) Ordenar por Edad de menor a mayor
        6) Ordenar por Edad de mayor a menor
        7) Ordenar por Carrera de la A-Z
        8) Ordenar Por Carrera de la Z-A
        9) Ordenar por Anio de menor a mayor
        10) Ordenar por Anio de mayor a menor
        11) Volver al Menu Principal
                    """
            opcion = raw_input(" >>> ")
            return (opcion)



    def funcionamiento(self):
        opcion = ""

        opcion = RA.Menu("Menu Principal")
        if opcion == "1":
            RA.Menu("Registro del Alumno")
            Registro = RA.RegistrarAlumno()
            RA.AlmacenarRegistro(Registro)
            RA.funcionamiento()

        if opcion == "2":
            opcion = RA.Menu("Tabla de Alumnos", "RA.MostrarRegistros()")

            while opcion != "11":
                if opcion == "1":
                    opcion = RA.Menu("Tabla de Alumnos", "RA.OrdenamientoCreciente('Nombre')")
                elif opcion == "2":
                    opcion = RA.Menu("Tabla de Alumnos", "RA.OrdenamientoDecreciente('Nombre')")
                elif opcion == "3":
                    opcion = RA.Menu("Tabla de Alumnos", "RA.OrdenamientoCreciente('Apellido')")
                elif opcion == "4":
                    opcion = RA.Menu("Tabla de Alumnos", "RA.OrdenamientoDecreciente('Apellido')")
                elif opcion == "5":
                    opcion = RA.Menu("Tabla de Alumnos", "RA.OrdenamientoCreciente('Edad')")
                elif opcion == "6":
                    opcion = RA.Menu("Tabla de Alumnos", "RA.OrdenamientoDecreciente('Edad')")
                elif opcion == "7":
                    opcion = RA.Menu("Tabla de Alumnos", "RA.OrdenamientoCreciente('Carrera')")
                elif opcion == "8":
                    opcion = RA.Menu("Tabla de Alumnos", "RA.OrdenamientoDecreciente('Carrera')")
                elif opcion == "9":
                    opcion = RA.Menu("Tabla de Alumnos", "RA.OrdenamientoCreciente('Anio')")
                elif opcion == "10":
                    opcion = RA.Menu("Tabla de Alumnos", "RA.OrdenamientoDecreciente('Anio')")

            RA.funcionamiento()

        if opcion == "3":
            exit()


RA = RegistroAlumnos()
RA.funcionamiento()
