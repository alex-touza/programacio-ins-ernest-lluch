from formularis import pausar
from menu import Menu

class MenuExemple(Menu):
	def __init__(self):
		super().__init__("Títol")

	@Menu.menu()
	def __call__(self):
		pass

	@Menu.eina("Eina 1", 1)
	def eina1(self):
		pausar()

	@Menu.eina("Eina 2", 2)
	def eina2(self):
		pausar()

	@Menu.eina("Eina 3", 3)
	def eina3(self):
		pausar()

m = MenuExemple()

m()