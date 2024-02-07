from id import ID
from llibre import Llibre
from menu import Menu
from cataleg import Cataleg
from prestecs import Prestecs


class Biblioteca(Menu):

  def __init__(self, cataleg: Cataleg) -> None:
    self.cataleg = cataleg
    # self.usuaris = usuaris
    self.prestecs = Prestecs(cataleg)

    super().__init__("Biblioteca", enrere="Sortir")

  @Menu.menu()
  def __call__(self):
    print(self)
    print()
    pass

  @Menu.eina("Catàleg", 1, func_clau='cataleg')
  def admin_catàleg(self):
    pass

  @Menu.eina("Préstecs", 2, func_clau='prestecs')
  def admin_prestecs(self):
    pass

  def __str__(self) -> str:
    return str(self.cataleg) + '\n' + str(self.prestecs)


# usuari_id = ID()
llibre_id = ID()

# usuaris = Usuaris([
#     Usuari("Hug", "Montolí", usuari_id()),
#     Usuari("Mikhaïl", "Gorbatxov", usuari_id()),
#     Usuari("Miquel", "Garcia", usuari_id())
# ], usuari_id)

cataleg = Cataleg(
  [
     Llibre("La plaça del diamant", "Mercè Rodoreda", 1962),
     Llibre("Jo confesso", "Jaume Cabré", 2011),
     Llibre("Mecanoscrit del segon origen", "Manuel de Pedrolo", 1974),
     Llibre("La dona dels ulls de serp", "Carme Riera", 1999),
     Llibre("Pa negre", "Emili Teixidor", 2003),
     Llibre("La catedral del mar", "Ildefonso Falcones", 2006),
     Llibre("Mirall trencat", "Mercè Rodoreda", 1974),
     Llibre("L'últim abat", "Josep M. Espinàs", 2010),
     Llibre("El cor de la nit", "Joan Perucho", 1961),
     Llibre("Els ocells de la universitat", "Joan Sales", 1939),
     Llibre("Les veus del Pamano", "Jaume Cabré", 2004),
     Llibre("La filla estrangera", "Najat El Hachmi", 2008),
     Llibre("Quaderns de l'exili", "Josep Carner", 1939),
     Llibre("La rosa del vent", "Sílvia Alcàntara", 1998),
     Llibre("Els hereus de la terra", "Ildefonso Falcones", 2009),
     Llibre("Vell llibre de dades", "Josep Pla", 1964),
     Llibre("La plaga", "Albert Sánchez Piñol", 2006),
     Llibre("L'ombra del vent", "Carlos Ruiz Zafón", 2001),
     Llibre("Marina", "Carlos Ruiz Zafón", 1999),
     Llibre("La pell freda", "Albert Sánchez Piñol", 2003),
     Llibre("Els jardins de la Memòria", "Rosa Maria Arquimbau", 1987),
     Llibre("El quadern gris", "Josep Pla", 1966),
  ],
    llibre_id)

biblioteca = Biblioteca(cataleg)

biblioteca()
print("Fins aviat!")
