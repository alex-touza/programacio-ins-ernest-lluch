from collections.abc import Callable
from typing import Any, Optional
from menu import Carta
from plat import Plat
from taula import Taula
from formularis import Opcio

class Estats(Enum):
  Lliure = "lliure"
  Ocupada = "ocupada"
  Reservada = "reservada"
  
# Taula actual
t = 0

def main():
  menu = Carta([
      Plat("Espaguetis", 800, True),
      Plat("Arròs", 650, True),
      Plat("Pizza", 1000, False),
      Plat("Amanida", 500, True),
      Plat("Bistec", 1250, False)
  ])
  
  taules = [Taula(i, menu) for i in range(1, 4)]
  print("Benvingut al nostre restaurant!")
  print(f"Tenim {len(taules)} taules disponibles.")
  print()
  
  menu.mostrar()
  print()

  
  while True:
    opcions = {str(t): t for t in taules} | {"Menú": lambda: menu.mostrar(True)}
  
    Opcio(str(, opcions, args=None, enrere=None)()
    
    


if __name__ == "__main__":
  main()
