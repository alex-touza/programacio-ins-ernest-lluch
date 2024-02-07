# L'administrador del llibre és en una classe separada
# per no copiar els mètodes per a cadascun.
from formularis import Decisio, pausar
from id import ID
from llibre import Estat, Llibre
from menu import Menu
from text import taula


class AdminLlibre(Menu):

  def __init__(self, llibre_id: int, ref_llibres: list[Llibre], ids: ID):
    self.llibre_id = llibre_id
    self.ref_llibres = ref_llibres

    self.ids = ids

    assert self.ids.existeix(self.llibre_id), "L'ID no existeix"

    self.llibre = None
    for l in self.ref_llibres:
      if l.id == self.llibre_id:
        self.llibre = l
        break

    assert self.llibre is not None, "El llibre que es vol administrar no existeix."

    super().__init__("Administrar llibre | " + (
        lambda t: t if len(t) <= 25 else (f'{t:.15}...'))(self.llibre.titol))

  def _confirmar(self, missatge: str) -> bool:
    return Decisio(None, False, missatge, "Enrere", None, str(self.llibre))()

  @Menu.menu(lambda self: self.llibre.estat, lambda self:
             f"#{self.llibre.id} - {self.llibre.estat.value.capitalize()}")
  def __call__(self):
    pass

  @Menu.eina("Préstec", 1, Estat.Disponible)
  def prestec(self):
    assert self.llibre is not None
    
    if self.llibre.estat is Estat.EnPrestec:
      print()
      print("El llibre ja està en préstec.")
      pausar(nova_linia=True)
      return
    
    if not self._confirmar("Fer préstec"):
      return


    self.llibre.prestec()

    print("Préstec realitzat.")
    pausar(nova_linia=True)

  @Menu.eina("Retornar", 1, Estat.EnPrestec)
  def retornar(self):
    assert self.llibre is not None

    if self.llibre.estat is Estat.Disponible:
      print()
      print("El llibre no té cap préstec actiu.")
      pausar(nova_linia=True)
      return
    
    if not self._confirmar("Retornar llibre"):
      return

    self.llibre.retornar()

    print("Llibre retornat.")
    pausar(nova_linia=True)

  @Menu.eina("Informació", (2, 2), (Estat.Disponible, Estat.EnPrestec))
  def info(self):
    print(str(self.llibre))
    pausar(nova_linia=True)

  @Menu.eina("Esborrar", 3, Estat.Disponible)
  def esborrar(self):
    if Decisio(None, False, "Esborrar", "Enrere", None,
               str(self.llibre))() == 0:
      return

    i = 0
    for l in self.ref_llibres:
      if l.id == self.llibre_id:
        self.ref_llibres.pop(i)
        break
      i += 1

    assert self.llibre is not None
    self.llibre.estat = Estat.Esborrat

    self.ids.eliminar(self.llibre.id)
    print(f"Llibre amb ID #{self.llibre.id} esborrat.")
    print()
    pausar()

    self.sortir()
