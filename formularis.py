from collections.abc import Callable
from typing import TypeVar
from os import system, name

T = TypeVar('T')


def clear():

  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')


def titol(text):
  print(text)
  print("----------------")


class Opcio:
  """
  Crea un formulari amb opcions, reutilitzable simplement cridant una instància.
  
  """

  def __init__(self,
               titol: str,
               opcions,
               args=None,
               enrere: str | None = "Enrere",
               refrescar=True,
               sep="----------------"):
    """
    - opcions: Diccionari de les opcions, on les claus són els noms de les opcions i els valors són les funcions associades. El tipus no està anotat per la seva complexitat.
      valors, les funcions que s'executen quan es selecciona la opció. Allò que retornin és ignorat.
    - args: L'argument amb el qual es cridaran les funcions.
    """
    self.titol = titol
    self.opcions = opcions
    self.args = args
    self.enrere = enrere
    self.refrescar = refrescar
    self.sep = sep

  # Retorna l'índex de l'opció escollida.
  def __call__(self) -> int:
    print(self.titol)
    if self.sep:
      print(self.sep)
    if self.enrere is not None:
      print(f"0. {self.enrere}")

    for i, opcio in enumerate(self.opcions.keys(), 1):
      print(f"{i}. {opcio}")

    op = input()
    if self.refrescar:
      clear()
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
      print("Opció invàlida.")
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
    - comprovar: Funció que ha de retornar un booleà indicant si el text introduït és vàlid. El primer argument és el text i el segon la llargada.
    """
    self.missatge = missatge
    self.sufix = sufix
    self.comprovar = comprovar
    self.buit = buit

  def __call__(self) -> str:
    text = input(self.missatge + self.sufix)
    invalid = None

    if (self.buit and text == ""):
      invalid = False
    else:
      invalid = not self.comprovar(text, len(text))

    if invalid:
      print("Text invàlid.")
      return self()
    return text


class Pausar(Opcio):

  def __init__(self):
    super().__init__("", {}, sep="")


class Decisio(Opcio):

  def __init__(self,
               titol: str,
               refrescar=True,
               si="Sí",
               no="No",
               sep="----------------"):
    super().__init__(titol, {t: None
                             for t in [si, no]}, None, None, refrescar, sep)

  def __call__(self) -> bool:
    return super()() == 1
    