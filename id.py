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
