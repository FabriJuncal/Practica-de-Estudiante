# -*- coding: utf-8 -*-

class menu():


  def MInicio(self):
    print('\n''\n'u"""     **********************
         MENU DE INICIO
     **********************

 1)Ingresar nombre de la editorial y su localidad.
 2)Salir.""")



  def MTrabajo(self):

    print('\n''\n'u"""     ***********************
         MENU DE TRABAJO
     ***********************

 1)Registrar libro/os.
 2)Mostrar lista de libros.
 3)Menu de venta.
 4)Salir.""")

  def IngresoLibro(self):
     print('\n'"""    Ingrese los datos del libro
       --------------------------------""")

  def PreguntaRegistrarLibro(self):
     print('\n''\t'"     ¿Desea registrar otro libro? s/n"'\t''\t''\t')

  def IngresoLibro(self):
    print('\n'"""             Ingrese los datos del libro
      -----------------------------------------""")

  def ImprimirListaLibros(self):
      print('\n'"""    Lista de Libros
----------------------------""")

  def MenuDatosLibro(self):
    print('\n'"""

 1) Ver datos de un libro.
 2) Volver al menu de trabajo.
 3) Salir.
 """)

  def NoExisteLibro(self):
     print('\n'"      **** No hay libros registrados ****"'\n')

  def MVenta(self):
    print('\n''\n'u"""    *******************
       MENU DE VENTA
    *******************
    1) Vender.
    2) Ver lista de ventas.
    3) Volver al menu de trabajo.
    4) Salir""")


  def Carrito (self):
      print('\n'"     Libros en el carrito    (Escriba FIN para terminar)")
      print("    -----------------------")

  def FinVenta(self):
      print ('\n' """   *** FIN DE VENTA ***"""'\n')


  def ListaVenta(self):
      print('\n''\n'u"""       **********************
           LISTA DE VENTAS
       **********************""")


m = menu()
