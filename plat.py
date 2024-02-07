from dataclasses import dataclass, field
from typing import Optional
from formularis import Text

@dataclass
class Plat:
  nom: str
  preu: int
  veg: bool = False

  quantitat: int = 1

  def __str__(self):
    return ("(V) " if self.veg else "") + f"{self.nom} - {self.preu/100:.2f}€"

  def total(self):
    return self.preu * self.quantitat