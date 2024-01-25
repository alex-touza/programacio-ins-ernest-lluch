from formularis import Opcio, Pausar, titol
from plat import Plat


class Carta(Opcio):
  """
  Carta és derivat d'Opcio per permetre la selecció de plats.
  """

  def __init__(self, plats: list[Plat]):
    # Ordenar els plats
    self.plats = sorted(plats, key=lambda plat: (-plat.veg, plat.nom))

    # Cridar constructor d'Opcio
    super().__init__("Escull un plat", {plat.nom: None for plat in self.plats}, refrescar=False)

  def __str__(self) -> str:
    return '\n'.join(plat.nom + (' (V) ' if plat.veg else ' ') +
                     f'- {plat.preu/100:.2f}€' for plat in self.plats)

  def __getitem__(self, key):
    return self.plats[key]

  def __dir__(self):
    return {plat.nom: None for plat in self.plats}

  def mostrar(self, pause=False):
    titol("Carta")
    print(self)
    if pause:
     Pausar()

  def esborrar(self):
    i = Opcio("Esborrar plat", dir(self), enrere="Acabar")()
    if i > 0:
      i -= 1
      # TODO: Comprovar que el plat no estigui en una comanda
      del self.plats[i]
      self.esborrar()

  def afegir(self):
    titol("Afegir plat")
    