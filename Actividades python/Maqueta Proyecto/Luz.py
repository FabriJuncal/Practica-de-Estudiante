class Luz():
  """docstring for luz"""
  def __init__(self, id):
      self.id = id
    
  
  def prender(self):
    radio.send(self.id, 1);
      
    
    
  def apagar(self):
    radio.send(self.id, 0);
   
    