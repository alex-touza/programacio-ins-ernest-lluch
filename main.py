from audiovisual import Audiovisual, AudiovisualTipus
from menu import Menu
from formularis import Decisio, pausar, Opcio, quant
from colorama import init

from text import Colors

init()


class MenuPrincipal(Menu):
	def __init__(self):
		self.cataleg: list[Audiovisual] = [
			Audiovisual("Catch Me If You Can", 1, AudiovisualTipus.PELICULA),
			Audiovisual("3%", 2, AudiovisualTipus.SERIE),
			Audiovisual("Rasputin - Boney M.", 3, AudiovisualTipus.MUSICA),
			Audiovisual("Sail Over Seven Seas - Gina T.", 3, AudiovisualTipus.MUSICA),
			Audiovisual("Who Killed Captain Alex?", 4, AudiovisualTipus.PELICULA),
			Audiovisual("Once Upon a Time in Uganda?", 5, AudiovisualTipus.PELICULA),
			Audiovisual("Salvation", 6, AudiovisualTipus.SERIE),
			Audiovisual("State Anthem of the Soviet Union", 7, AudiovisualTipus.MUSICA),
		]
		self._ordenar_cataleg()
		super().__init__("Metflix", enrere="Sortir")

	def _mostrar_taula(self, llista: list[Audiovisual]) -> None:
		if len(llista) > 0:
			maxw = max([len(p.titol) for p in llista]) + 2
			print(f"{'ID':<4}{'TÍTOL':<{maxw}}{'TIPUS':>12}")
			for p in llista:
				id = '#' + (str(p.id)).rjust(2, '0')
				print(p.tipus.color(f"{id:<4}{p.titol:<{maxw}}{p.tipus.repr:>12}"))

		print(Colors.gris(quant(len(llista), "element", "elements")))

	def _ordenar_cataleg(self):
		self.cataleg.sort(key=lambda x: x.titol)

	@Menu.menu()
	def __call__(self):
		pass

	@Menu.eina("Mostrar tot el catàleg", 0)
	def mostrar_cataleg(self):
		self._mostrar_taula(self.cataleg)
		pausar(nova_linia=True)

	@Menu.eina("Mostrar el catàleg per tipus", 1)
	def filtrar_cataleg(self):
		ind = Opcio("Escull un tipus d'audiovisual", {tipus.repr_pl.capitalize(): None for tipus in AudiovisualTipus}, sep=None, refrescar=False)()

		if ind == 0: return

		tipus = list(AudiovisualTipus)[ind - 1]

		print()
		self._mostrar_taula([c for c in self.cataleg if c.tipus == tipus])

		pausar(True)

	@Menu.eina("Marcar continguts com a vists/no vists", 2)
	def marcar_vist(self):
		pass

	@Menu.eina("Mostrar continguts vists", 3)
	def mostrar_vist(self):
		pass

	@Menu.eina("Crear llista de reproducció", 4)
	def crear_llista(self):
		pass

	@Menu.eina("Mostrar llista de reproducció", 5)
	def mostrar_llista(self):
		pass

menu = MenuPrincipal()

while True:
	menu()