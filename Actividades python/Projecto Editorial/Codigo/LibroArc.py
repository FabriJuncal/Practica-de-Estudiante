# -*- coding: utf-8 -*-

class libro():
  def __init__(self):
    self.nombrelib=""
    self.valor=""
    self.autor=""
    self.aniopublicacion=""
    self.genero=""
    self.color=""
    self.ListaAutores = []
    self.LibroRegistrado=[]
    self.respuesta = ""



  def ingresarLIB(self):
    self.nombrelib=raw_input('\n'"Nombre: ")
    self.valor=raw_input("Precio: ")
    self.aniopublicacion=raw_input("Año de publicacion: ")
    self.genero=raw_input("Género: ")
    self.color=raw_input("Color de portada: ")
    self.LibroRegistrado = [self.nombrelib,self.valor,self.aniopublicacion,self.genero,self.color]
    return(self.LibroRegistrado)

  def ingresarAUT(self):
      self.autor = raw_input("Autor: ")
      return(str(self.autor))

  def RegistroLibros(self):
      UnAutor = True
      self.LibroRegistrado = l.ingresarLIB()
      while self.respuesta != "no":
          if UnAutor == True:
              Autor = l.ingresarAUT()
              self.ListaAutores.append(Autor)
              UnAutor = False
          else:
              self.respuesta = raw_input(" Ingresar otro Autor?"'\n''\t')
              if self.respuesta == "si" or self.respuesta == "Si" or self.respuesta == "SI":
                  Autor = l.ingresarAUT()
                  self.ListaAutores.append(Autor)

      UnAutor = True
      self.respuesta = ""
      self.LibroRegistrado.append(self.ListaAutores)
      self.ListaAutores = []
      return(self.LibroRegistrado)

l = libro()
