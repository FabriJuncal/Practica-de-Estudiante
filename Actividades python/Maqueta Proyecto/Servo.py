class Servo():
  """docstring for luz"""
  def __init__(self, id):
      self.id = id
      
  
  def mover(self, grado):
    #radio.send(self.id, grado);
    return(self.id, grado)  
   
  def cerrar(self):
    #radio.send(self.id, 0);
    return(self.id, 0) 
  
  def abrir(self):
    #radio.send(self.id, 180)
    return(self.id, 90)