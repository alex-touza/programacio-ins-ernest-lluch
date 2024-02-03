from admin_llibre import AdminLlibre
from formularis import ColeccioFormularis, Decisio, Nombre, Text, pausar, titol
from id import ID
from llibre import Llibre
from menu import Menu
from typing import Callable
from usuari import Usuari
from usuaris import Usuaris
from dataclasses import dataclass


class Cataleg(Menu):

	def __init__(self, llibres: list[Llibre], ids: ID, ref_usuaris):
		self.llibres = llibres
		self.ids = ids
		self.ref_usuaris = ref_usuaris

		super().__init__("Catàleg")

	@Menu.menu()
	def __call__(self):
		pass

	@Menu.eina("Mostrar catàleg", 1)
	def mostrar_catàleg(self):
		if len(self) == 0:
			print("No hi ha cap llibre.")
		else:
			self.llibres.sort(key=lambda l: l.id)
			for l in self:
				print(l)

		print()
		self._demanar_id()

	@Menu.eina("Cercar llibre", 2)
	def cercar_llibre(self):
		q = Text("Cerca per títol o autor", buit=True)()
		print()
		if q is not None:
			titol("Cercar llibre - Resultats", True)
			print(f'Cercant "{q}"...')
			print()

			r: set[tuple[Llibre, int]] = {
					(l, l.id)
					for l in self
					if q.lower() in l.titol.lower() or q.lower() in l.autor.lower()
			}

			if len(r) == 0:
				print("No s'ha trobat cap llibre.")
			else:
				for l, id in r:
					print(l)
			print()

			self._demanar_id(lambda n: n in [l[1] for l in r],
											 "L'ID no és als resultats.")

	@Menu.eina("Afegir llibre", 3)
	def afegir_llibre(self):
		dades = ColeccioFormularis({
				"titol":
				Text("Títol", buit=True),
				"autor":
				Text("Autor", buit=True),
				"any":
				Nombre("Any", lambda n: n < 2025, buit=True)
		})()
		
		if dades is None:
			return
		dades.update({"id": self.ids()})

		llibre = Llibre(**dades)

		print()
		print("S'afegirà el llibre:")
		print(llibre)
		if Decisio(None, refrescar=False, si="Confirmar", no="Enrere")():
			self.llibres.append(llibre)
		else:
			self.ids.eliminar(llibre.id)

	def _demanar_id(self,
									comprovar: Callable[[int], bool] = lambda n: True,
									error_compr: str = "Valor invàlid."):
		n = Nombre("Introdueix l'ID d'un llibre (deixa buit per acabar)",
							 comprovar1=lambda n: self.ids.existeix(n),
							 error_compr1="L'ID no existeix.",
							 comprovar2=comprovar,
							 error_compr2=error_compr,
							 buit=True)()
		if n is not None:
			AdminLlibre(n, self.llibres, self.ids, self.ref_usuaris)()

	def __repr__(self) -> str:
		return str([str(l) for l in self.llibres])

	def __len__(self):
		return len(self.llibres)

	def __iter__(self):
		return iter(self.llibres)

	def __str__(self) -> str:
		p = len(self)
		return (f"{p} llibres" if p > 1 else "1 llibre") if p else "Cap llibre"

	def __getitem__(self, n: int) -> Llibre | None:
		l = [l for l in self.llibres if l.id == n]
		return None if len(l) == 0 else l[0]