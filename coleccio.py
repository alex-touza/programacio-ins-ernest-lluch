from formularis import quant
from id import ID
from pelicula import Pelicula


class Coleccio:

  def __init__(self, nom: str | None, descr: str | None, id: int | None, ids: ID, llista_init: list[Pelicula] = []):
    self.descr = descr
    self.llista = llista_init[:]
    self.id = ids() if id is None else id
    self.ids = ids
    self.nom = f"Col·lecció #{self.id}" if nom is None else nom

  def afegir(self, pelicula: Pelicula) -> None:
    self.llista.append(pelicula)

  def eliminar(self, id: int) -> Pelicula:
    for p in self:
      if p.id == id:
        self.llista.remove(p)
        self.ids.eliminar(id)
        return p

    raise ValueError(f"No s'ha trobat la pel·lícula amb ID {id}")

  def inclou(self, pelicula: Pelicula | int):
    for p in self:
      if ((p is pelicula) if isinstance(pelicula, Pelicula) else (p.id == pelicula)):
        return True

    return False


  def __add__(self, other):
    return Coleccio(self.nom + " / " + other.nom, self.descr,
                    self.ids(), self.ids, list(set(self.llista + other.llista)))

  def quant(self) -> str:
    return quant(len(self.llista), 'pel·lícula', 'películ·les')
    
  def __str__(self) -> str:
    return f"{self.nom} ({self.quant()})"

  def __len__(self) -> int:
    return len(self.llista)

  def __iter__(self):
    return iter(self.llista)
