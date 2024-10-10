seznam_cisel = {
        0: "nula",
        1: "jedna",
        2: "dva",
        3: "tři",
        4: "čtyři",
        5: "pět",
        6: "šest",
        7: "sedm",
        8: "osm",
        9: "devět",
        10: "deset",
        11: "jedenáct",
        12: "dvanáct",
        13: "třináct",
        14: "čtrnáct",
        15: "patnáct",
        16: "šestnáct",
        17: "sedmnáct",
        18: "osmnáct",
        19: "devatenáct",
        20: "dvacet",
        30: "třicet",
        40: "čtyřicet",
        50: "padesát",
        60: "šedesát",
        70: "sedmdesát",
        80: "osmdesát",
        90: "devadesát",
        100: "sto"
    }


def cislo_text(cislo):
        
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100

        if cislo in seznam_cisel : #seznam_cisel[cislo]
            return seznam_cisel[cislo]
        
        elif cislo > 100 or cislo < 0: #pokud to třeba přesahuje
            return f"Číslo {cislo} přesahuje omezení 0 - 100"
        
        else: # např. když je číslo 25

            desitky = (cislo // 10) * 10
            jednotky = cislo % 10

            return f"{seznam_cisel[desitky]} {seznam_cisel[jednotky]}"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(int(cislo))
    print(text)

""" 
cislo = 0
while cislo <= 100:
    text = cislo_text(int(cislo))
    print(text)
    cislo += 1  
"""