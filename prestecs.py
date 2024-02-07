from cataleg import Cataleg
from menu import Menu
from llibre import Llibre, Estat
from formularis import pausar


class Prestecs(Menu):
	def __init__(self, cataleg: Cataleg):
		self.cataleg = cataleg
		self.llista: list[Llibre] = []

		super().__init__("Préstecs")

	def _actualitzar(self):
		self.llista = [l for l in self.cataleg if l.estat is Estat.EnPrestec]
		
	@Menu.menu(descr=lambda self: str(self))
	def __call__(self):
		pass

	@Menu.eina("Mostrar préstecs", 1)
	def mostrar_prestecs(self):
		self._actualitzar()
		if len(self) == 0:
			print("No hi ha cap préstec.")
		else:
			for p in self:
				print(p.taula())

		pausar(nova_linia=True)

	@Menu.eina("Nou préstec", 2)
	def nou_prestec(self):
		if self.cataleg._admin_llibre(cridar_met='prestec') is not None:
			self.nou_prestec()

	@Menu.eina("Retornar llibre", 3, cond=lambda self: len(self) > 0)
	def retornar_llibre(self):
		if self.cataleg._admin_llibre(cridar_met='retornar') is not None:
			self.retornar_llibre()
		
	def __len__(self):
		return len(self.llista)

	def __iter__(self):
		return iter(self.llista)

	def __str__(self) -> str:
		self._actualitzar()
		p = len(self)
		return (f"{p} préstecs" if p > 1 else "1 préstec") if p else "Cap préstec"