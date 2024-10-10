
"""
def porovnej(cislo):
    if cislo > 100:
        print(cislo, " je větší než 100")
    else:
        print(cislo, " je menší než 100")

if __name__ == "__main__":
    a = input("Zadej cislo: ")
    a = int(a)
"""



# funkce vrati treti prvek ze seznamu, pokud ma mene nez 3 prvky, vrati None
def vrat_treti(seznam):
    if len(seznam) >= 3:
        return seznam[2]
    else:
        return None

# funkce spocita prumer z hodnot v seznamu, pouzijte sum(), len()
def udelej_prumer(seznam):
    prumer = sum(seznam) / len(seznam)
    return prumer

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    return f"Jméno: {slovnik["jmeno"]}, Příjmení: {slovnik["prijmeni"]}, Věk: {slovnik["vek"]}, Průměrná známka: {udelej_prumer(slovnik["znamky"])}"


if __name__ == "__main__":
    seznam = [9,8,5]
    vysledek = vrat_treti(seznam)
    print(vysledek)

    obalka = [9,8,7,6]
    vysledek = udelej_prumer(obalka)
    print(vysledek)

    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    vysledek = naformatuj_text(student)
    print(vysledek)

    student["vek"] # -> 21
    student["znamky"] # -> [1, 2, 1, 1, 3, 2]
    student["znamky"][2] # -> 1

    a = 1
    f"Naformatovany retezes s hodnotou {a}" # ""Naformatovany retezes s hodnotou 1"