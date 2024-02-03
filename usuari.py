from llibre import Llibre

class Usuari:
	def __init__(self, nom: str, cognom: str, id: int) -> None:
		self.nom = nom
		self.cognom = cognom
		self.id = id
		self.prestecs: list[int] = []
		self.reserves: list[int] = []

	def __call__(self):
		pass