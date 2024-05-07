from collections.abc import Callable
from typing import Any, overload
from colorama import Fore, Style


class Modificador:

	def __init__(self, c: str, r: str = Style.RESET_ALL):
		self.c = c
		self.r = r

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
			return self.c + str(text) + self.r

	# Afegim funcions màgiques de suma perquè actuïn com a strings
	def __add__(self, other):
		return str(self) + other

	def __radd__(self, other):
		return other + str(self)


class Colors:
	entrada = Modificador(Fore.YELLOW, Fore.RESET)

	gris = Modificador(Fore.LIGHTBLACK_EX, Fore.RESET)
	verd = Modificador(Fore.GREEN, Fore.RESET)
	groc = Modificador(Fore.LIGHTYELLOW_EX, Fore.RESET)
	blau = Modificador(Fore.BLUE, Fore.RESET)
	vermell = Modificador(Fore.RED, Fore.RESET)
	magenta = Modificador(Fore.MAGENTA, Fore.RESET)

	reset = Modificador(Fore.RESET, Fore.RESET)



class Estils:
	brillant = Modificador(Style.BRIGHT, Style.NORMAL)
	fosc = Modificador(Style.DIM, Style.NORMAL)

	reset = Modificador(Style.RESET_ALL)


def taula(dades: dict[str, Any]):
	for i, (k, v) in enumerate(dades.items()):

		print(Colors.gris(f"{k:<15}") + f"{v:>20}")

def catch(func: Callable, error_message: str) -> bool:
	def error(e):
		Colors.vermell()
		print(error_message)
		print(e)
		Colors.reset()


	try:
		func()
	except Exception as e:
		error(e)
		return False

	return True

