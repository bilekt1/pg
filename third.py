def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.

    Napoveda jak otestova prvocislo:
    Cislo 36 vznikne nasobenim:
    1 * 36
    2 * 18
    3 * 12
    4 * 9
    6 * 6
    9 * 4
    12 * 3
    18 * 2
    36 * 1
    Jak vidite v druhe polovine se dvojice opakuji, tzn. v tomto pripade staci overit delitelnost pouze do 6 (vcetne)
    """

    if cislo <= 1:
        return False
        # return f"{cislo} je rovno či menší než 1, tudíž nemůže být prvočíslo"
    else:
        for i in range(2, cislo):
        # pokud je číslo dělitelné "i" a nezůstane zbytek -> není to prvočíslo (prvočíslo je dělitelné 1 a stejným číslem)
            if cislo % i == 0:
                return False
        
    return True

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """

    maximum = int(maximum)

    seznam = []
    pokus = 1

    if maximum >= 2:
        while pokus <= maximum:

          vysledek = je_prvocislo(pokus)

          if vysledek == True:
             seznam.append(pokus) 
          """else:
            print(f"číslo {pokus} není prvočíslo")"""
            

          pokus += 1
        else:
            return seznam
    else:
        return "Zadejte číslo větší než 1"

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)