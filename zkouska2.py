# napište funkci, která podle typu "+", "-", "*", "/" provede operaci a vrati vysledek

def operace(typ, a, b):
    matematicka_operace = None
    

if __name__ == "__main__":
    try:
        operace("+", 1, 2)
        operace("-", 2, 1)
        operace("*", 0, 5)
        operace("/", 4, 2)
        operace("/", 4, 0)
    except ZeroDivisionError:
        print("Dělení nulou nelze")