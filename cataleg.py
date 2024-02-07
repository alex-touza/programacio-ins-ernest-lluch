from admin_llibre import AdminLlibre
from formularis import ColeccioFormularis, Decisio, Nombre, Text, pausar, titol
from id import ID
from llibre import Llibre, Estat
from menu import Menu
from typing import Callable
from dataclasses import dataclass


class Cataleg(Menu):
	@staticmethod
	def encapcalament():
		print(f"{'ID':^4} {'TÍTOL':^35} {'AUTOR':^25} {'ANY':^4} {'ESTAT':^15}")

	def __init__(self, llibres: list[Llibre], ids: ID):
		self.llibres = llibres
		self.ids = ids

		# Assignar IDs als llibres etiquetats com a perduts
		for l in self.llibres:
			if l.estat is Estat.Perdut:
				l.assignar_id(ids)

		super().__init__("Catàleg")

	@Menu.menu(descr=lambda self: str(self))
	def __call__(self):
		pass

	@Menu.eina("Mostrar catàleg", 1)
	def mostrar_catàleg(self):
		if len(self) == 0:
			print("No hi ha cap llibre.")
		else:
			self.llibres.sort(key=lambda l: l.id)
			self.encapcalament()
			for l in self:
				print(l.taula())

		print()
		admin = self._admin_llibre()
		if admin is not None:
			admin()

	@Menu.eina("Cercar llibre", 2, cond=lambda self: len(self) > 0)
	def cercar_llibre(self):
		q = Text("Cerca per títol o autor", buit=True)()
		print()
		if q is not None:
			titol("Cercar llibre - Resultats", True)
			print(f'Cercant "{q}"...')
			print()


			# Obtenir els llibres que coincideixin amb la cerca
			r_titol: list[Llibre] = [
					l
					for l in self
					if q.lower() in l.titol.lower()
				]
			r_titol.sort(key=lambda t: t.id)

			r_autor: list[Llibre] = [
					l
					for l in self
					if q.lower() in l.autor.lower()
				]
			r_autor.sort(key=lambda t: t.id)

			print("Cerca per títol:")
			if len(r_titol) == 0:
				print("No s'ha trobat cap llibre.")
			else:
				for l in r_titol:
					print(l)
			
			print()
	
			print("Cerca per autor:")
			if len(r_autor) == 0:
				print("No s'ha trobat cap llibre.")
			else:
				for l in r_autor:
					print(l)
			print()

			if len(r_titol) == 0 and len(r_autor) == 0:
				pausar()
			else:
				admin = self._admin_llibre(lambda n: n in [l.id for l in r_titol] or n in [l.id for l in r_autor],
												 "L'ID no és als resultats.")
				if admin is not None:
					admin()


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

	@Menu.eina("Esborrar llibre", 4, cond=lambda self: len(self) > 0)
	def esborrar_llibre(self):
		if self._admin_llibre(cridar_met='esborrar') is not None:
			self.esborrar_llibre()


	# Demanar un ID a l'usuari per administrar el llibre corresponent
	def _admin_llibre(self,
									comprovar: Callable[[int], bool] = lambda n: True,
									error_compr: str = "Valor invàlid.", cridar_met: str | None = None):
		n = Nombre("Introdueix l'ID d'un llibre (deixa buit per acabar)",
							 sufix=": #",
							 comprovar1=lambda n: self.ids.existeix(n),
							 error_compr1="L'ID no existeix.",
							 comprovar2=comprovar,
							 error_compr2=error_compr,
							 buit=True)()
		if n is not None:
			admin = AdminLlibre(n, self.llibres, self.ids)
			
			if cridar_met is not None:
				getattr(admin, cridar_met)()

			return admin
		

	def __repr__(self) -> str:
		return str([l.taula() for l in self.llibres])

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