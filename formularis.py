from collections.abc import Callable
from typing import TypeVar
from os import system, name

from text import Colors, Estils

T = TypeVar('T')


def clear():
	if name == 'nt':
		system('cls')
	else:
		system('clear')


def titol(text: str, _clear=False):
	if _clear:
		clear()
	print(Estils.brillant(text))
	print("----------------")


class Opcio:
	"""
  Crea un formulari amb opcions, reutilitzable simplement cridant una instància.
  
  """

	def __init__(self,
	             missatge: str | None,
	             opcions,
	             args=None,
	             descr: str | None = None,
	             enrere: str | None = "Enrere",
	             refrescar=True,
               mostrar=True,
	             sep: str | None="----------------"):
		"""
    - opcions: Diccionari de les opcions, on les claus són els noms de les opcions i els valors són les funcions
    associades. Allò que retornin és ignorat. El tipus no està anotat per la seva complexitat.
    - args: L'argument amb el qual es cridaran les funcions.
    """
		self.missatge = missatge
		self.descr = descr
		self.opcions = opcions
		self.args = args
		self.enrere = enrere
		self.refrescar = refrescar
		self.mostrar = mostrar
		self.sep = sep

	# Retorna l'índex de l'opció escollida.
	def __call__(self) -> int:
		if self.refrescar:
			clear()

		if self.missatge is not None:
			print(Estils.brillant(self.missatge))

		if self.sep is not None:
			print(self.sep)

		if self.descr is not None:
			print(self.descr)

		Colors.opcions()

		if self.mostrar:
			if self.enrere is not None:
				print(f"0. {self.enrere}")
			for i, opcio in enumerate(self.opcions.keys(), 1):
				print(f"{i}. {opcio}")
		
		Colors.reset()

		op = input(Colors.entrada)
		Colors.reset()
		if self.enrere is not None and (op == "" or op == "0"):
			return 0
		elif op.isdigit() and int(op) in range(1, len(self.opcions) + 1):
			c = int(op)
			# Executar funció associada a l'opció amb els arguments
			v = list(self.opcions.values())[c - 1]

			if v is not None:
				if self.args is None:
					v()
				else:
					v(self.args)

			return c
		else:
			print(Colors.error("Opció invàlida."))
			# Tornar a escollir. Recursivitat, yay.
			return self()


class Text:

	def __init__(self,
	             missatge: str,
	             comprovar: Callable[[str, int], bool] = (lambda t, le: True),
	             sufix=": ",
	             buit=False):
		"""
    - missatge: Títol del formulari.
    - comprovar: Funció que ha de retornar un booleà indicant si el text introduït
      és vàlid. El primer argument és el text i el segon la llargada.
    - buit: Permet un valor buit com a resposta.
    """
		self.missatge = missatge
		self.sufix = sufix
		self.comprovar = comprovar
		self.buit = buit

	def __call__(self) -> str:
		text = input(("" if self.missatge is None else (self.missatge + self.sufix)) + Colors.entrada)
		Colors.reset()

		valid = (text != "" and self.comprovar(text, len(text))) or (self.buit and text == "")
		# Taula de veritat
		# self.buit    text == ""   self.comprovar     *valid*
		#     0           0              0                0
		#     0           0              1                1
		#     0           1              0                0
		#     0           1              1                0
		#     1           0              0                0
		#     1           0              1                1
		#     1           1              0                1
		#     1           1              1                1
		#

		if not valid:
			print(Colors.error("Text invàlid."))
			return self()
		return text


class Nombre:
	def __init__(self, missatge: str | None = "", comprovar: Callable[[int], bool] = lambda n: True, sufix=": ", buit=False):
		self.buit = buit
		self.sufix = sufix
		self.comprovar = comprovar
		self.missatge = missatge

	def __call__(self) -> int | None:
		n = input(("" if self.missatge is None else (self.missatge + self.sufix)) + Colors.entrada)
		Colors.reset()
		nint: None | int = None

		if n == "" and self.buit:
			return None

		try:
			nint = int(n)
		except Exception:
			pass

		if nint is not None and self.comprovar(nint):
			return nint
		else:
			print(Colors.error("Valor invàlid."))
			return self()


# Una mica estúpid utilitzar una classe així...
class Pausar:
	def __init__(self):
		self.__call__()

	def __call__(self):
		input("\nPrem qualsevol tecla per continuar..." + Colors.entrada)
		Colors.reset()


class Decisio(Opcio):

	def __init__(self,
	             missatge: str | None = "",
	             refrescar=True,
	             si="Sí",
	             no="No",
	             sep: str | None="----------------",
	             descr: str | None = None):
		super().__init__(missatge, {si: None}, None, descr, no, refrescar, sep=sep)

	def __call__(self) -> bool:
		return super().__call__() == 1
