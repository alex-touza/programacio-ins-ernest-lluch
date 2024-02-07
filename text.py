from colorama import Fore, Style


class Modificador:
    def __init__(self, c: str):
        self.c = c

    def __str__(self):
        return self.c

    def __call__(self, text = None) -> str | None:
        if text is None:
            print(self.c, end="")
            return None
        else:
            return self.c + str(text) + Style.RESET_ALL

    # Afegim funcions màgiques de suma perquè actuïn com a strings
    def __add__(self, other):
        return str(self) + other
        
    def __radd__(self, other):
        return other + str(self)

class Colors:
    opcions = Modificador(Fore.BLUE)
    entrada = Modificador(Fore.YELLOW)
    error = Modificador(Fore.RED)
    reset = Modificador(Fore.RESET)

class Estils:
    brillant = Modificador(Style.BRIGHT)
    fosc = Modificador(Style.DIM)