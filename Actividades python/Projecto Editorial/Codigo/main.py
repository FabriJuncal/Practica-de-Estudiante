# -*- coding: utf-8 -*-
import getpass
from EditorialArc import editorial
from LibreriaArc import Libreria
from InterfazArc import menu
from VentaArc import venta

e = editorial()
l = Libreria()
v = venta()
m = menu()

class ControlRespuestas2():

    def __init__(self):
        self.Opcion = 0
        self.respuesta = ""
        self.Usuario = getpass.getuser()
    def ElejirOpcion(self):
      a = raw_input('\n'"  Elija una opcion con los numeros: ")
      return (a)

    def RegistrarLibro(self):
        self.respuesta = "si"
        while self.respuesta == "si" or self.respuesta == "Si" or  self.respuesta == "SI":
            m.IngresoLibro()
            l.RegistrarLibro()
            self.respuesta = ""
            while self.respuesta != "si" and self.respuesta != "Si" and  self.respuesta != "SI" and  self.respuesta != "no" and self.respuesta != "No" and self.respuesta != "NO":
                self.respuesta = raw_input('\n''\t'"     ¿Guardar Registro del Libro? s/n"'\n''\t''\t''\t')
            if self.respuesta == "si" or self.respuesta == "Si" or self.respuesta == "SI":
                l.GuardarRegistro()
                m.PreguntaRegistrarLibro()
                self.respuesta = ""
                while self.respuesta != "si" and self.respuesta != "Si" and  self.respuesta != "SI" and  self.respuesta != "no" and self.respuesta != "No" and self.respuesta != "NO":
                    self.respuesta = raw_input('\t''\t''\t')
                if self.respuesta == "no" or self.respuesta == "No" or self.respuesta == "NO":
                    CR2.MenuTrabajo()
            elif  self.respuesta == "no" or self.respuesta == "No" or self.respuesta == "NO":
                m.PreguntaRegistrarLibro()
                self.respuesta = ""
                while self.respuesta != "si" and self.respuesta != "Si" and  self.respuesta != "SI" and  self.respuesta != "no" and self.respuesta != "No" and self.respuesta != "NO":
                    self.respuesta = raw_input('\t''\t''\t')
                if self.respuesta == "no" or self.respuesta == "No" or self.respuesta == "NO":
                    CR2.MenuTrabajo()

    def MostrarDatosLibro(self):
        self.respuesta = "si"
        while self.respuesta == "si" or self.respuesta == "Si" or  self.respuesta == "SI":
            l.buscarLIB()
            self.respuesta = ""
            while self.respuesta != "si" and self.respuesta != "Si" and  self.respuesta != "SI" and  self.respuesta != "no" and self.respuesta != "No" and self.respuesta != "NO":
                self.respuesta = raw_input('\n''\t''\t'"¿Desea volver a buscar?"'\n''\t''\t''\t')
            if  self.respuesta == "no" or self.respuesta == "No" or self.respuesta == "NO":
                CR2.MenuTrabajo()


    def MostrarListaLibros(self):
        m.ImprimirListaLibros()

        if len(l.ListaLibro()) == 0:
            m.NoExisteLibro()
            CR2.MenuTrabajo()

        else:
            Lista = l.ListaLibro()
            for i in range(len(Lista )):
                print('\n' + str(i+1) + ") " + Lista[i][0])

            m.MenuDatosLibro()
            self.Opcion = CR2.ElejirOpcion()
            if self.Opcion == "1":
             CR2.MostrarDatosLibro()
            elif self.Opcion == "2":
              CR2.MenuTrabajo()
            elif self.Opcion == "3":
              exit()
            else:
              CR2.MostrarListaLibros()

    def CarritoVenta(self):
      NoExisteLibro = True
      NombreLibro = []
      PrecioLibro = []
      TotalVenta = 0
      m.Carrito()
      j = 0
      VentaLibro = ""
      while True:
        VentaLibro = ""
        while VentaLibro == "":

            VentaLibro=(raw_input('\n'" "+str(j+1)+") "))

        if VentaLibro == "fin" or VentaLibro == "Fin" or VentaLibro == "FIN" :
            m.FinVenta()
            Editorial = e.imprimirEDI()
            Cliente = v.imprimirCLI()
            v.FinVenta(self.Usuario,Editorial,Cliente,NombreLibro,PrecioLibro,TotalVenta)
            NombreLibro = []
            PrecioLibro = []
            TotalVenta = 0
            break

        elif VentaLibro !="":
            ListaLibros = l.ListaLibro()
            for i in range(len(ListaLibros)):

                if VentaLibro == ListaLibros[i][0]:
                    print( "\t""\t""\t""\t" +  "   | " + ListaLibros[i][1] + "$")
                    PrecioLibro.append(ListaLibros[i][1])
                    TotalVenta = int(TotalVenta) + int(ListaLibros[i][1])
                    print"-------------------------------------------------"
                    print("TOTAL: " + "\t""\t""\t""\t" + "   | " + str(TotalVenta) + "$")
                    NombreLibro.append(VentaLibro)
                    j=int(j)+1
                    NoExisteLibro = False

            if NoExisteLibro == True:
                print ("\t""\t""\t""\t" +  "   | " + "*NO EXISTE*")
                print"-------------------------------------------------"
                print("TOTAL: " +  "\t""\t""\t""\t" + "   | " + str(TotalVenta) + "$")




    def InicioPrograma(self):
      print ( '\n'" **** Ingresado como %s ****"'\n' %self.Usuario )

      m.MInicio()
      self.Opcion = CR2.ElejirOpcion()
      if self.Opcion == "1":
        e.ingresarEDI()
        CR2.MenuTrabajo()
      elif self.Opcion == "2":
        exit()
      else:
        CR2.InicioPrograma()


    def MenuTrabajo(self):

      m.MTrabajo()
      self.Opcion = CR2.ElejirOpcion()
      if self.Opcion == "1":
        CR2.RegistrarLibro()
        CR2.MenuTrabajo()

      elif self.Opcion == "2":
        CR2.MostrarListaLibros()
        CR2.MenuTrabajo()
      elif self.Opcion == "3":
        CR2.MenuVenta()
      elif self.Opcion == "4":
        exit()
      else:
        CR2.MenuTrabajo()


    def MenuVenta(self):

      m.MVenta()
      self.Opcion = CR2.ElejirOpcion()

      if self.Opcion == "1":
        v.ingresarCLI()
        CR2.CarritoVenta()
        CR2.MenuVenta()
      elif self.Opcion == "2":
        m.ListaVenta()
        v.ImprimirListaVentas()
        CR2.MenuVenta()
      elif self.Opcion == "3":
        m.MTrabajo()
      elif self.Opcion == "4":
        exit()
      else:
        CR2.MenuVenta()


CR2 = ControlRespuestas2()
CR2.InicioPrograma()
