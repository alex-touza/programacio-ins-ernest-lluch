from menu import Carta
from taula import Taula
from formularis import Opcio

class Restaurant(Opcio):
  def __init__(self, carta: Carta, n_taules=3) -> None:
    self.menu = carta
    self.taules = [Taula(i, carta) for i in range(n_taules)]
    self.n = n_taules
    super().__init__(str(self), {str(t): t for t in self.taules} | {"Administrar taules": self, "Veure carta": lambda: carta.mostrar(True)})

  def __int__(self):
    return self.n

  def __str__(self):
    return f"Restaurant - {self.n} taules"

  def ampliar(self, n=1):
    self.taules.extend([Taula(i, self.menu) for i in range(self.n, self.n+n+1)] )
    self.n += n
    
  def esborrar(self, i=1):
    assert i > 0 and i <= self.n
    self.taules.pop(i - 1)
    self.n -= 1


    