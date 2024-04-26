from __future__ import annotations

class Paquet:
	def __init__(self, uuid: str, contingut: str) -> None:
		self.uuid = uuid
		self.contingut = contingut
		self.bustia: Bustia | None = None

	def enviar(self, bustia: Bustia) -> None:
		bustia.enviarPaquet(self)

	def recollir(self):
		if not self.bustia:
			raise ValueError
		else:
			self.bustia.recollirPaquet()

	def __str__(self):
		return f"Paquet {self.uuid} [{self.contingut}] --> Bústia #{self.bustia.id}" if self.bustia else f"Paquet #{self.uuid} [{self.contingut}]"


class Bustia:
	def __init__(self, id: str):
		self.id = id
		self.paquet: Paquet | None = None

	def enviarPaquet(self, p: Paquet) -> None:
		if self.paquet:
			raise ValueError
		else:
			self.paquet = p
			self.paquet.bustia = self

	def recollirPaquet(self) -> Paquet:
		if not self.paquet:
			raise ValueError
		else:
			p = self.paquet
			self.paquet = None
			p.bustia = None
			return p

	def __str__(self):
		return f"Bústia #{self.id} --> Paquet {self.paquet.uuid} [{self.paquet.contingut}]" if self.paquet else f"Bústia #{self.id} (buida)"