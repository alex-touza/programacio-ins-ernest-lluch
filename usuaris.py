from id import ID
from menu import Menu
from usuari import Usuari

class Usuaris(Menu):
	def __init__(self, usuaris: list[Usuari], ids: ID):
		self.usuaris = usuaris
		self.eliminats_n = 0
		self.ids = ids

		super().__init__("Usuaris")

	
	@Menu.menu()
	def __call__(self):
		pass

	@Menu.eina("Mostrar usuaris", 1)
	def mostrar_usuaris(self):
		pass

	@Menu.eina("Afegir usuari", 2)
	def afegir_usuari(self):
		pass

	@Menu.eina("Eliminar usuari", 3)
	def eliminar_usuari(self):
		pass
		# Revisar historial d'accions als llibres i
		# substituir l'ID de l'usuari per -(elimants_n)

	def __len__(self):
		return len(self.usuaris)

	def __iter__(self):
		return iter(self.usuaris)

	def __getitem__(self, n: int) -> Usuari | None:
		for u in self:
			if u.id == n:
				return u
		return None

	def __str__(self) -> str:
		p = len(self)
		return (f"{p} usuaris" if p > 1 else "1 usuari") if p else "Cap usuari"