from coleccio import Coleccio
from formularis import GrupFormularis, pausar, quant, Text, Nombre, Decisio
from id import ID
from menu import Menu
from pelicula import Pelicula, Genere
from unidecode import unidecode


class Cataleg(Menu):
	@staticmethod
	def encapcalament():
		print(f"{'ID':^4} {'TÍTOL':^25} {'DIRECTOR':^30} {'GÈNERE':^16} {'ANY':^4}")

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

	def _mostrar(self):
		if len(self) == 0:
			print("Catàleg buit")
		else:
			self.pelicules.sort(key=lambda l: l.id)
			self.encapcalament()
			for l in self:
				print(l.taula())
		

	@Menu.eina("Mostrar catàleg", 1)
	def mostrar_cataleg(self):
		self._mostrar()
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
			"genere": Text("Gènere", lambda s, le: unidecode(s.lower()) in generes),
			"any": Nombre("Any", lambda n: n < 2025, buit=True)
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
		self._mostrar()
		print()
		
		n = Nombre("Introdueix l'ID d'una pel·lícula",
							 sufix=": #",
							 comprovar1=lambda n: self.ids.existeix(n),
							 error_compr1="L'ID no existeix.",
							 buit=True)()

		p = self._obtenir_pelicula()
		
		if p is not None:
			# Obtenir pel·lícula
			p = None
			for l in self:
				if l.id == n:
					p = l
					break

			assert p is not None
			
			print()
			print("S'eliminarà la pel·lícula:")
			if Decisio(None, False, "Eliminar", "Enrere", None,
				 str(p))():
				self.ids.eliminar(n)
				self.pelicules.remove(p)
				
				print(f"Pel·lícula amb ID #{n} esborrada.")
				print()
				pausar()

	def _obtenir_pelicula(self):
		n = Nombre("Introdueix l'ID d'una pel·lícula",
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
				
	@Menu.eina("Seleccionar pel·lícula", 0, amagada=False)			
	def seleccionar_pelicula(self, coleccio: Coleccio):
		print(coleccio)
		self._mostrar()

		p = 0

		while p is not None:
			p = self._obtenir_pelicula()

			if p is not None:
				coleccio.llista.append(p)

	
	def __iter__(self):
		return iter(self.pelicules)

	def __len__(self):
		return len(self.pelicules)

	def __str__(self):
		return quant(len(self), "pel·lícula", "pel·lícules")