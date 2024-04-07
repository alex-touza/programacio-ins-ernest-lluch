from os import remove
from menu import Menu
from formularis import Decisio, Nombre, Text, pausar, titol
from os.path import isfile, getsize

from text import Colors

class MenuPrincipal(Menu):
	def __init__(self, titol_fitxer: str):
		self.titol_fitxer = titol_fitxer
		
		super().__init__("Nomificador", enrere="Sortir")

	@Menu.menu(descr="L'eina perfecta per als oblidadors professionals de noms.")
	def __call__(self):
		pass

	@Menu.eina("Mostrar noms", 1, cond=lambda self: isfile(self.titol_fitxer))
	def mostrar_noms(self):
		if getsize(self.titol_fitxer) == 0:
			print(Colors.groc("El fitxer és buit."))
			pausar()
			return
			
		with open(self.titol_fitxer) as file:
			for nom in file:
				print(f'\t{nom}',end="")

		pausar(nova_linia=True)
	
	@Menu.eina("Afegir nom", 2)
	def afegir_nom(self):
		noms = []

		nom_form = Text("Introdueix un nom", buit=True)

		nom = nom_form()
		while nom != "":
			noms.append(nom + '\n')
			
			nom = nom_form()
		
		if len(noms) == 0:
			return

		print("S'escriurà el nom:" if len(noms) == 1 else "S'escriuran els noms:")
		
		for _nom in noms:
			print(f"\t{_nom}", end="")

		if Decisio("", False, "Escriure", "Enrere")():
			print()

			ultLinia = ""
			
			try:
				with open(self.titol_fitxer, 'r') as file:
					linies = file.readlines()
					ultLinia = linies[-1] if len(linies) > 0 else "\n"
										
			except Exception as e:
				Colors.error()
				print("Error en comprovar la cua del fitxer.")
				print(e)
				Colors.reset()
				pausar()
				return
			
			try:
				with open(self.titol_fitxer, 'a') as file:
					if not ultLinia.endswith('\n'):
						file.write('\n')
					file.writelines(noms)
					
			except Exception as e:
				Colors.error()
				print("Error en escriure el fitxer.")
				print(e)
				Colors.reset()
			else:
				print(Colors.verd("S'ha escrit el fitxer correctament."))

			pausar()
			
	@Menu.eina("Esborrar nom", 3, cond=lambda self: isfile(self.titol_fitxer))
	def esborrar_nom(self):
		noms = []
		treure = []

		def _mostrar():
			print("S'eliminarà el nom:" if len(treure) == 1 else "S'eliminaran els noms:")
			for n in treure:
				print(f"\t{n}")

			print()
			if len(noms) == 0:
				print("La llista quedarà buida.")
			else:
				print("Quedarà a la llista:" if len(noms) == 1 else "Quedaran a la llista:")
				for i, nom in enumerate(noms, 1):
					print(f"{i}. {nom}")
			
		
		if getsize(self.titol_fitxer) == 0:
			print(Colors.groc("El fitxer és buit."))
			pausar()
			return

		
		with open(self.titol_fitxer) as file:
			noms = [l.rstrip('\n') for l in file]

		for i, nom in enumerate(noms, 1):
			print(f"{i}. {nom}")

		print()
		print("Deixa buit per acabar.")
		rem_form = Nombre("Introdueix l'índex d'un nom", lambda n: 1 <= n <= len(noms), buit=True)

		nom_ind = rem_form()

		while nom_ind != None:
			treure.append(noms.pop(nom_ind-1))

			print()
			_mostrar()
			print()

			if len(noms) == 0:
				break

			nom_ind = rem_form()
		else:
			print()

		if len(treure) > 0 and Decisio("Vols aplicar els canvis?", False, "Confirmar", "Enrere")():
			print()
			try:
				with open(self.titol_fitxer, 'w') as file:
					file.writelines('\n'.join(noms))
			except Exception as e:
				Colors.error()
				print("Error en escriure el fitxer.")
				print(e)
				Colors.reset()
			else:
				print(Colors.verd("S'ha escrit el fitxer correctament."))

			pausar()

m = MenuPrincipal("noms.txt")

while m():
	pass