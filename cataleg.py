from id import ID
from menu import Menu
from pelicula import Pelicula


class Cataleg:
	def __init__(self, pelicules: list[Pelicula], ids: ID) -> None:
		self.pelicules = pelicules
		self.ids = ids

		for p in self:
			if p.id == -1:
				p.id = self.ids()
		
	def __iter__(self):
		return iter(self.pelicules)