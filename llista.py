from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from types import NoneType

from audiovisual import Audiovisual, LLISTA_IDS_LLARGADA, mostrar_taula, EXTENSIO
from fitxer import Fitxer
from formularis import quant
from text import Estils


class Llista:
	class Modes(Enum):
		ESCRIPTURA = auto()
		LECTURA = auto()

	class Vista:
		"""Vista prèvia d'una llista que conté el nom i el nombre d'elements."""
		nom: str
		n: int

		def __init__(self, ruta: str) -> None:
			self.ruta = ruta
			self.nom = ruta[:-len(EXTENSIO)]
			self.n = Fitxer(self.nom, ruta).get_line_count(LLISTA_IDS_LLARGADA + 1)

		def __len__(self):
			return self.n

		def __str__(self):
			return f"{self.nom} ({quant(self.n, 'element', 'elements')})"

		def obtenir_llista(self, cataleg: list[Audiovisual]):
			return Llista(self.nom, Llista.Modes.LECTURA, cataleg)

	@staticmethod
	def veure_llistes(self) -> list[Llista.Vista]:
		pass

	def __len__(self):
		return len(self.elements)

	def __init__(self, nom: str, mode: Llista.Modes, cataleg: list[Audiovisual] | None = None):
		self._nom = nom
		self.fitxer = Fitxer(self.nom, self.nom + EXTENSIO)

		self.mode = mode
		self.elements: list[Audiovisual] = [] if mode is Llista.Modes.ESCRIPTURA else [
			[p for p in cataleg if p.id == int(id)][0] for id in self.fitxer.read().content
		]

	def desar(self):
		if self.mode == Llista.Modes.LECTURA: raise TypeError

		if self.fitxer.exists():
			raise FileExistsError

		self.fitxer.iter_write([str(p.id).rjust(LLISTA_IDS_LLARGADA, '0') for p in self.elements])

	def mostrar(self):
		print(Estils.brillant(self.nom))
		mostrar_taula(self.elements)

	@property
	def nom(self):
		return self._nom

	@nom.setter
	def nom(self, value: str):
		self._nom = value
		self.fitxer = Fitxer(self.nom, self.nom + EXTENSIO)
