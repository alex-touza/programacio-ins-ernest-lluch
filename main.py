from bustia import Bustia, Paquet
from formularis import Decisio, Text, pausar
from id import UUID
from menu import Menu
from string import ascii_uppercase
from text import Colors


class MenuPrincipal(Menu):
	def __init__(self):
		self.paquets_ids = UUID()
		self.armari: list[Bustia] = [Bustia(id) for id in ascii_uppercase[:10]]
		self.paquets: list[Paquet] = []
		

		super().__init__("ArmariGeddon")

	def _obtenir_bustia(self, id: str):
		return [b for b in self.armari if b.id == id][0]
		
	@Menu.menu(descr="L'armari més astronòmicament eficient de l'univers.")
	def __call__(self):
		pass

	@Menu.eina("Recollir un paquet", 1, cond=lambda self: len(self.paquets) > 0)
	def recollir(self):
		

		if Decisio("Com vols cercar el teu paquet?", False, "Per bústia", "Per UUID del paquet", None)():
			print()
			
			b: Bustia | None = None
	
			while b is None:
				id = Text("ID de la bústia (A-J)", buit=True, default=None)()
				if id is None: return

				if id not in [b.id for b in self.armari]:
					print(Colors.error(f"No s'ha trobat la bústia amb id #{id}"))
					continue
				
				b = self._obtenir_bustia(id)
	
				if b.paquet:
					break
					
				print(Colors.error("La bústia no té cap paquet."))
				b = None
	
			
			print()
			print("Es recollirà el paquet:")
			print(b.paquet)
			if Decisio(None, refrescar=False, si="Confirmar", no="Enrere")():
				p = b.recollirPaquet()
				print()
	
				print("Contingut del paquet:")
				print(p.contingut)
				
				print(Colors.verd("Paquet recollit satisfactòriament."))
				pausar(True)
		else:
			print()

			p = None

			while p is None:
				uuid = Text("Introdueix un UUID de paquet", buit=True, default=None)()

				if uuid is None: return

				if uuid not in [p.uuid for p in self.paquets]:
					print(Colors.error(f"No s'ha trobat el paquet amb UUID {uuid}"))

				p = [p for p in self.paquets if p.uuid == uuid][0]


				print()
				print("Es recollirà el paquet:")
				print(p)
				if Decisio(None, refrescar=False, si="Confirmar", no="Enrere")():
					p.recollir()
					print()

					print("Contingut del paquet:")
					print(p.contingut)

					print(Colors.verd("Paquet recollit satisfactòriament."))
					pausar(True)


			
					
			

	@Menu.eina("Enviar un paquet", 2)
	def enviar(self):
		pid = self.paquets_ids()
		print("UUID del paquet:", pid)
		print()
		
		cont = Text("Contingut del paquet", buit=True, default=None)()
		if cont is None: return

		p = Paquet(pid, cont)

		b: Bustia | None = None

		while b is None:
			id = Text("ID de la bústia (A-J)", buit=True, default=None)()
			if id is None: return

			if id not in [b.id for b in self.armari]:
				print(Colors.error(f"No s'ha trobat la bústia amb id #{id}"))
				continue

			b = self._obtenir_bustia(id)

			if b.paquet:
				print(Colors.error("La bústia ja té un paquet."))
				b = None
			else:
				break
		
		print()
		print("S'enviarà el paquet:")
		print(p)
		print("-->",b)
		if Decisio(None, refrescar=False, si="Confirmar", no="Enrere")():
			
			p.enviar(b)
			
			self.paquets.append(p)
			print()
			print(Colors.verd("Paquet enviat satisfactòriament."))
			pausar(True)

		
	
	@Menu.eina("Llistar bústies", 3)
	def llistar_busties(self):
		for b in self.armari:
			print(b)

		pausar(True)

	@Menu.eina("Buidar la bústia", 4, cond=lambda self: len(self.paquets) > 0)
	def buidar(self):
		if Decisio(f"Segur que vols buidar la bústia?", False, "Buidar", "Enrere", f"Es recolliran els {len(self.paquets)} paquets." if len(self.paquets) > 1 else "Es recollirà el paquet.")():
			paquets = [(b.id, b.recollirPaquet()) for b in self.armari if b.paquet]

			print()
			print("Paquets recollits:")
			for p in paquets:
				print(f"#{p[0]} --> {p[1]}")

			pausar(True)

			self.paquets = []


					


m = MenuPrincipal()

while m():
	pass