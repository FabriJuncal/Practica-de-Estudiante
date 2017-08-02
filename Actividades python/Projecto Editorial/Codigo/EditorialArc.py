# -*- coding: utf-8 -*-

class editorial():
  def __init__(self):
    self.editorial = ""
    self.localidad = ""
    self.LSeditorial = []

  def ingresarEDI(self):
    self.editorial = raw_input('\n'" Ingrese el nombre de la editorial: ")
    self.localidad = raw_input(" Ingrese la localidad de la editorial: ")
    return

  def imprimirEDI(self):
    self.LSeditorial = [self.editorial,self.localidad]
    return(self.LSeditorial)
