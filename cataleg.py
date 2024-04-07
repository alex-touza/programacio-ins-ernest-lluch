from coleccio import Coleccio
from formularis import GrupFormularis, pausar, quant, Text, Nombre, Decisio
from id import ID
from menu import Menu
from pelicula import Pelicula, Genere
from unidecode import unidecode
from text import Estils

class Cataleg(Menu):
	@staticmethod
	def encapcalament():
		print(Estils.brillant(f"{'ID':^4} {'TÍTOL':^40} {'DIRECTOR':^32} {'GÈNERE':^24} {'ANY':^4}"))

	def __init__(self, pelicules: list[Pelicula], ids: ID) -> None:
		self.pelicules = pelicules
		self.ids = ids

		for p in self:
			if p.id == -1:
				p.id = self.ids()

		super().__init__("Catàleg")

	@Menu.menu(descr=lambda self: str(self))
	def __call__(self):
		pass

	def mostrar(self):
		if len(self) == 0:
			print("Catàleg buit")
		else:
			self.pelicules.sort(key=lambda l: l.id)
			self.encapcalament()
			for l in self:
				print(l.taula())
		

	@Menu.eina("Mostrar catàleg", 1)
	def mostrar_cataleg(self):
		self.mostrar()
		pausar(nova_linia=True)
		
	@Menu.eina("Afegir pel·lícula", 2)
	def afegir_pelicula(self):
		generes = [unidecode(g.value.lower()) for g in Genere]
		
		print("Gèneres disponibles:")
		for g in Genere:
			print(f'\t{g.value.capitalize()}')
		print()

		dades = GrupFormularis({
			"titol": Text("Títol", buit=True),
			"director": Text("Director", buit=True),
			"genere": Text("Gènere", lambda s, le: unidecode(s.lower()) in generes, buit=True),
			"any": Nombre("Any", lambda n: 1900 < n < 2025, buit=True)
		}, opcional=True)()

		if dades is None:
			return

		# Buscar gènere a l'enum
		for g in Genere:
			if unidecode(g.value.lower()) == unidecode(dades["genere"].lower()):
				dades["genere"] = g
				break
		
		dades.update({"id": self.ids()})

		pelicula = Pelicula(**dades)

		print()
		print("S'afegirà la pel·lícula:")
		print(pelicula)
		
		if Decisio(None, refrescar=False, si="Confirmar", no="Enrere")():
			self.pelicules.append(pelicula)
		else:
			self.ids.eliminar(pelicula.id)

	@Menu.eina("Eliminar pel·lícula", 3, cond=lambda self: len(self) > 0)
	def eliminar_pelicula(self):
		self.mostrar()
		print()

		p = self._obtenir_pelicula()
		
		if p is None:
			return

		assert p is not None

		print()
		print("S'eliminarà la pel·lícula:")
		if Decisio(None, False, "Eliminar", "Enrere", None,
			 str(p))():
			self.ids.eliminar(p.id)
			self.pelicules.remove(p)

			print(f"Pel·lícula amb ID #{p.id} esborrada.")
			print()
			pausar()

	def _obtenir_pelicula(self):
		n = Nombre("ID de la pel·lícula",
			 sufix=": #",
			 comprovar1=lambda n: self.ids.existeix(n),
			 error_compr1="L'ID no existeix.",
			 buit=True)()
		if n is not None:
			# Obtenir pel·lícula
			p = None
			for l in self:
				if l.id == n:
					p = l
					break
		
			assert p is not None

			return p
		return None

	def __iter__(self):
		return iter(self.pelicules)

	def __len__(self):
		return len(self.pelicules)

	def __str__(self):
		return quant(len(self), "pel·lícula", "pel·lícules")