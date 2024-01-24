from enum import Enum
from formularis import Opcio, Pausar, Text, clear, titol
from menu import Carta
from plat import Plat


class Estat(Enum):
  Lliure = "lliure"
  Ocupada = "ocupada"
  Reservada = "reservada"


class Taula:

  def __init__(self, id: int, carta: Carta) -> None:
    self.id = id
    self.plats: list[Plat] = []
    self.carta = carta

    self.estat = Estat.Lliure

    self.nom: str | None = None
    self.telefon: str | None = None

  def __str__(self) -> str:
    return f"Taula {self.id} ({self.estat.value}" + (")" if self.nom is  None else ")")

  def __call__(self) -> None:
    if Opcio(f"Taula #{self.id} ({self.estat.value})",
        {
            "Afegir plats": lambda self: self._afegir(),
            "Veure comanda": lambda self: self._comanda(),
            "Pagar": lambda self: self._pagar()
        } if self.estat is Estat.Ocupada else
        ({
            "Cancel·lar reserva": lambda self: self._reservar(False),
            "Informació": lambda self: self._info(),
            "Ocupar": lambda self: self._ocupar()
        } if self.estat is Estat.Reservada else {
            "Reservar": lambda self: self._reservar(True),
            "Ocupar": lambda self: self._ocupar()
            # Passem self a les funcions perquè aquestes tinguin accés
            # a la instància de la taula.
        }),
        self)() != 0:
      self()

  def _afegir(self) -> None:
    plat = self.carta()
    if (plat == 0): self._mostrar()
    else:
      self.plats.append(self.carta[plat - 1])
      self._afegir()

  def _reservar(self, estat: bool) -> None:
    titol(f"Reservar taula #{self.id}")
    if (estat):
      self.estat = Estat.Reservada
      self.nom = Text("Nom")()
      self.telefon = Text("Telèfon", lambda t, le: 7 <= le <= 15, buit=True)()
      clear()
    else:
      self.estat = Estat.Lliure
      self.nom = None
      self.telefon = None

  def _treure(self) -> None:
    pass

  def _info(self) -> None:
    if self.nom is not None:
      print(f"Nom:\t{self.nom}")
    if self.telefon is not None:
      print(f"Telèfon:\t{self.telefon}")
    Pausar()()
    pass

  def _pagar(self) -> None:
    pass

  def _ocupar(self) -> None:
    if self.estat is Estat.Lliure:
      titol(f"Ocupar taula #{self.id}")
      self.nom = Text("Nom")()
      clear()

    self.estat = Estat.Ocupada

  def _comanda(self) -> None:
    pass

  def _total(self):
    return sum(plat.preu for plat in self.plats)

  def _mostrar(self) -> None:
    print("Comanda:")
    for plat in self.plats:
      print(f"  {plat.nom} - {plat.preu/100:.2f}€")

    print(f"Total: {self._total()}€")
