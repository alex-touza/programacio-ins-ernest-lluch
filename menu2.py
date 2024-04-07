from collections.abc import Callable
from typing import ClassVar, Generic, TypeVar
from formularis import Opcio, titol
from functools import wraps

T = TypeVar('T')  # Argument per cridar la funció per obtenir el titol
U = TypeVar('U')  # Tipus de la clau per mostrar les opcions. Pot ser un enum.

def menu(titol: str | Callable[[T], str], arg: T | None = None, clau: Callable | None = None, descr: str | Callable[..., str] | None = None, enrere: str | None = "Enrere"):
	def wrapper(cls):
		cls_init = cls.__init__
		class Menu:
			def __init__(self, titol: str | Callable[[T], str], arg: T | None = None, clau: Callable | None = None, descr: str | Callable[..., str] | None = None, enrere: str | None = "Enrere") -> None:
				self._titol = titol
				self.titol_arg = arg
				self.enrere = enrere

				self.clau = clau
				self.descr = descr

				self._sortir = False

		def __init__(self, *args, **kwargs):
			self.__menu__ = Menu(titol, arg, clau, descr, enrere)

			cls_init(self, *args, **kwargs)

		cls.__init__ = __init__
		return cls
	

class Menu(Generic[T, U]):
	def __init__(self, titol: str | Callable[[T], str], arg: T | None = None, enrere: str | None = "Enrere") -> None:
		self._titol = titol
		self.titol_arg = arg
		self.enrere = enrere

		# Quan és True, l'administrador es tancarà encara que
		# no s'esculli "Enrere"
		self._sortir = False