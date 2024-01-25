from carta import Carta
from taula import Taula, Estat
from formularis import Opcio, Pausar, titol, clear, Nombre, Decisio
from collections import Counter


class Restaurant(Opcio):
	def __init__(self, carta: Carta, n_taules=3) -> None:
		self.carta = carta
		self.taules = [Taula(i, carta) for i in range(1, n_taules+1)]
		self.n = n_taules

	def __call__(self):
		super().__init__(str(self), {str(t): t for t in self.taules} | {
			"Administrar taules": self._administrar_taules,
			"Veure carta": lambda: self.carta.mostrar(True)
		}, enrere=None)
		return super().__call__()

	def _comptar_taules(self):
		return {"total": self.n} | dict(Counter([t.estat for t in self.taules]))

	def veure_taules(self):
		etiquetes = {
			"total": "Taules: ",
			Estat.Lliure: "Taules lliures: ",
			Estat.Ocupada: "Taules ocupades: ",
			Estat.Reservada: "Taules reservades: "
		}
		compte = self._comptar_taules()

		print('\n    '.join([l + str(compte.get(e, 0)) for e, l in etiquetes.items()]))

	def _administrar_taules(self):
		titol("Administrador de taules", True)
		self.veure_taules()
		op = Opcio(None, {"Afegir taules": lambda self: self._afegir(), "Treure una taula": lambda self: self._treure()}, args=self, sep=None, refrescar=False)()
		if op != 0:
			self._administrar_taules()

	def _afegir(self):
		titol("Afegir taules", True)
		n = Nombre("Introdueix el nombre de taules", comprovar=lambda m: m >= 0, buit=True)()
		if n is not None:
			self.taules.extend([Taula(i, self.carta) for i in range(self.n, self.n + n)])
			self.n += n

	def _treure(self):
		op = Decisio("Treure una taula", descr="Es treurà la taula lliure amb l'identificador més alt.", si="D'acord", no="Enrere")

		i = -1
		for j, t in enumerate(self.taules):
			if t.estat is Estat.Lliure:
				i = j

		if i == -1:
			print("Error: Totes les taules estan ocupades.")
			Pausar()




	def __int__(self):
		return self.n

	def __str__(self):
		return f"Restaurant - {self.n} taules"

	def __dir__(self):
		return {str(t): t for t in self.taules}

