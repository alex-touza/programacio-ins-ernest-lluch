from enum import Enum


class AudiovisualTipus(Enum):
	PELICULA = (1,( "pel·lícula", "pel·lícules"))
	SERIE = (2, ("sèrie", "sèries"))
	MUSICA = (3, ("música", "música"))

	def __init__(self, id: int, name: tuple[str, str]) -> None:
		self.id = id
		self._name = name
		self.repr_pl = self._name[1]
		self.repr = self._name[0]
		

class Audiovisual:
	def __init__(self, titol: str, id: int, tipus: AudiovisualTipus, vist: bool = False) -> None:
		self.titol = titol
		self.id = id
		self.tipus = tipus
		self.vist = vist

	def marcarVist(self):
		self.vist = not self.vist