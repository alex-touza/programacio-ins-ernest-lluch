from formularis import Opcio
from id import ID
from llibre import Llibre
from menu import Menu
from text import taula
from usuari import Usuari
from usuaris import Usuaris
from cataleg import Cataleg
from prestecs import Prestecs

class Biblioteca(Menu):

  def __init__(self, cataleg: Cataleg, usuaris: Usuaris) -> None:
    self.cataleg = cataleg
    self.usuaris = usuaris
    self.prestecs = Prestecs(usuaris, cataleg)

    super().__init__("Biblioteca", enrere="Sortir")

  @Menu.menu()
  def __call__(self):
    print(self)
    print()
    pass

  @Menu.eina("Catàleg", 1, func_clau='cataleg')
  def admin_catàleg(self):
    pass

  @Menu.eina("Usuaris", 2, func_clau='usuaris')
  def admin_usuaris(self):
    pass

  @Menu.eina("Préstecs", 3, func_clau='prestecs')
  def admin_prestecs(self):
    pass

  def __str__(self) -> str:
    return '\n'.join([str(self.cataleg), str(self.usuaris), str(self.prestecs)])


usuari_id = ID()
llibre_id = ID()

usuaris = Usuaris([
    Usuari("Hug", "Montolí", usuari_id()),
    Usuari("Mikhaïl", "Gorbatxov", usuari_id()),
    Usuari("Miquel", "Garcia", usuari_id())
], usuari_id)

cataleg = Cataleg([
    Llibre("Entre dos blaus", "Arturo Padilla de Juan", 2020, llibre_id()),
    Llibre("El senyor dels anells", "J.R.R. Tolkien", 1954, llibre_id())
], llibre_id, usuaris)

biblioteca = Biblioteca(cataleg, usuaris)

biblioteca()
print("Fins aviat!")
