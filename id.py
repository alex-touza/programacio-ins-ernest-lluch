from sortedcontainers import SortedSet

class ID:
	def __init__(self) -> None:
		self.n = 0
		self.lliures: SortedSet[int] = SortedSet()

	def __call__(self) -> int:
		r = self.n if len(self.lliures) == 0 else self.lliures.pop(0)
		self.n += 1
		return r

	def eliminar(self, id: int) -> None:
		assert self.existeix(id)
		
		self.n -= 1
		
		if self.n != id:
			self.lliures.add(id)

	def existeix(self, id: int) -> bool:
		return id < self.n and not self.lliures.count(id)

	