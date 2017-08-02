# -*- coding: utf-8 -*-
import time

class venta():
  def __init__(self):
    self.cliente = ""
    self.valortotal = ""
    self.fecha = ""
    self.venta = []
    self.ventas = []
    self.lista_ventas = []
    self.listaTOT_V = []
    self.ventaLIB = []
    self.comprobanteLIB = []
    self.lisLIBven = []
    self.valorLIB = []
    self.totalV = 0

  def ingresarCLI(self):
    self.cliente = raw_input('\n'" Ingresar nombre del cliente: ")

  def imprimirCLI(self):
    return(self.cliente)


  def imprimirTOT(self):
    print('\n''\n'"El total es " + self.valortotal)


  def listaventas(self,listaventas):
    self.ventas = listaventas
    self.lista_ventas.append(self.ventas)

  def FinVenta(self,Usuario,Editorial,Cliente,NombreLibro,ValorLibro,TotalVenta):
      Fecha = time.strftime("%d/%m/%y")
      Hora = time.strftime('%I:%M:%S %p')
      Editorial = Editorial
      Vendedor = Usuario
      Cliente = Cliente
      NombreLibro = NombreLibro
      ValorLibro = ValorLibro
      TotalVenta = TotalVenta
      self.listaTOT_V.append(TotalVenta)
      self.comprobanteLIB = [Fecha,Hora,Editorial,Cliente,NombreLibro,ValorLibro,TotalVenta,Vendedor]
      self.lista_ventas.append(  self.comprobanteLIB)
      self.lisLIBven = []
      self.valorLIB = []
      self.totalV = 0




  def ImprimirListaVentas(self):

    if len(self.lista_ventas) == 0:
      print('\n'" **** No se ha realizado ninguna venta ****"'\n')


    for j in range(len(self.lista_ventas)):
      print('\n'"  " + str(j+1) + ")")
      j=int(j)
      print("  Fecha: " + self.lista_ventas[j][0])
      print("  Hora: " + self.lista_ventas[j][1] )
      print("  Editorial: " + self.lista_ventas[j][2][0] )
      print("  Localidad: " + self.lista_ventas[j][2][1])
      print("  Cliente: " + self.lista_ventas[j][3])
      print("  Libros que compro: ")
      if len(self.lista_ventas) == 0:
        print("   *** No compro libros ***")
      else:

        for i in (range(len(self.lista_ventas[j][4]))):
          print('\t''\t'"     " + str(i+1) + ") ")
          i=int(i)
          print('\t''\t'"      " + str(self.lista_ventas[j][4][i]) + " " + str(self.lista_ventas[j][5][i]) + "$")
          print('\t''\t'"    --------------------------------")
          i=int(i)

        print('\n''\n'"  Total de la venta: " + str(self.lista_ventas[j][6]) + "$"'\n')
        print("  En caja: " + str(self.lista_ventas[j][7]) + '\n')
        print("**********************************************************")


V = venta()
