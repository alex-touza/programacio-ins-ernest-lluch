from id import ID
from pelicula import Pelicula

class Coleccio:
	def __init__(self, nom: str, descr: str, llista_init: list[Pelicula], id: int | None, ids: ID):
		self.nom = nom
		self.descr = descr
		self.llista: list[Pelicula] = []
		self.id = ids() if id is None else id
		self.ids = ids

	def afegir(self, pelicula: Pelicula) -> None:
		self.llista.append(pelicula)

	def eliminar(self, id: int) -> None:
		for p in self:
			if p.id == id:
				self.llista.remove(p)
				self.ids.eliminar(id)
				return
				
		raise ValueError(f"No s'ha trobat la pel·lícula amb ID {id}")
		
	def __add__(self, other):
		return Coleccio(self.nom + " / " + other.nom, self.descr, self.llista + [other], self.ids(), self.ids)

	def __str__(self) -> str:
		return f"#{self.id} {self.nom} ({'1 pel·lícula' if len(self.llista) == 1 else f'{len(self.llista)} películ·les'})"

	def __len__(self) -> int:
		return len(self.llista)

	def __iter__(self):
		return iter(self.llista)