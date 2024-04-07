from formularis import Decisio, GrupFormularis, Nombre, Text, pausar, quant
from menu import Menu
from fitxer import Fitxer, Modes
from text import Colors, Estils, catch
from re import fullmatch
from dataclasses import dataclass, asdict

@dataclass
class Usuari:
	nom: str
	cognom1: str
	cognom2: str
	dni: str
	edat: int

	@property
	def csv(self):
		return ','.join([self.nom, self.cognom1, self.cognom2, self.dni, str(self.edat)])


	@property
	def data(self):
		return asdict(self).items()

	def mostrar(self, columnes):
		for i, (k, v) in enumerate(self.data, 0):
			print((columnes[i]).ljust(10), Colors.blau(v.rjust(25)))

class MenuPrincipal(Menu):
	def __init__(self, nom_fitxer: str):
		self.fitxer = Fitxer(nom_fitxer, f"{nom_fitxer.lower()}.csv")

		self.columnes = {"Nom": 20, "Cognom 1": 20, "Cognom 2": 20, "DNI": 12, "Edat": 5}

		self.dni_form = Text("DNI", lambda s, le: fullmatch(r'^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$', s) != None, buit=True)

		super().__init__("Altura de dades")

	def _llegir(self) -> list[list] | None:
		csv = self.fitxer.csv_read()
		if isinstance(csv, bool):
			print(Colors.groc("El fitxer no existeix o està buit."))
			pausar(nova_linia=True)
			return None

		return csv

	def _escriure(self, s):
		if catch(lambda: self.fitxer.read().iter_write([s]), "Error en escriure les dades."):
			print(Colors.verd("S'han escrit les dades correctament."))

	def _obtenir_usuari(self, csv: list[list]) -> tuple[Usuari, int] | None:
		dni = self.dni_form()

		usuari: Usuari | None = None
		index: int = -1

		for i, u_data in enumerate(csv):
			u = Usuari(*u_data)

			if dni == u.dni:
				usuari = u
				index = i
				break

		if usuari is None:
			print(Colors.groc("No s'ha trobat l'usuari."))
			return None
		else:
			print(Colors.verd("S'ha trobat l'usuari."))
			return usuari, index

	def _afegir_capcaleres(self):
		print("Afegint capçaleres...")

		if not catch(lambda: self.fitxer.write(','.join(self.columnes.keys())), "Error en afegir les capçaleres."):
			pausar()
			return

		print(Colors.verd("Capçaleres afegides."))
	
	@Menu.menu(descr="L'administrador de dades amb el joc de paraules matemàtic més penós de la història.")
	def __call__(self):
		pass

	@Menu.eina("Crear usuari", 1)
	def crear_usuari(self):
		dnis = []
		if self.fitxer.exists():
			csv = self.fitxer.csv_read()
			if csv:
				dnis = [u[list(self.columnes.keys()).index("DNI")] for u in csv]
				
		else:
			print(Colors.groc("El fitxer no existeix. Es crearà 'dades.csv'."))
			self._afegir_capcaleres()
			print()

		usuari: None | Usuari = None

		

		while usuari is None:
	
			form = GrupFormularis({
				"nom": Text("Nom", lambda s, le: le < 20, buit=True),
				"cognom1": Text("Cognom 1", lambda s, le: le < 20, buit=True),
				"cognom2": Text("Cognom 2 (pot ser buit)", lambda s, le: le < 20, buit=True),
				"DNI": self.dni_form,
				"Edat": Nombre("Edat", lambda n: 0 < n < 120, buit=True)
			}, True, [2])()
	
			if form is None:
				return
	
			usuari = Usuari(*form.values())

			if usuari.dni in dnis:
				print()
				print(Colors.error("Error: Ja existeix un usuari amb aquest DNI"))
				
				usuari = None

				op = input("Prem enter per tornar a provar, 0 per acabar")

				if op == "0":
					return

				print()

		

		

		print()
		self._escriure(usuari.csv)

		pausar()
		return

	@Menu.eina("Consultar usuari", 2)
	def consultar_usuari(self):
		csv = self._llegir()
		if not csv:
			return

		usuari: None | Usuari = None

		while usuari is None:

			dni = self.dni_form()

			if dni == "":
				return

			for u_data in csv:
				u = Usuari(*u_data)
				if u.dni == dni:
					usuari = u
					break

			print()
			if usuari is None:
				print(Colors.groc("No s'ha trobat l'usuari."))
				print()
			else:
				usuari.mostrar(list(self.columnes.keys()))

		pausar(nova_linia=True)

	@Menu.eina("Esborrar usuari", 3)
	def esborrar_usuari(self):
		csv = self._llegir()
		if not csv:
			return

		usuari_ind: None | int = None
		usuari: None | Usuari = None

		while usuari_ind is None:

			dni = self.dni_form()
			print()

			if dni == "":
				return

			new_csv = []

			for i, u_data in enumerate(csv, 1):
				u = Usuari(*u_data)
				if u.dni == dni:
					usuari_ind = i
					usuari = u
				else:
					new_csv.append(u.csv)
					
			if usuari_ind is None:
				print(Colors.groc("No s'ha trobat l'usuari."))
				print()
				
			else:
				assert usuari is not None
				
				print(Colors.verd("S'ha trobat l'usuari."))
				print()
				usuari.mostrar(list(self.columnes.keys()))

				def esborrar():
					self.fitxer.begin(Modes.Write)
					self._afegir_capcaleres()
					self.fitxer.end().read().begin(Modes.Write).iter_write(new_csv).end()
					
				print()
				
				if Decisio("Segur que el vols esborrar?", False, "Esborrar", "Enrere")() and catch(esborrar, "Error en escriure el fitxer."):
					print(Colors.verd("S'ha escrit el fitxer correctament."))
					pausar(nova_linia=True)

				
			

	@Menu.eina("Consultar tots els usuaris", 4)
	def consultar_tot(self):
		csv = self._llegir()
		if not csv:
			return

		csv = [[value.ljust(list(self.columnes.values())[i]) for i, value in enumerate(line)] for line in csv]

		Estils.brillant()
		
		print(quant(len(csv), "usuari", "usuaris"))
		print()

		for title, width in self.columnes.items():
			print(title.center(width),end="")

		print()

		Estils.reset()

		for line in csv:
			print(''.join(line))



		pausar(nova_linia=True)

	@Menu.eina("Reinicialitzar base de dades", 5)
	def reinicialitzar(self):
		if Decisio("Segur que vols esborrar totes les dades?", False, "Reinicialitzar", "Enrere", None)():
				pass
			


m = MenuPrincipal("Dades")

while m():
	pass