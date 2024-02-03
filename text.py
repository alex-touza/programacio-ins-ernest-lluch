from typing import Any, overload
from colorama import Fore, Style


class Modificador:

	def __init__(self, c: str):
		self.c = c

	def __str__(self):
		return self.c

	@overload
	def __call__(self, text: str) -> str:
		pass

	@overload
	def __call__(self, text:None=None) -> None:
		pass

	def __call__(self, text: str | None=None) -> str | None:
		if text is None:
			print(self.c, end="")
			return
		else:
			return self.c + str(text) + Style.RESET_ALL

	# Afegim funcions màgiques de suma perquè actuïn com a strings
	def __add__(self, other):
		return str(self) + other

	def __radd__(self, other):
		return other + str(self)


class Colors:
	opcions = Modificador(Fore.BLUE)
	entrada = Modificador(Fore.YELLOW)

	gris = Modificador(Fore.LIGHTBLACK_EX)
	
	error = Modificador(Fore.RED)
	
	reset = Modificador(Fore.RESET)


class Estils:
	brillant = Modificador(Style.BRIGHT)
	fosc = Modificador(Style.DIM)


def taula(dades: dict[str, Any]):
	for i, (k, v) in enumerate(dades.items()):

		print(Colors.gris(f"{k:<15}") + f"{v:>20}")
