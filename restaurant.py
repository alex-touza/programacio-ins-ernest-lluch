from carta import Carta
from taula import Taula, Estat
from formularis import Opcio, Pausar, titol, clear
from collections import Counter


class Restaurant(Opcio):
	def __init__(self, carta: Carta, n_taules=3) -> None:
		self.menu = carta
		self.taules = [Taula(i, carta) for i in range(1, n_taules+1)]
		self.n = n_taules
		super().__init__(str(self), {str(t): t for t in self.taules} | {
			"Administrar taules": self._administrar_taules,
			"Veure carta": lambda: carta.mostrar(True)
		}, enrere=None)

	def __int__(self):
		return self.n

	def __str__(self):
		return f"Restaurant - {self.n} taules"

	def _comptar_taules(self):
		return {"total": self.n} | dict(Counter([t.estat for t in self.taules]))

	def _administrar_taules(self):
		titol("Administrador de taules", True)
		etiquetes = {
			"total": "Taules: ",
			Estat.Lliure: "Taules lliures: ",
			Estat.Ocupada: "Taules ocupades: ",
			Estat.Reservada: "Taules reservades: "
		}
		compte = self._comptar_taules()

		print('\n\t'.join([l + str(compte.get(e, 0)) for e, l in etiquetes.items()]))
		Pausar()
		#Opcio("", {"Afegir taules": self})

	def _ampliar(self, n=1):
		self.taules.extend([Taula(i, self.menu) for i in range(self.n, self.n + n + 1)])
		self.n += n

	def _esborrar(self, i=1):
		assert i > 0 and i <= self.n
		self.taules.pop(i - 1)
		self.n -= 1
