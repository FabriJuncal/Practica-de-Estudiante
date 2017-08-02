# -*- coding: utf-8 -*-
from LibroArc import libro
l = libro()

class Libreria():

    def __init__(self):
        self.respuesta = ""
        self.LibroRegistrado = []
        self.ListaLibros = []

    def RegistrarLibro(self):
        self.LibroRegistrado = l.RegistroLibros()

    def GuardarRegistro(self):
        self.ListaLibros.append(self.LibroRegistrado)
        print('\n'"      **** El registro se a guardado con exito ****")

    def ListaLibro(self):
        return(self.ListaLibros)

    def buscarLIB(self):
      NoExisteLibro = True
      nombre_libro= raw_input('\n'"  Nombre del libro: ")
      for i in range(len(self.ListaLibros)):
        if nombre_libro == self.ListaLibros[i][0]:
          NoExisteLibro = False
          nombrelib = self.ListaLibros[i][0]
          valor = self.ListaLibros[i][1]
          aniopublicacion = self.ListaLibros[i][2]
          genero = self.ListaLibros[i][3]
          color = self.ListaLibros[i][4]

          print('\n'"Nombre: " + nombrelib)
          print("Precio: " + valor + "$")
          print("Año de publicacion: " + aniopublicacion)
          print("Género: " + genero)
          print("Color de portada: " + color)
          if len(self.ListaLibros[i][5]) > 1:
            print("Autores: ")
            for j in range(len(self.ListaLibros[i][5])):
                print("      " + str(j+1) + ")" + self.ListaLibros[i][5][j])
                j = int(j)
          else:
              print("Autor: " + self.ListaLibros[i][5][0])


      if NoExisteLibro == True:
          print('\n'"      **** No existe el libro en el registro ****")


L = Libreria()
