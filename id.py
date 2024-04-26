from random import randint
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

# ID alfabètic
class AID:
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


# Realment no és un UUID de veritat, sinó simplement un generador d'IDs alfanumèrics no consecutius.
class UUID:
	def __init__(self) -> None:
		self.usats: list[str] = []

	def __call__(self) -> str:
		s = ''

		while s == '' or s in self.usats:
			s = ''.join(str(randint(0, 9)) for _ in range(4)) \
			+ '-' \
			+ ''.join(chr(randint(65, 90)) for _ in range(2))
		
		self.usats.append(s)

		return s

	def existeix(self, uuid: str) -> bool:
		return uuid in self.usats
