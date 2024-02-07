from sortedcontainers import SortedSet

# Sistema de reutilització d'IDs.
# M'he adonat que realment és una idea terrible...
# class ID:
# 	def __init__(self) -> None:
# 		self.n = 0
# 		self.lliures: SortedSet[int] = SortedSet()
# 
# 	def __call__(self) -> int:
# 		r = self.n if len(self.lliures) == 0 else self.lliures.pop(0)
# 		self.n += 1
# 		return r
# 
# 	def eliminar(self, id: int) -> None:
# 		assert self.existeix(id)
# 		
# 		self.n -= 1
# 		
# 		if self.n != id:
# 			self.lliures.add(id)
# 
# 	def existeix(self, id: int) -> bool:
# 		return id < self.n and not self.lliures.count(id)

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