from __future__ import annotations
from enum import Enum

from formularis import quant
from text import Colors, Modificador

LLISTA_IDS_LLARGADA = 3
EXTENSIO = ".metflix"


def str_id(id: int):
	return '#' + (str(id)).rjust(2, '0')


def str_vist(vist: bool, ljust: int | None = None):
	s = ('vist' if vist else 'no vist')

	if ljust:
		s = s.ljust(ljust)

	return Colors.verd(s) if vist else Colors.groc(s)

def mostrar_taula(llista: list[Audiovisual]) -> None:
	if len(llista) > 0:
		maxw = max([len(p.titol) for p in llista]) + 4
		print(f"{'ID':<4}{'TÍTOL':<{maxw}}{'TIPUS':<12}{'VIST':<8}")
		for p in llista:
			print(
				f"{str_id(p.id):<4}{p.tipus.color(p.titol.ljust(maxw))}{p.tipus.color(p.tipus.repr.ljust(12))}{str_vist(p.vist)}")

	print(Colors.gris(quant(len(llista), "element", "elements")))


class AudiovisualTipus(Enum):
	PELICULA = (1, ("pel·lícula", "pel·lícules"), Colors.blau)
	SERIE = (2, ("sèrie", "sèries"), Colors.cian)
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

	def __str__(self):
		return f"{str_id(self.id)} - " + self.tipus.color(
			f"{self.titol} ({self.tipus.repr})") + f" - {str_vist(self.vist)}"

	# def marcarVist(self):
	# 	self.vist = not self.vist
