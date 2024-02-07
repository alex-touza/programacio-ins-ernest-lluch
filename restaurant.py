from administrador import Administrador
from carta import Carta
from taula import Taula, Estat
from formularis import Opcio, Pausar, titol, clear, Nombre, Decisio
from collections import Counter

from text import Colors


class Restaurant(Administrador):
	def __init__(self, carta: Carta, n_taules=3) -> None:
		self.carta = carta
		self.taules = [Taula(i, carta) for i in range(1, n_taules+1)]

		super().__init__("Taules")

	def __call__(self):
		Opcio(str(self), {str(t): t for t in self.taules} | {
			"Administrar taules": self._admin_taules,
			"Administrar carta": self.carta
		}, enrere=None, args=None)()

	def _comptar_taules(self):
		return {"total": int(self)} | dict(Counter([t.estat for t in self.taules]))

	def veure_taules(self):
		etiquetes = {
			"total": "Taules: ",
			Estat.Lliure: "Taules lliures: ",
			Estat.Ocupada: "Taules ocupades: ",
			Estat.Reservada: "Taules reservades: "
		}
		compte = self._comptar_taules()

		print('\n    '.join([l + str(compte.get(e, 0)) for e, l in etiquetes.items()]))

	@Administrador.menu()
	def _admin_taules(self):
		self.veure_taules()

	@Administrador.eina("Afegir taules", 1)
	def _afegir(self):
		n = Nombre("Introdueix el nombre de taules", comprovar=lambda m: m >= 0, buit=True)()
		if n is not None:
			self.taules.extend([Taula(i + 1, self.carta) for i in range(int(self), int(self) + n)])

	@Administrador.eina("Treure una taula", 2, descr="Es treurà la taula lliure amb l'identificador més alt.")
	def _treure(self):
		if not Decisio(None, si="D'acord", no="Enrere", refrescar=False, sep=None)():
			return

		i = -1
		for j, t in enumerate(self.taules[::-1]):
			if t.estat is Estat.Lliure:
				i = int(self) - j - 1
				break
				
		if i == -1:
			print(Colors.error("Error: No hi ha cap taula lliure."))
			Pausar()
		else:
			self.taules.pop(i)

	def __int__(self):
		return len(self.taules)

	def __str__(self):
		return "Restaurant"
