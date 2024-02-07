from cataleg import Cataleg
from coleccio import Coleccio
from id import ID
from menu import Menu

class AdminColeccio(Menu):
	def __init__(self, coleccio_id: int, ref_coleccions: list[Coleccio], ids: ID):
		self.coleccio_id = coleccio_id
		self.ref_coleccions = ref_coleccions
		self.ids = ids

		assert self.ids.existeix(self.coleccio_id), "L'ID no existeix"

		self.coleccio = None
		for l in self.ref_coleccions:
			if l.id == self.coleccio_id:
				self.coleccio = l
				break

		assert self.coleccio is not None, "El llibre que es vol administrar no existeix."

		super().__init__("Administrar col·lecció | " + (
				lambda t: t if len(t) <= 25 else (f'{t:.15}...'))(self.coleccio.nom))

	@Menu.menu(descr=lambda self: str(self.coleccio))
	def __call__(self):
		pass

	@Menu.eina("Afegir pel·lícula", 1)
	def afegir_pelicula(self):
		pass
	
	@Menu.eina("Treure pel·lícula", 2, cond=lambda self: len(self.coleccio) > 0)
	def treure_pelicula(self):
		pass

	@Menu.eina("Combinar col·lecció", 3, cond=lambda self: len(self.ref_coleccio) > 0)
	def combinar_coleccio(self):
		pass
