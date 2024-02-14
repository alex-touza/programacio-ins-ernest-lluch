from cataleg import Cataleg
from coleccio import Coleccio
from admin_coleccio import AdminColeccio
from formularis import Decisio, Nombre, Text, quant
from id import ID
from menu import Menu


class Coleccions(Menu):

	def __init__(self, cataleg: Cataleg):
		self.cataleg = cataleg
		self.ids = ID()

		self.llista: list[Coleccio] = []

		super().__init__("Col·leccions", enrere="Sortir")

	@Menu.menu(descr=lambda self: str(self))
	def __call__(self):
		pass

	@Menu.eines_dinamiques
	def coleccions(self):
		return {
				str(c):
				(lambda c:
				 (lambda self: AdminColeccio(c.id, self.llista, self.cataleg, self.ids)
					()))(c)
				for c in self.llista
		}

	@Menu.eina("Nova colecció", 1)
	def nova_coleccio(self):
		nom = Text("Nom", buit=True)()
		if nom == "":
			return

		descr = Text("Descripció (opcional)", buit=True, default=None)()

		print()
		c = Coleccio(nom, descr, None, self.ids)
		self._confirmar_creacio(c)

	@Menu.eina("Combinar col·leccions", 2, cond=lambda self: len(self) > 1)
	def combinar_coleccions(self):
		self._mostrar()
		col_ids: list[int | None | Coleccio] = []

		form = Nombre("ID d'una col·lecció",
									lambda n: self.ids.existeix(n) and n not in col_ids,
									sufix=": #",
									buit=True)

		for i in range(2):
			col_ids.append(form())

			if None in col_ids:
				return

		col: list[Coleccio] = []
		for i, c in enumerate(col_ids):
			for ci in self:
				if ci.id == c:
					col.append(ci)
					break
		print()
		print("Es combinaran les col·leccions:")
		for c in col:
			print(c)

		self._confirmar_creacio(col[0] + col[1], "", "=> ")

	def _confirmar_creacio(self,
												 c,
												 missatge="Es crearà la col·lecció:",
												 prefix=""):

		if missatge != "":
			print(missatge)
		print(prefix + str(c))

		if Decisio(None, refrescar=False, si="Confirmar", no="Enrere")():
			self.llista.append(c)
			AdminColeccio(c.id, self.llista, self.cataleg, self.ids)()
		else:
			self.ids.eliminar(c.id)

	def _mostrar(self):
		for c in self:
			print(f"#{c.id} {c}")

		print()

	def __iter__(self):
		return iter(self.llista)

	def __len__(self):
		return len(self.llista)

	def __str__(self) -> str:
		return quant(len(self), "col·lecció", "col·leccions")
