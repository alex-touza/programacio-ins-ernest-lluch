class ID:
	def __init__(self, inici=1) -> None:
		self.inici = inici
		self.n = inici
		self.eliminats: list[int] = []

	def __call__(self) -> int:
		r = self.n
		self.n += 1
		return r

	def eliminar(self, id: int) -> None:
		self.eliminats.append(id)

	def existeix(self, id: int) -> bool:
		return self.inici <= id < self.n and not self.eliminats.count(id)

# En algun moment pot semblar que els identificadors estiguin mal numerats.
# Per exemple, aquesta llista de col·leccions és possible:
# 
# #1 a (2 películ·les)
# #2 b (2 películ·les)
# #3 c (3 películ·les)
# #6 d (3 películ·les)
#
# AIXÒ NO ÉS UN BUG. Cada cop que es crea una col·lecció temporal, encara
# que es descarti, genera un nou identificador únic que no podrà ser
# reutilitzat. Abans vaig implementar un sistema de reutilització de
# IDs però realment tot el sentit d'aquests és que siguin únics, i això
# segueix sent així per a les instàncies temporals.