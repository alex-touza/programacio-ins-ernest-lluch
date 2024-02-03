# L'administrador del llibre és en una classe separada
# per no copiar els mètodes per a cadascun.
from formularis import pausar
from id import ID
from llibre import Estat, Llibre
from menu import Menu
from text import taula
from usuaris import Usuaris


class AdminLlibre(Menu):

  def __init__(self, llibre_index: int, ref_llibres: list[Llibre], ids: ID, ref_usuaris: Usuaris):
    self.llibre_index = llibre_index
    self.ref_llibres = ref_llibres
    self.ref_usuaris = ref_usuaris
    self.llibre = self.ref_llibres[self.llibre_index]
    self.ids = ids
    assert self.llibre is not None
    
    super().__init__("Administrar llibre | " + (
        lambda t: t if len(t) <= 25 else (f'{t:.15}...'))(self.llibre.titol))
    
  @Menu.menu(
      lambda self: self.llibre.estat,
      lambda self: f"#{self.llibre.id} - {self.llibre.estat.value.capitalize()}")
  def __call__(self):
    pass

  @Menu.eina("Préstec", 1, Estat.Disponible)
  def prestec(self):
    pass

  @Menu.eina("Tornar", (1, 1), (Estat.EnPrestec, Estat.EnPrestecReservat))
  def tornar(self):
    pass

  @Menu.eina("Reservar", 2, Estat.EnPrestec)
  def reservat(self):
    pass

  @Menu.eina("Cancel·lar reserva", 2, Estat.EnPrestecReservat)
  def cancelar_reserva(self):
    pass

  @Menu.eina("Informació", (2, 3, 3),
             (Estat.Disponible, Estat.EnPrestec, Estat.EnPrestecReservat))
  def info(self):
    pass

  @Menu.eina("Historial", (3, 4, 4),
             (Estat.Disponible, Estat.EnPrestec, Estat.EnPrestecReservat))
  def historial(self):
    
    for user_id, accio in self.llibre.historial:
      print()

  @Menu.eina("Esborrar", 4, Estat.Disponible)
  def esborrar(self):
    self.ref_llibres.pop(self.llibre_index)
    self.llibre.estat = Estat.Esborrat
    
    self.ids.eliminar(self.llibre.id)
    print(f"Llibre amb ID #{self.llibre.id} esborrat.")
    pausar()
    
