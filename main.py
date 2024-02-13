from cataleg import Cataleg
from id import ID
from menu import Menu
from pelicula import Pelicula, Genere
from coleccions import Coleccions
from colorama import init

init()

class Videoclub(Menu):
	def __init__(self, cataleg: Cataleg):
		self.cataleg = cataleg
		self.coleccions = Coleccions(cataleg)
		
		super().__init__("Videoclub", enrere="Sortir")

	@Menu.menu(descr=lambda self: str(self))
	def __call__(self):
		pass
	
	@Menu.eina("Catàleg", 1, func_clau='cataleg')
	def admin_cataleg(self):
		pass
	
	@Menu.eina("Col·leccions", 2, func_clau='coleccions')
	def admin_coleccions(self):
		pass
	
	def __str__(self) -> str:
		return str(self.cataleg) + '\n' + str(self.coleccions)

pelicules_id = ID()

cataleg = Cataleg([
	Pelicula("Interstellar", "Christopher Nolan", Genere.CienciaFiccio, 2014),
	Pelicula("Mr. Nobody", "Pierre Van Dormael", Genere.CienciaFiccio, 2009),
	Pelicula("Cidade de Deus", "Fernando Meirelles, Kátia Lund", Genere.Drama, 2002),
	Pelicula("Faroeste Caboclo", "René Sampaio", Genere.Drama, 2013),
	Pelicula("La Celestina", "Gerardo Vera", Genere.Drama, 1996),
	Pelicula("Oppenheimer", "Christopher Nolan", Genere.Drama, 2023),
	Pelicula("Doctor Strange", "Scott Derrickson", Genere.Accio, 2016),
	Pelicula("The Imitation Game", "Morten Tyldum", Genere.Drama, 2014),
	Pelicula("Back to the Future", "Robert Zemeckis", Genere.CienciaFiccio, 1985),
	Pelicula("As Above, So Below", "John Erick Dowdle", Genere.Terror, 2014),
	Pelicula("Cloud Atlas", "The Wachowskis", Genere.Drama, 2012),
	Pelicula("Matrix", "The Wachowskis", Genere.CienciaFiccio, 1999),
	Pelicula("Contact", "Robert Zemeckis", Genere.CienciaFiccio, 1997),
	Pelicula("Grease", "Randal Kleiser", Genere.Romanc, 1978),
	Pelicula("The Garden of Woods", "Makoto Shinkai", Genere.Romanc, 2013),
	Pelicula("Miracolo a Milano", "Vittorio De Sica", Genere.Fantasia, 1951),
	Pelicula("The Odyssey", "Andrei Konchalovsky", Genere.Aventura, 1997),
	Pelicula("Spy Kids", "Robert Rodriguez", Genere.Aventura, 2001),
	Pelicula("The Physician", "Philipp Stölzl", Genere.Aventura, 2013),
	Pelicula("A.I. Artificial Intelligence", "Steven Spielberg", Genere.CienciaFiccio, 2001),
], pelicules_id)

videoclub = Videoclub(cataleg)
videoclub()