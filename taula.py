from enum import Enum
from administrador import Administrador
from formularis import Decisio, Nombre, Opcio, Pausar, Text, clear, titol
from text import Estils
from copy import deepcopy
from plat import Plat
from carta import Carta


class Estat(Enum):
	Lliure = "lliure"
	Ocupada = "ocupada"
	Reservada = "reservada"


class Taula(Administrador):

	def __init__(self, id: int, _carta: Carta) -> None:
		self.id = id
		self.plats: list[Plat] = []
		
		
		self.carta = _carta

		self.estat = Estat.Lliure

		super().__init__(f"Taula #{self.id}")

		self.nom: str | None = None
		self.telefon: str | None = None
		
		self.pers: int = 0

	def __str__(self) -> str:
		return f"Taula #{self.id} ({self.estat.value}" + (")" if self.nom is None else f" - {self.pers} pers. - {self.nom})")

	@Administrador.menu(clau=lambda self: self.estat, descr=lambda self: self.estat.value.capitalize() + ("" if self.pers == 0 else f" ({self.pers} pers.)"))
	def __call__(self) -> None:
		pass

	@Administrador.eina("Veure comanda", 2, Estat.Ocupada)	
	def _comanda(self):
		self._mostrar()
		Pausar()
	
	@Administrador.eina("Pagar", 3, Estat.Ocupada)
	def _pagar(self):
		self._mostrar()
		if len(self.plats) == 0:
			Pausar()
		elif Decisio(None, refrescar=False, si="Pagar", no="Cancel·lar")():
			self.estat = Estat.Lliure
			self.nom = None
			self.telefon = None
			self.pers = 0
			print()
			print("Comanda pagada.")
			Pausar()
		
	
	@Administrador.eina("Nova comanda", 1, Estat.Ocupada, "Escriu un plat per línia i deixa'n una buida per acabar.")
	def _demanar(self) -> None:
		plat = Opcio(None, self.carta.dict(), enrere="Acabar", sep=None, refrescar=False)()
		
		while True:
			if plat == 0:
				self._mostrar()
				Pausar()
				break
			else:
				self._afegir(self.carta[plat - 1])
			plat = Opcio(None, self.carta.dict(), mostrar=False, sep=None, refrescar=False)()

	def _afegir(self, plat):
		if self.plats.count(plat) == 0:
			self.plats.append(deepcopy(plat))
		else:
			self.plats[self.plats.index(plat)].quantitat += 1

	@Administrador.eina("Reservar", 1, Estat.Lliure)
	def _reservar(self) -> None:
		self.nom = Text("Nom", buit=True)()
		if self.nom == "":
			self.nom = None
			return
		self.telefon = Text("Telèfon (opcional)", lambda t, le: 7 <= le <= 15, buit=True)()
		if self.telefon == "":
			self.telefon = None

		p = Nombre("N. de persones", lambda n: 1 <= n <= 10, buit=True)()
		if p is None:
			self.nom = None
			self.telefon = None
			return
		self.pers = p
		self.estat = Estat.Reservada

	@Administrador.eina("Cancel·lar reserva", 3, Estat.Reservada)
	def _cancelar_reserva(self):
		if Decisio(None, si="Confirmar", no="Enrere", descr="Segur que vols cancel·lar la reserva?", sep=None)():
			self.estat = Estat.Lliure
			self.nom = None
			self.telefon = None
			self.pers = 0

	def _treure(self) -> None:
		pass

	@Administrador.eina("Informació", (2, 4), (Estat.Reservada, Estat.Ocupada))
	def _info(self) -> None:
		if self.nom is not None:
			print(f"Nom:      {self.nom}")
		if self.telefon is not None:
			print(f"Telèfon:  {self.telefon}")
		if self.pers is not None:
			print(f"N. pers:  {self.pers}")
		Pausar()
		pass


	@Administrador.eina("Ocupar", (2, 3), (Estat.Lliure, Estat.Reservada))
	def _ocupar(self) -> None:
		if self.estat is Estat.Lliure:
			self.nom = Text("Nom", buit=True)()
			if self.nom == "":
				self.nom = None
				return
			p = Nombre("N. de persones", lambda n: 1 <= n <= 10)()
			if p is None:
				self.nom = None
				return
			self.pers = p
		self.estat = Estat.Ocupada


	def __int__(self):
		return sum(plat.total() for plat in self.plats)

	def _mostrar(self) -> None:
		if len(self.plats) == 0:
			print("La comanda és buida.")
			return
			
		print("Comanda:")
		for plat in self.plats:
			print(f"  {plat.nom} - {plat.preu / 100:.2f}€/plat - {plat.quantitat} plat{'' if plat.quantitat == 1 else 's'} - {plat.total() / 100:.2f}€")
		
		print()
		
		total = round(int(self) / 100, 2)
		print(f"Total: {Estils.brillant(total)}€")
		print(f"Persones: {self.pers}")
		
		preu_pers = round(int(self) / self.pers / 100, 2)
		print(f"Preu per persona: {Estils.brillant(preu_pers)}€")
		print()
		print(f"Nom: {self.nom}")
		if self.telefon is not None:
			print(f"Telèfon:  {self.telefon}")

	