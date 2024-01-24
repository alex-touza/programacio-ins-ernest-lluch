from collections.abc import Callable
from typing import Any, Optional
from carta import Carta
from plat import Plat
from taula import Taula
from formularis import Opcio
from restaurant import Restaurant



# Taula actual
t = 0

def main():
  carta = Carta([
    Plat("Espaguetis", 800, True),
    Plat("Arròs", 650, True),
    Plat("Pizza", 1000, False),
    Plat("Amanida", 500, True),
    Plat("Bistec", 1250, False)
  ])
  restaurant = Restaurant(carta)


  while True:
    restaurant()




if __name__ == "__main__":
  main()
