# -*- coding: utf-8 -*-
import mysql.connector

id_codigo = 0
opcion = ""

#Creando nuestro diccionario
datos = {
'host':'127.0.0.1',
'user':'root',
'password':'',
'database':'prueba'

} #Diccionario

conexion = mysql.connector.connect(**datos)#Se colocan dos asteriscos
                                           # porque se esta trabajando
                                           # con un diccionario
cursor = conexion.cursor()# Creamos el cursor
                          # sirve para hacer
                          # consultas
while opcion != "4":
    print ("""
                ****************************************
                 Conexion de Prueba a una Base de Datos
                ****************************************
    """)


    print ("""
    1) Ingresar nuevo registro
    2) Borrar un registro
    3) Mostrar Tabla
    4) Salir
    """)

    opcion = raw_input("    >>> ")

    if opcion == "1":
        print ("""
                ***************************************
                            REGISTRAR USUARIO
                ***************************************
        """)
        Nombres = raw_input ('\n''\t'"Nombre: ")
        Apellidos = raw_input ('\t'"Apellido: ")
        Edad = int(raw_input('\t'"Edad: "))

        consulta = "INSERT INTO usuarios (id_usuarios, Nombres, Apellidos, Edad) VALUES ('%i','%s','%s','%i') " %(id_codigo, Nombres, Apellidos, Edad)
        mensaje = '\n'"         *** El registro se ha guardado con exito ***"

    elif opcion == "2":
        print ("""
                ***************************************
                            Eliminar Registro
                ***************************************
        """)
        
        id_codigo = int(raw_input('\t''\n'"Ingrese el ID :"))
        consulta = "DELETE FROM usuarios WHERE id_usuarios = '%i'" %(id_codigo)
        mensaje = '\n'"         *** El registro se ha eliminado con exito ***"

    elif opcion == "3":
        print ("""
                ***************************************
                                USUARIOS
                ***************************************
        """)

        consulta = ("SELECT id_usuarios, Nombres, Apellidos, Edad FROM usuarios")
        cursor.execute(consulta) # Ejecuta la consulta

        for (id_usuarios, Nombres, Apellidos, Edad) in cursor:
            print (""" | id_usuarios: %i |   Nombres: %s |   Apellidos: %s  | Edad: %i |
            """ % (id_usuarios, Nombres, Apellidos, Edad))

    if opcion == "1" or opcion == "2":
        try:
            cursor.execute(consulta) # Ejecuta la consulta
            conexion.commit() # Guardar los cambios.
            print("%s") %(mensaje) # Imprime el mensaje segun la operacion ejecutada
        except:
            print('\n'"       *** No se a podido realizar la operacion ***")

conexion.close()
