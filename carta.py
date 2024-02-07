from administrador import Administrador
from formularis import Opcio, Text, Decisio, Nombre, Pausar, clear, titol
from plat import Plat


class Carta(Administrador):

  def __init__(self, plats: list[Plat]):
    self.plats = plats
    self.ordenar()

    super().__init__("Carta")
    
  def __str__(self) -> str:
    return '\n'.join(str(plat) for plat in self.plats)

  def __getitem__(self, key):
    return self.plats[key]

  @Administrador.menu()
  def __call__(self) -> None:
    pass

  def ordenar(self):
    self.plats.sort(key=lambda plat: (-plat.veg, plat.nom))

  def dict(self):
    return {str(plat): None for plat in self.plats}


  @Administrador.eina("Mostrar carta", 0)
  def mostrar(self) -> None:
    print(str(self))
    Pausar()

  
  @Administrador.eina("Esborrar plats", 2)
  def esborrar(self):
    i = 1
    while True:
      i = Opcio(None, self.dict(), enrere="Acabar", sep="", refrescar=False)()
      if i > 0:
        i -= 1
        # TODO: Comprovar que el plat no estigui en una comanda
        del self.plats[i]

      else:
        break
      


  @Administrador.eina("Afegir plat", 1)
  def afegir(self):    
    nom = Text("Nom del plat", lambda t, le: 0 < le <= 30, buit=True)()
    if nom == "":
      return
      
    preu = Nombre("Preu del plat en cèntims", lambda n: 0 < n <= 10000, buit=True)()
    if preu is None:
      return
    
    veg = Text("Plat vegetarià (S/N)", lambda t, le: t.upper() in ["S", "N"], buit=True)() == "S"

    plat = Plat(nom, preu, veg)
    print()
    print("S'afegirà el plat:")
    print(plat)
    if Decisio(None, refrescar=False, si="Confirmar", no="Enrere")():
      self.plats.append(plat)
      self.ordenar()