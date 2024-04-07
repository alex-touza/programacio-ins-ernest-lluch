from os import remove
from menu import Menu
from formularis import Decisio, Nombre, pausar, titol
from os.path import isfile

from text import Colors

class MenuPrincipal(Menu):
	def __init__(self, titol_fitxer: str):
		self.titol_fitxer = titol_fitxer
		self.n_form = Nombre("Introdueix un nombre de l'1 al 10", lambda n: 1 <= n <= 10, buit=True)
		
		super().__init__("MultipliFitxer", enrere="Sortir")

	@Menu.menu(descr="Aprèn la taula de multiplicar amb l'eina amb el pitjor nom del món.")
	def __call__(self):
		pass

	@Menu.eina("Generar taula", 1)
	def generar_taula(self):
		n = self.n_form()
		if n is None:
			return

		nom = self.titol_fitxer.format(n)
	
		print()
		if isfile(nom):
			print(Colors.groc("El fitxer ja existeix."))
			pausar()
			return
			

		taula = '\n'.join([f"{n} x {i} = {n*i}" for i in range(1, 11)])

		print(taula)
		print()
		
		try:
			with open(nom, 'w') as f:
				f.write(taula)
		except Exception as e:
			Colors.error()
			print("Error en escriure el fitxer.")
			print(e)
			Colors.reset()
			return
		else:
			print(Colors.verd("S'ha escrit el fitxer correctament."))

		pausar(nova_linia=True)

	@Menu.eina("Llegir taula", 2)
	def llegir_taula(self):
		n = self.n_form()
		if n is None:
			return
		
		nom = self.titol_fitxer.format(n)

		if isfile(nom):
			m = self.n_form()
			if m is None:
				pass
			try:
				print()
				with open(nom, 'r') as f:
					for i, line in enumerate(f, 1):
						if i == m:
							print(line)
							break
					else:
						raise LookupError

			except Exception as e:
				Colors.error()
				print("Error en llegir el fitxer.")
				print(e)
				Colors.reset()
				return
			else:
				print(Colors.verd("S'ha llegit el fitxer correctament."))
		else:
			print(Colors.groc("El fitxer no existeix."))
			pausar()
			return
		

		nom = self.titol_fitxer.format(n)


		pausar(nova_linia=True)
		
m = MenuPrincipal("taula-{}.txt")

while m():
	pass