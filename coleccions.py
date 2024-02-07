from cataleg import Cataleg
from coleccio import Coleccio
from menu import Menu


class Coleccions(Menu):
	def __init__(self, cataleg: Cataleg):
		self.cataleg = cataleg

		self.llista: list[Coleccio] = []
		
		super().__init__("Col·leccions", enrere="Sortir")

	@Menu.menu(descr=lambda self: str(self))
	def __call__(self):
		pass

	@Menu.eines_dinamiques
	def coleccions(self):
		return {str(c): c for c in self.llista}

	def __iter__(self):
		return iter(self.llista)

	def __len__(self):
		return len(self.llista)

	def __str__(self) -> str:
		return "1 col·lecció" if len(self.llista) == 1 else f"{len(self.llista)} col·leccions"