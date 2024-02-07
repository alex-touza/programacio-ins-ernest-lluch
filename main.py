from carta import Carta
from plat import Plat
from restaurant import Restaurant

from colorama import init

from text import Colors

init()

# Taula actual
t = 0


def main():
	carta = Carta([
		Plat("Espaguetis", 800, True),
		Plat("Arròs", 650, True),
		Plat("Pizza", 1000, False),
		Plat("Amanida", 500, True),
		Plat("Bistec", 1250, False),
		Plat("Feijoada", 2000, True)
	])
	restaurant = Restaurant(carta)

	while True:
		try:
			restaurant()
		except Exception as e:
			Colors.error()
			raise e

if __name__ == "__main__":
	main()
