def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.

    typ = figurka["typ"]
    pozice = figurka["pozice"]

    # přesahuje šachovnici?
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    # je cílová pozice obsazená?
    if cilova_pozice in obsazene_pozice:
        return False

    # pohyb figurky
    if typ == "pěšec":
        if pozice[1] == cilova_pozice[1]:  # stejný sloupec
            if pozice[0] == 2 and cilova_pozice[0] == 4:  # pohyb o 2 pole - když je ve 2. řádku
                if (3, pozice[1]) not in obsazene_pozice: # pokud mezi tím není obsazené pole
                    return True
            
            elif cilova_pozice[0] == pozice[0] + 1:  # pohyb o 1 pole dopředu
                return True
            
        return False

    elif typ == "jezdec":
        x = abs(cilova_pozice[0] - pozice[0])
        y = abs(cilova_pozice[1] - pozice[1])

        return (x == 2 and y == 1) or (x == 1 and y == 2)

    elif typ == "věž":
        if pozice[0] == cilova_pozice[0]:  # stejný řádek

            start = pozice[1]
            end = cilova_pozice[1]

            if start > end:
                start, end = end, start

            for col in range(start + 1, end):
                if (pozice[0], col) in obsazene_pozice:

                    return False
            return True
        
        elif pozice[1] == cilova_pozice[1]:  # stejný sloupec

            start = pozice[0]
            end = cilova_pozice[0]

            if start > end:
                start, end = end, start

            for row in range(start + 1, end):
                if (row, pozice[1]) in obsazene_pozice:
                    return False
                
            return True
        return False

    elif typ == "střelec":

        x = abs(cilova_pozice[0] - pozice[0])
        y = abs(cilova_pozice[1] - pozice[1])

        if x == y:

            smer_x = 1 if cilova_pozice[0] > pozice[0] else -1
            smer_y = 1 if cilova_pozice[1] > pozice[1] else -1

            for i in range(1, x):

                mezipolicko = (pozice[0] + i * smer_x, pozice[1] + i * smer_y)
                if mezipolicko in obsazene_pozice:
                    return False
                
            return True
        return False

    elif typ == "dáma":
        if pozice[0] == cilova_pozice[0] or pozice[1] == cilova_pozice[1]:  # pohyb jako věž
            return je_tah_mozny({"typ": "věž", "pozice": pozice}, cilova_pozice, obsazene_pozice)
        
        elif abs(cilova_pozice[0] - pozice[0]) == abs(cilova_pozice[1] - pozice[1]):  # pohyb jako střelec
            return je_tah_mozny({"typ": "střelec", "pozice": pozice}, cilova_pozice, obsazene_pozice)
        return False

    elif typ == "král":

        x = abs(cilova_pozice[0] - pozice[0])
        y = abs(cilova_pozice[1] - pozice[1])

        if x <= 1 and y <= 1:  # pohybuje se jen o jedno pole
            return True
        return False

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu může pěšec o 2 body
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True