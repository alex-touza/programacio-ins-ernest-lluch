from enum import Enum

from text import Colors, Modificador


class AudiovisualTipus(Enum):
	PELICULA = (1, ("pel·lícula", "pel·lícules"), Colors.blau)
	SERIE = (2, ("sèrie", "sèries"), Colors.groc)
	MUSICA = (3, ("música", "música"), Colors.magenta)

	def __init__(self, id: int, name: tuple[str, str], color: Modificador) -> None:
		self.id = id
		self._name = name
		self.repr_pl = self._name[1]
		self.repr = self._name[0]
		self.color = color


class Audiovisual:
	def __init__(self, titol: str, id: int, tipus: AudiovisualTipus, vist: bool = False) -> None:
		self.titol = titol
		self.id = id
		self.tipus = tipus
		self.vist = vist

	# def marcarVist(self):
	# 	self.vist = not self.vist
