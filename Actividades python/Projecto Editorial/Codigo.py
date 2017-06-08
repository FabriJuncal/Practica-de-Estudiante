# -*- coding: utf-8 -*-
class Editorial():
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
  
  
       
class libro():
  def __init__(self):
    self.nombrelib=""
    self.valor=""
    self.autor=""
    self.aniopublicacion=""
    self.genero=""
    self.color=""
    self.listalib=[]
    self.lislisLIB=[]
    self.lisLIBven=[]
    self.comprobanteLIB=[]
    self.comprobanteLIBtotal = []
    self.valorLIB = []
    self.totalV = 0
    self.ventaLIB = []
    self.listaTOT_V = []
    self.listaAutores = []
    self.lislisAUT = []
    
    return
  
  def ingresarLIB(self):
    print('\n'"""    Ingrese los datos del libro
  --------------------------------""")
    self.nombrelib=raw_input('\n'"Nombre: ")
    self.valor=raw_input("Precio: ")
    l.ingresarAUT() 
    self.aniopublicacion=raw_input("Año de publicacion: ")
    self.genero=raw_input("Género: ")
    self.color=raw_input("Color de portada: ")
   
    return
  def ingresarAUT(self):
      self.autor = raw_input("Autor: ")
      self.listaAutores.append(self.autor)     
      m.pregunta7()
      return
    
  def guardarLIB(self):
    self.lislisAUT.append(self.listaAutores)
    self.listalib = [self.nombrelib,self.valor,self.lislisAUT,self.aniopublicacion,self.genero,self.color]
    self.lislisLIB.append(self.listalib)
    self.listaAutores = []
    self.lislisAUT = []
    print('\n'"      **** El registro se a guardado con exito ****")
  
  def limpiarAUT(self):
    self.listaAutores = []
    self.lislisAUT = []
    return
    
  def imprimirLIB(self):

    print('\n'"Nombre: " + self.listalib[0])
    print("Precio: " + self.listalib[1] + "$")
    
    if len(self.listalib[2]) > 1:
      for i in range(len(self.listalib[2])):
        print("Autores: ")
        print("      " + str(i) + ")" + self.listalib[2][i])
        i = int(i)
    else:
      print("Autor: " + self.listalib[2][0])
           
    print("Autor: " + self.listalib[2])
    print("Año de publicacion: " + self.listalib[3])
    print("Género: " + self.listalib[4])
    print("Color de portada: " + self.listalib[5])
    
    return
  
  def imprimir_LS_LIB(self):
    print('\n'"""    Lista de Libros
----------------------------""")
    if len(self.lislisLIB) == 0:
      print('\n'"      **** No hay libros registrados ****"'\n')
      m.MTrabajo()  
      
    for i in range(len(self.lislisLIB)):
      print('\n' + str(i+1) + ") " + self.lislisLIB[i][0])
    print('\n'"""

 1) Ver datos de un libro.
 2) Volver al menu de trabajo.
 3) Salir.
 """)
    p = m.pregunta()  
    if p == "1":
      l.buscarLIB()        
    elif p == "2":
      m.MTrabajo()      
    elif p == "3":
      exit()
    else:
      l.imprimir_LS_LIB()
      
  def imprimir_carrito_LIB(self):
    
    print('\n'"     Libros en el carrito    (Escriba FIN para terminar)")
    print("    -----------------------")
    j = 0
    
    while True:          
      VLibro=(raw_input(" "+str(j+1)+") "))
      
      if VLibro=="":
        
        while True:

            VLibro= (raw_input(" "+str(j+1)+") "))
            print("\t"+"|"+"\t")
             
            if VLibro == "fin" or VLibro == "Fin" or VLibro == "FIN" :
              E = e.imprimirEDI()
              C = v.imprimirCLI() 
              self.listaTOT_V.append(self.totalV)
              self.ventaLIB = [self.lisLIBven,self.valorLIB]
              self.comprobanteLIB = [E, C,self.ventaLIB]
              self.comprobanteLIBtotal.append(self.comprobanteLIB)
              l.comprobante_venta()
              
              self.lisLIBven = []
              self.valorLIB = []
              self.totalV = 0
              return
            elif VLibro !="":
                break
      elif VLibro == "fin" or VLibro == "Fin" or VLibro == "FIN" :
        E = e.imprimirEDI()
        C = v.imprimirCLI() 
        self.listaTOT_V.append(self.totalV)
        self.ventaLIB = [self.lisLIBven,self.valorLIB]
        self.comprobanteLIB = [E, C,self.ventaLIB]
        self.comprobanteLIBtotal.append(self.comprobanteLIB)
        l.comprobante_venta()
        
        self.lisLIBven = []
        self.valorLIB = []
        self.totalV = 0
        
        return             
      else:                  
        for i in range(len(self.lislisLIB)):
              
          if VLibro == self.lislisLIB[i][0]:       
            print("\t" + "|"+"\t" + self.lislisLIB[i][1]+ "$")
            self.valorLIB.append(self.lislisLIB[i][1])
            self.totalV = int(self.totalV) + int(self.lislisLIB[i][1])     
            print"----------------------------------"   
            print("TOTAL: " + "\t" + "|"+"\t" + str(self.totalV) + "$") 
            self.lisLIBven.append(VLibro)
          
                    
          elif len(self.lislisLIB) == len(self.lislisLIB) and VLibro != self.lislisLIB[i][0]:  
            print("\t" + "|"+"\t" + "*NO EXISTE*")                  
            print"----------------------------------"   
            print("TOTAL: " + "\t" + "|"+"\t" + str(self.totalV) + "$")  
            j=int(j)-1
    
      j=int(j)+1 
  
  def totalventa(self,Nventa):
    j = Nventa
    print('\n''\n'"  Total de la venta: " + str(self.listaTOT_V[j]) + "$"'\n')
  
  def comprobante_venta(self):
    v.listaventas(self.comprobanteLIBtotal)
    
  
  def buscarLIB(self):
    nombre_libro= raw_input("  Nombre del libro: ")
    for i in range(len(self.lislisLIB)):
      if nombre_libro == self.lislisLIB[i][0]:
       
        nombrelib=self.lislisLIB[i][0]
        valor=self.lislisLIB[i][1]
        aniopublicacion=self.lislisLIB[i][3]
        genero=self.lislisLIB[i][4]
        color=self.lislisLIB[i][5]

        print('\n'"Nombre: " + nombrelib)
        print("Precio: " + valor + "$")
        if len(self.lislisLIB[i][2][0]) > 1:
          print("Autores: ")
          for j in range(len(self.lislisLIB[i][2][0])):
            
            print("      " + str(j+1) + ")" + self.lislisLIB[i][2][0][j])
            j = int(j)
        else:
          print("Autor: " + self.lislisLIB[i][2][0][0])
          
        print("Año de publicacion: " + aniopublicacion)
        print("Género: " + genero)
        print("Color de portada: " + color)
        
        m.pregunta6()
        
    if (len(self.lislisLIB)) == (len(self.lislisLIB)) and nombre_libro != self.lislisLIB[i][0]:
      print('\n'"  *** No existe ese nombre en el registro de libros ***")
      m.pregunta6()
    
    return
    
  
