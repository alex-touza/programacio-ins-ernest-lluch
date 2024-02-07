from cataleg import Cataleg
from id import ID
from menu import Menu
from pelicula import Pelicula, Genere
from coleccions import Coleccio

class Videoclub(Menu):
	def __init__(self, cataleg: Cataleg):
		self.cataleg = cataleg
		self.coleccions = Coleccions(cataleg)
		
		super().__init__("Videoclub", enrere="Sortir")

	@Menu.menu(descr=lambda self: str(self))
	def __call__(self):
		pass
	
	@Menu.eina("Catàleg", 1, func_clau='cataleg')
	def admin_catàleg(self):
		pass
	
	@Menu.eina("Col·leccions", 2, func_clau='coleccions')
	def admin_coleccions(self):
		pass
	
	def __str__(self) -> str:
		return str(self.cataleg) + '\n' + str(self.coleccions)

pelicules_id = ID()

cataleg = Cataleg([Pelicula("Interstellar", "Christopher Nolan", Genere.CienciaFiccio, 2014)], pelicules_id)

