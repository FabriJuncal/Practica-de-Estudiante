# -*- coding: utf-8 -*-
import mysql.connector

class BaseDatos():
    def __init__(self): #, datos):
        self.id_codigo = 0
        self.opcion = ""
        #self.datos = datos
        #Creando nuestro diccionario
        self.datos = {
        'host':'127.0.0.1',
        'user':'root',
        'password':'',
        'database':'prueba'
        } #Diccionario

        self.conexion = mysql.connector.connect(**self.datos)#Se colocan dos asteriscos
                                               # porque se esta trabajando
                                               # con un diccionario
        self.cursor = self.conexion.cursor()# Creamos el cursor
                              # sirve para hacer
                              # consultas


    def Registros(self):

        while self.opcion != "5":
            print ("""
                        ***************************************
                        Conexion de Prueba a una Base de Datos
                        ***************************************
            """)


            print ("""
            1) Ingresar nuevo registro
            2) Borrar un registro
            3) Mostrar Tabla
            4) Guardar Registro
            5) Salir
            """)

            self.opcion = raw_input("    >>> ")

            if self.opcion == "1":
                print ("""
                        ***************************************
                                    REGISTRAR USUARIO
                        ***************************************
                """)
                Nombres = raw_input ('\n''\t'"Nombre: ")
                Apellidos = raw_input ('\t'"Apellido: ")
                Edad = int(raw_input('\t'"Edad: "))

                consulta = "INSERT INTO usuarios (id_usuarios, Nombres, Apellidos, Edad) VALUES ('%i','%s','%s','%i') " %(self.id_codigo, Nombres, Apellidos, Edad)
                mensaje = '\n'"             *** El registro se ha guardado con exito ***"

            elif self.opcion == "2":
                print ("""
                        ***************************************
                                    Eliminar Registro
                        ***************************************
                """)

                self.id_codigo = int(raw_input('\t''\n'"Ingrese el ID :"))
                consulta = "DELETE FROM usuarios WHERE id_usuarios = '%i'" %(self.id_codigo)
                mensaje = '\n'"             *** Se ha eliminado el registro de la base de datos ***"

            elif self.opcion == "3":
                print ("""
                        ***************************************
                                        USUARIOS
                        ***************************************
                """)

                consulta = ("SELECT * FROM usuarios")
                self.cursor.execute(consulta) # Ejecuta la consulta

                print """    %-12s  |         %-15s  |        %-15s |       %-5s | 
------------------------------------------------------------------------------------""" % (
                    "id_usuarios", "Nombres", " Apellidos", "Edad")

                for (id_usuarios, Nombres, Apellidos, Edad) in self.cursor:
                    print """      %-12s|     %-20s |   %-20s |       %-5s | 
-------------------------------------------------------------------------------------""" % \
                          (id_usuarios, Nombres, Apellidos, Edad)

            if self.opcion == "1" or self.opcion == "2":
                try:
                    self.cursor.execute(consulta) # Ejecuta la consulta
                    self.conexion.commit() # Guardar los cambios.
                    print("%s") %(mensaje) # Imprime el mensaje segun la operacion ejecutada
                except:
                    print('\n'"             *** No se a podido realizar la operacion ***")


            elif self.opcion == "4":
                BD.CrearArchivo()



        self.conexion.close()







    def CrearArchivo(self):
        consulta = ("SELECT * FROM usuarios")
        self.cursor.execute(consulta)  # Ejecuta la consulta
        nombre = raw_input("Nombre del archivo: ")
        archivo = open(nombre, 'w')
        Campos = """ 
    ****************************
            REGISTROS
    **************************** """+"\n"
        archivo.write(Campos)



        for (id_usuarios, Nombres, Apellidos, Edad) in self.cursor:
            archivo.write("\n"+"ID: "+str(id_usuarios)+"\n"+"Nombre: "+Nombres+"\n"+"Apellido: "+Apellidos+"\n"+"Edad: "+str(Edad)+"\n" )
            archivo.write("""---------------------------------------------------------------------""")
            #archivo.close()
    #print"""      %-12s|     %-20s |   %-20s |       %-5s |
 #% \
  #    (id_usuarios, Nombres, Apellidos, Edad)

 #       )
#        archivo.close()





#print """
#   ************************************
#       Conexion a la Base de Datos
#  ************************************
        
#"""
#host = raw_input("Host: ")
#user = raw_input("User: ")
#password = raw_input("Password: ")
#database = raw_input("Data Base: ")
#datos = {
#        'host':host,
#        'user':user,
#        'password':password,
#        'database':database
#        } #Diccionario


BD = BaseDatos()
BD.Registros()
