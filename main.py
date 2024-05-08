from enum import Enum, auto
from os.path import isfile
from glob import glob

from colorama import init

from audiovisual import Audiovisual, AudiovisualTipus, mostrar_taula, str_vist, str_id, EXTENSIO
from formularis import pausar, Opcio, Nombre, Text, Decisio, titol
from id import ID
from llista import Llista
from menu import Menu
from text import Colors, Estils

init()


class MenuPrincipal(Menu):
	def __init__(self, _ids: ID, cataleg: list[Audiovisual]):
		self.ids = _ids
		self.cataleg = cataleg
		self._ordenar_cataleg()
		super().__init__("Metflix", enrere="Sortir")

	def _ordenar_cataleg(self) -> None:
		self.cataleg.sort(key=lambda x: x.titol)

	def _obtenir_element(self) -> Audiovisual | None:

		id = Nombre("Introdueix un ID (deixa buit per acabar)", lambda n: self.ids.existeix(n), None,
		            "L'ID no existeix.", buit=True)()

		if id is None: return

		r = [p for p in self.cataleg if p.id == id][0]

		return r

	@Menu.menu()
	def __call__(self):
		pass

	@Menu.eina("Mostrar tot el catàleg", 0)
	def mostrar_cataleg(self):
		mostrar_taula(self.cataleg)
		pausar(True)

	@Menu.eina("Mostrar el catàleg per tipus", 1)
	def filtrar_cataleg(self):
		ind = Opcio("Escull un tipus d'audiovisual", {tipus.repr_pl.capitalize(): None for tipus in AudiovisualTipus},
		            sep=None, refrescar=False)()

		if ind == 0: return

		tipus = list(AudiovisualTipus)[ind - 1]

		print()
		mostrar_taula([c for c in self.cataleg if c.tipus == tipus])

		pausar(True)

	@Menu.eina("Marcar continguts com a vists/no vists", 2)
	def marcar_vist(self):
		mostrar_taula(self.cataleg)
		print()

		p = self._obtenir_element()

		if p is None: return

		print()
		print(p)
		print()
		op = Opcio("Marcar com a...", {"vist": None, "no vist": None}, sep=None, refrescar=False, enrere="Enrere")()

		if op == 0: return

		dif = (op == 1) != p.vist

		p.vist = op == 1

		print()
		if dif:
			print(f"S'ha marcat l'element amb ID {Colors.blau(str_id(p.id))} com a {str_vist(p.vist, None)}")
		else:
			print(f"L'element amb ID {Colors.blau(str_id(p.id))} ja estava marcat com a {str_vist(p.vist, None)}")

		pausar(True)

	@Menu.eina("Mostrar continguts vists", 3)
	def mostrar_vist(self):
		mostrar_taula([p for p in self.cataleg if p.vist])
		pausar(True)

	@Menu.eina("Crear llista de reproducció", 4)
	def crear_llista(self):
		class Estat(Enum):
			INICI = (1, "")
			MENU = (2, "")
			NOM = (3, "Canviar el nom")
			AFEGIR = (4, "Veure/afegir elements")
			DESAR = (5, "Desar la llista")

			def __init__(self, id: int, nom: str):
				self.id = id
				self.nom = nom

		estat_opcions = [e for e in Estat if e.nom != ""]

		estat: Estat = Estat.INICI

		llista = Llista("", Llista.Modes.ESCRIPTURA)

		primer = True

		while estat is not Estat.DESAR:
			prev_estat = estat.value

			match estat:
				case Estat.INICI | Estat.NOM:

					if (nom := Text("Nom de la llista", buit=True)()) != "":
						if isfile(nom + EXTENSIO):
							print()
							print(Colors.vermell("Una llista amb aquest nom ja existeix."))
							print()

							continue

						else:
							llista.nom = nom

					elif estat is Estat.INICI:
						return

					if estat is Estat.INICI:
						titol(f"Crear llista de reproducció - {llista.nom}", True)
						estat = Estat.AFEGIR
					else:
						estat = Estat.MENU

				case Estat.AFEGIR:
					if primer:
						print(Estils.brillant("Catàleg"))
						mostrar_taula(self.cataleg)
						print()

					if len(llista) > 0:
						llista.mostrar()
						print()

					p = self._obtenir_element()

					if p is None:
						if len(llista) == 0: return

						estat = Estat.MENU
					else:
						if p in llista.elements:
							print()
							print(Colors.groc("Aquest element ja està a la llista."))

						else:
							llista.elements.append(p)

					print()

				case Estat.MENU:
					op = Opcio(f"Crear llista de reproducció - {llista.nom}", {e.nom: None for e in estat_opcions})()
					if op == 0: return

					print()

					estat = estat_opcions[op - 1]

			primer = prev_estat != estat.value

		llista.desar()

		print(Colors.verd(f"S'ha desat la llista com a \"{llista.nom}{EXTENSIO}\" correctament."))
		pausar(True)

	@Menu.eina("Mostrar llistes de reproducció", 5)
	def mostrar_llista(self):
		llistes = [Llista.Vista(p) for p in glob("*" + EXTENSIO)]

		op = Opcio("Escull una llista", {str(v): None for v in llistes}, sep=None, refrescar=False)()
		if op == 0: return

		print()

		llistes[op - 1].obtenir_llista(self.cataleg).mostrar()


		pausar(True)



ids = ID()
menu = MenuPrincipal(ids, [
	Audiovisual("Catch Me If You Can", ids(), AudiovisualTipus.PELICULA),
	Audiovisual("3%", ids(), AudiovisualTipus.SERIE),
	Audiovisual("Rasputin - Boney M.", ids(), AudiovisualTipus.MUSICA),
	Audiovisual("Sail Over Seven Seas - Gina T.", ids(), AudiovisualTipus.MUSICA),
	Audiovisual("Who Killed Captain Alex?", ids(), AudiovisualTipus.PELICULA),
	Audiovisual("Once Upon a Time in Uganda?", ids(), AudiovisualTipus.PELICULA),
	Audiovisual("Salvation", ids(), AudiovisualTipus.SERIE),
	Audiovisual("State Anthem of the Soviet Union", ids(), AudiovisualTipus.MUSICA),
])

while True:
	menu()