class venta():
  def __init__(self):
    self.cliente=""
    self.valortotal=""
    self.fecha=""
    self.venta = []
    self.ventas=[]
    self.lista_ventas=[]
    
  def ingresarCLI(self):
    self.cliente = raw_input('\n'" Ingresar nombre del cliente: ")   
    return
  
  def imprimirCLI(self):
    return(self.cliente)
  
   
  def imprimirTOT(self):    
    print('\n''\n'"El total es " + self.valortotal)    
    return 
  
  
  def listaventas(self,listaventas):
    self.ventas = listaventas
    self.lista_ventas.append(self.ventas)
    
    
  def imprimir_LS_venta(self):
    print('\n''\n'u"""     **********************
         LISTA DE VENTAS
     **********************""")
    if len(self.lista_ventas) == 0:
      print('\n'" **** No se ha realizado ninguna venta ****"'\n')
      m.MVenta()
      
    for j in range(len(self.lista_ventas)):
      print('\n'"  " + str(j+1) + ")")
      j=int(j)
      print("  Editorial: " + self.lista_ventas[0][j][0][0] ) 
      print("  Localidad: " + self.lista_ventas[0][j][0][1])
      print("  Cliente: " + self.lista_ventas[0][j][1])
      print("  Libros que compro: ")
      if len(self.lista_ventas) == 0:
        print("   *** No se vendio libros ***")
      else:
        
        for i in (range(len(self.lista_ventas[0][j][2][0]))):         
          print('\t''\t'"     " + str(i+1) + ") ")
          i=int(i)      
          print('\t''\t'"      " + str(self.lista_ventas[0][j][2][0][i]) + " " + str(self.lista_ventas[0][j][2][1][i] + "$") )
          print('\t''\t'"    --------------------------------")
          i=int(i)
          
        
        l.totalventa(j)
        
        print("**********************************************************")
        
        
        
