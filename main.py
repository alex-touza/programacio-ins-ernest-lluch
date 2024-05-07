from audiovisual import Audiovisual, AudiovisualTipus
from menu import Menu
from formularis import Decisio, pausar, Opcio
from colorama import init

init()


class MenuPrincipal(Menu):
	def __init__(self):
		self.cataleg: list[Audiovisual] = [
			Audiovisual("Atrapa'm si pots", 0, AudiovisualTipus.PELICULA),
			Audiovisual("3%", 1, AudiovisualTipus.SERIE),
			Audiovisual("Rasputin - Boney M.", 2, AudiovisualTipus.MUSICA)
		]
		super().__init__("Metflix", enrere="Sortir")

	@Menu.menu()
	def __call__(self):
		pass

	@Menu.eina("Mostrar tot el catàleg", 0)
	def mostrarCataleg(self):
		print(f"{'TÍTOL':<30}{'TIPUS':>12}")
		for p in self.cataleg:
			print(f"{p.titol:<30}{p.tipus.repr:>12}")

		pausar(nova_linia=True)

	@Menu.eina("Mostrar el catàleg per tipus", 1)
	def filtrarCataleg(self):
		tipus = Opcio("Escull un tipus d'audiovisual", {tipus.repr_pl.capitalize(): None for tipus in AudiovisualTipus})()

		print(list(AudiovisualTipus)[tipus])

	@Menu.eina("Marcar continguts com a vists/no vists", 2)
	def marcarVist(self):
		pass

	@Menu.eina("Mostrar continguts vists", 3)
	def mostrarVist(self):
		pass

	@Menu.eina("Crear llista de reproducció", 4)
	def crearLlista(self):
		pass

	@Menu.eina("Mostrar llista de reproducció", 5)
	def mostrarLlista(self):
		pass

menu = MenuPrincipal()

while True:
	menu()