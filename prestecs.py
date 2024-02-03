from cataleg import Cataleg
from menu import Menu
from usuaris import Usuaris
from dataclasses import dataclass
from usuari import Usuari
from llibre import Llibre
from formularis import pausar

@dataclass
class Prestec:
	usuari: Usuari
	llibre: Llibre


class Prestecs(Menu):
	def __init__(self, ref_usuaris: Usuaris, ref_cataleg: Cataleg):
		self.usuaris = ref_usuaris
		self.cataleg = ref_cataleg
		self.llista: list[Prestec] = []

		super().__init__("Préstecs")

	@Menu.menu()
	def __call__(self):
		pass

	@Menu.eina("Mostrar préstecs", 1)
	def mostrar_prestecs(self):
		if len(self) == 0:
			print("No hi ha cap préstec.")
		else:
			for p in self:
				print(p)

		pausar(nova_linia=True)

	@Menu.eina("Nou préstec", 2)
	def nou_prestec(self):
		pass

	def __len__(self):
		return len(self.llista)

	def __iter__(self):
		return iter(self.llista)

	def __str__(self) -> str:
		p = len(self)
		return (f"{p} préstecs" if p > 1 else "1 préstec") if p else "Cap préstec"