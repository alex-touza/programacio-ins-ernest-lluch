from __future__ import annotations
from collections.abc import Iterable
from io import TextIOWrapper
from typing import Literal
from typing_extensions import LiteralString
from enum import Enum
from os.path import isfile
from os import remove

from text import catch


class Modes(Enum):
	Write = 'w'
	Read = 'r'
	Append = 'a'


class Fitxer:

	def __init__(self, title: str, path: str | None = None) -> None:
		self.title = title
		self.path = title + '.txt' if path is None else path

		self.obj: TextIOWrapper | None = None
		self.mode: Modes | None = None
		self.content: list[str] = []
		self.ends_with_newline = True

	@property
	def isOpen(self) -> bool:
		return self.obj is not None

	def begin(self, _mode: Modes) -> Fitxer:
		if self.mode == _mode:
			raise Exception
		else:
			if self.mode is not None:
				self.end()

			self.mode = _mode
			self.obj = open(self.path, _mode.value)

			if self.mode == Modes.Read:
				self.content = []
				self.read()

			return self

	def end(self, noexcept=False) -> Fitxer:
		if self.mode is not None:
			assert self.obj is not None

			self.mode = None
			self.obj.close()
			self.obj = None

			return self
		elif not noexcept:
			raise Exception

	def get_line(self, index: int):
		if self.mode == Modes.Read:
			assert self.content

			return self.content[index]
		elif self.obj is None:
			with open(self.path, Modes.Write.value) as f:
				return f.readlines()[index].rstrip('\n')
		else:
			raise Exception

	def write(self, s: str) -> Fitxer:
		if self.mode == Modes.Write or self.mode == Modes.Append:
			assert self.obj is not None
			self.obj.write(s)
			self.obj.flush()
		elif self.obj is None:
			with open(self.path, Modes.Append.value) as f:
				f.write(s)
				f.flush()
		else:
			raise Exception

		return self

	def iter_write(self, iter: list[str]) -> Fitxer:
		if self.mode == Modes.Write or self.mode == Modes.Append or self.obj is None:
			obj = open(self.path,
								 Modes.Append.value) if self.obj is None else self.obj
			if not self.ends_with_newline:
				obj.write('\n')
			obj.writelines([line + '\n' for line in iter])

			if self.mode == Modes.Write:
				self.content = iter
			else:
				self.content.extend(iter)

			obj.seek(0)

			if self.obj is None:
				obj.close()

			return self
		else:
			raise Exception

	def read(self, line: int | None = None, force=False) -> Fitxer:
		if self.mode is Modes.Read or self.obj is None and self.exists():
			obj = open(self.path, Modes.Read.value) if self.obj is None else self.obj

			self.content = obj.readlines()
			self.ends_with_newline = len(
					self.content) == 0 or self.content[-1].endswith("\n")
			self.content = [l.rstrip('\n') for l in self.content]
			obj.seek(0)

			if self.obj is None:
				obj.close()

			return self
		else:
			raise Exception

	def exists(self) -> bool:
		return isfile(self.path)

	def isEmpty(self) -> bool:
		if self.mode is Modes.Read or self.obj is None and self.exists():
			if self.obj is None and (self.content is None or len(self.content) == 0):
				self.read()
			return len(self.content) == 0
		else:
			raise Exception

	def remove(self, noexcept=False):
		self.end(noexcept=True)

		if self.exists():
			remove(self.path)
		elif not noexcept:
			raise FileNotFoundError

	def csv_read(self, force_read=False) -> list | Literal[False]:
		try:
			if force_read or len(self.content) == 0:
				self.read()
		except Exception:
			return False

		csv = []

		if len(self.content) == 1:
			return False

		for line in self.content[1:]:
			csv.append(line.split(','))

		return csv
