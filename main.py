from fitxer import Fitxer, Modes
from formularis import Decisio, Opcio, mentre, Text, pausar
from menu import Menu
from text import Estils, Colors
from random import randint
from re import fullmatch

class MenuPrincipal(Menu):

	def __init__(self):
		self.fitxers = {
				"noms": Fitxer("Noms", "noms.txt"),
				"cognoms": Fitxer("Cognoms", "cognoms.txt")
		}

		self.usuaris: dict[str, Fitxer] = {}

		super().__init__("Generador de noms aleatoris", enrere="Sortir")

	@Menu.menu()
	def __call__(self):
		pass

	@Menu.eina("Mostrar cadenes", 1)
	def mostrar_cadenes(self):
		for fitxer in self.fitxers.values():
			print(Estils.brillant(fitxer.title))
			if fitxer.exists():
				fitxer.read()

				if fitxer.isEmpty():
					print(Colors.groc("El fitxer és buit."))
				else:
					assert fitxer.content is not None
					for line in fitxer.content:
						print(f'\t{line}')
			else:
				print(Colors.groc("El fitxer no existeix."))

			print()

		pausar()

	@Menu.eina("Afegir noms", 2)
	def afegir_noms(self):
		noms = mentre(Text("Introdueix un nom", buit=True))

		if len(noms) > 0:
			self.fitxers["noms"].read().iter_write(noms)

	@Menu.eina("Afegir cognoms", 3)
	def afegir_cognoms(self):
		cognoms = mentre(Text("Introdueix un nom", buit=True))

		if len(cognoms) > 0:
			self.fitxers["cognoms"].read().iter_write(cognoms)

	@Menu.eina("Generar nom aleatori", 4)
	def generar(self):

		acabar = False
		nom_generat = ""

		while not acabar:
			print("Nom generat:")
			
			nom_generat = ' '.join(
					fitxer.read().content[randint(0,
																				len(fitxer.content) - 1)]
					for fitxer in self.fitxers.values())
			
			print('\t' + Colors.verd(nom_generat))
			print()
			op = Opcio(None, {"Generar-ne un altre": None, "Desar": None}, refrescar=False, enrere="Enrere")()
			if op == 0: return
			else: acabar = op == 2
			print()

		dni = Text("Introdueix el teu DNI", lambda s, le: fullmatch(r'^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$', s) != None)()
		assert dni is not None
		fitxer = self.usuaris.get(dni, None)

		try:
			if fitxer is None:
				fitxer = Fitxer(dni)
				self.usuaris[dni] = fitxer

			if fitxer.exists(): fitxer.read()
				
			fitxer.begin(Modes.Append)
			fitxer.iter_write([nom_generat])
			
			fitxer.end()
		except Exception as e:
			Colors.error()
			print("Error en desar el nom.")
			Colors.reset()
			pausar(nova_linia=True)
		else:
			print(Colors.verd("S'ha escrit el fitxer correctament."))
			print()
			print("Contingut del fitxer:")
			print(''.join(['\n\t' + l for l in fitxer.read().content]))
			pausar(nova_linia=True)
		
			
		

m = MenuPrincipal()

while m():
	pass
