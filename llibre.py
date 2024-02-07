from enum import Enum
from text import Colors
from id import ID


# Si el paràmetre és un generador d'IDs, crida'l, si no,
# assigna'l.
def obtenir_id(id: int | ID) -> int:
  return id() if isinstance(id, ID) else id


class Estat(Enum):
  EnPrestec = "en préstec"
  Disponible = "disponible"
  Esborrat = "esborrat"
  Perdut = "perdut"  # Quan el llibre no té un ID


class Llibre:

  def __init__(self,
               titol: str,
               autor: str,
               any: int,
               id: int | ID | None = None) -> None:
    self.titol = titol
    self.autor = autor
    self.any = any
    # L'ID pot ser inicialment None per assignar-lo més
    # tard programàticament.
    if id is None:
      self.estat: Estat = Estat.Perdut
      self.id = 0
    else:
      self.estat: Estat = Estat.Disponible

      self.id = obtenir_id(id)

  def __str__(self):
    return f"#{self.id if self.id is not None else '??'} {self.titol} ({self.autor}, {self.any} - {self.estat.value})"

  def taula(self):
    estat = f" {self.estat.value:^15}"
    return f"#{self.id if self.id is not None else '??':<3} {self.titol:<35} {self.autor:<25} {self.any:^4}" + (
        Colors.verd(estat)
        if self.estat is Estat.Disponible else Colors.groc(estat))

  def retornar(self):
    assert self.estat is not Estat.Disponible, "El llibre ja està disponible"
    assert self.estat is not Estat.Perdut, "El llibre no té un ID"

    self.estat = Estat.Disponible

  def assignar_id(self, id: int | ID):
    assert self.estat is Estat.Perdut, "El llibre ja té un ID"

    self.estat = Estat.Disponible
    self.id = obtenir_id(id)

  def prestec(self):
    assert self.estat is not Estat.Perdut, "El llibre no té un ID"
    self.estat = Estat.EnPrestec

  def __dict__(self) -> dict[str, str]:
    return {
        "Títol": self.titol,
        "Autor": self.autor,
        "Any": str(self.any),
        "Estat": self.estat.value
    }
