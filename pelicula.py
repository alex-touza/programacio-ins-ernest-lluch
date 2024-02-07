from enum import Enum
from id import ID

class Genere(Enum):
	Drama = "drama"
	CienciaFiccio = "ciència-ficció"
	Acció = "acció"
	Aventura = "aventura"
	Terror = "terror"
	Comedia = "comèdia"
	Fantasia = "fantasia"

# Si el paràmetre és un generador d'IDs, crida'l, si no,
# assigna'l.
def obtenir_id(id: int | ID) -> int:
	return id() if isinstance(id, ID) else id

class Pelicula:
	def __init__(self, titol: str, director: str, genere: Genere, any: int, id: int | ID | None = None) -> None:
		self.titol = titol
		self.director = director
		self.genere = genere
		self.any = any

		if id is None:
			self.id = -1
		else:
			self.id = obtenir_id(id)

	def __str__(self) -> str:
		return f"#{'??' if self.id == -1 else self.id} {self.titol} ({self.any} - {self.genere.value}) de {self.director}"