class menu():
  
  def __init__(self):
    self.lis_ventas = []
  
  def MInicio(self):
    print('\n''\n'u"""     **********************
         MENU DE INICIO
     **********************

 1)Ingresar nombre de la editorial y su localidad.
 2)Salir.""")
      
    a=m.pregunta()
        
    if a == "1":            
      e.ingresarEDI()
      m.MTrabajo()
    elif a== "2":
      exit()
    else:
      m.MInicio()
        
  def MTrabajo(self):
    
    print('\n''\n'u"""     ***********************
         MENU DE TRABAJO
     ***********************

 1)Registrar libro/os.
 2)Mostrar lista de libros.
 3)Menu de venta.
 4)Salir.""")
          
    a = m.pregunta()
        
    if a == "1":     
      l.ingresarLIB()
      m.pregunta5()
      m.pregunta2()
    elif a == "2": 
      l.imprimir_LS_LIB() 
    elif a == "3":
      m.MVenta()
    elif a == "4":
      exit()
    else:
      m.MTrabajo()
    
    
  def MVenta(self):
    print('\n''\n'u"""    *****************
      MENU DE VENTA
    *****************
    1) Vender.
    2) Ver lista de ventas.
    3) Volver al menu de trabajo.
    4) Salir""")

    a=m.pregunta()
    
    
    if a == "1":     
      v.ingresarCLI()
      l.imprimir_carrito_LIB()
      
      #v.imprimir_LS_VEN()
      m.MVenta()           
    elif a == "2":
      
      v.imprimir_LS_venta()
      m.MVenta()
    elif a == "3":
      m.MTrabajo()
    elif a == "4":
      exit() 
    else:
      m.MVenta()
      
      
  def pregunta(self):
    a = raw_input('\n'"  Elija una opcion con los numeros: ")
    return (a)
  
  def pregunta2(self):
    print('\n''\n'"""    *************************************************
               ¿Desea registrar otro libro?
    *************************************************"""'\n''\n')

    m.pregunta4()
    
  def pregunta3(self):
    p=raw_input('\n''\t''\t''\t'"Si o No? "'\n''\t''\t''\t'  )
    return(p)


  def pregunta4(self):
    p=m.pregunta3()
    if p== "si" or p=="Si" or p=="SI":
        l.ingresarLIB()
        m.pregunta5()
        m.pregunta2()
    elif p== "no" or p=="No" or p=="NO":
        m.MTrabajo()        
    else:
        if p!= "si" and p!= "no":
            while True:
                p=m.pregunta3()
                if p== "si" or p== "Si" or p== "SI":
                    l.ingresarLIB()
                    m.pregunta5()
                    m.pregunta2()
                elif p== "no" or p== "No" or p== "NO":    
                    m.MTrabajo()
        
  def pregunta5(self):
    p= raw_input('\n''\t'"     ¿Guardar Registro del Libro?"'\n''\t''\t''\t')
    
    if p== "si" or p=="Si" or p=="SI":
      l.guardarLIB()
      return
    elif p== "no" or p=="No" or p=="NO":
      l.limpiarAUT()
      return        
    else:
        if p!= "si" and p!= "no":
          while True:
            p=m.pregunta3()
            if p== "si" or p== "Si" or p== "SI":
              l.guardarLIB()
              return
            elif p== "no" or p== "No" or p== "NO":    
              l.limpiarAUT()
              return
          
  def pregunta6(self):
    p = raw_input('\n''\t''\t'"¿Desea volver a buscar?"'\n''\t''\t''\t')
    if p== "si" or p=="Si" or p=="SI":
      l.buscarLIB()
    elif p== "no" or p=="No" or p=="NO":
        m.MTrabajo()        
    else:
        if p!= "si" and p!= "no":
            while True:
                p=m.pregunta3()
                if p== "si" or p== "Si" or p== "SI":
                    l.buscarLIB()
                elif p== "no" or p== "No" or p== "NO":    
                    m.MTrabajo()
  
  def pregunta7(self):
    p = raw_input(" Ingresar otro Autor?"'\n''\t')
    if p == "si" or p == "Si" or p == "SI":
      l.ingresarAUT()
    elif p == "no" or p == "No" or p == "NO":
      return
    else:
      m.pregunta7()
      return
    
  
e = Editorial()
l = libro()
v = venta()
m = menu()

m.MInicio()



  
  
  
  
  
  
  
  
  
  
  
  
 

     
      

 
 
 
    
    
    
