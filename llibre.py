from dataclasses import dataclass
from enum import Enum


class Estat(Enum):
	EnPrestec = "en préstec"
	Disponible = "disponible"
	EnPrestecReservat = "en préstec, reservat"
	Esborrat = "esborrat"

class Accions(Enum):
	Prestec = "préstec"
	PrestecReserva = "préstec amb reserva"
	Reservar = "reservar"
	Tornar = "tornar"
	CancelarReserva = "cancel·lar reserva"


class Llibre:

	def __init__(self, titol: str, autor: str, any: int, id: int) -> None:
		self.titol = titol
		self.autor = autor
		self.any = any
		self.estat: Estat = Estat.Disponible
		self.id = id
		self.usuari_id = -1
		self.reserva_usuari_id = -1

		self.historial: list[tuple[int, Accions]]

		

	def __str__(self):
		return f"#{self.id} {self.titol} ({self.autor}, {self.any} - {self.estat.value})"

	def tornar(self):
		self.en_prestec = False

	def prestec(self):
		self.en_prestec = True

	def __dict__(self) -> dict[str, str]:
		return {
				"Títol": self.titol,
				"Autor": self.autor,
				"Any": str(self.any),
				"Estat": self.estat.value
		}
