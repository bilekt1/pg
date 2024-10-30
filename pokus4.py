def jaccardova_vzdalenost_mnozin(mnozina1, mnozina2):
    """
    Jaccardova vzdalenost říká, jak jsou dvě množiny rozdílné 0 znamená, že jsou stejné, 1 znamená, že jsou zcela rozdílné
    """
    
    mnozina1 = set(mnozina1)
    mnozina2 = set(mnozina2)

    Index = len(mnozina1.intersection(mnozina2)) / len(mnozina1.union(mnozina2))
    vzdalenost = 1 - Index

    return vzdalenost


if __name__ == "__main__":
    serp1 = ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    serp2 = ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    serp3 = ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]

    #print(jaccardova_vzdalenost_mnozin(serp1, serp2))
    #print(jaccardova_vzdalenost_mnozin(serp2, serp3))
    #print(jaccardova_vzdalenost_mnozin(serp1, serp3))



def levensteinova_vzdalenost(dotaz1, dotaz2):
    """
    Levensteinova vzdalenost říka, jak jsou 2 řetězce rozdílné, pokud jsou stejné je Levensteinova vzdalenost 0,
    pro řetězce "čas" a "čaj" je Levensteinova vzdalenost 1 (liší se v 1 písmenu)
    """
    lenght = max(len(dotaz1), len(dotaz2))  # 8
    i = 0
    levenstein = 0
    while i < lenght:
        if i < len(dotaz1) and i < len(dotaz2):
            if dotaz1[i] != dotaz2[i]:
                levenstein += 1
        else:
            levenstein += 1
        i += 1
    return levenstein


def levensteinova_vzdalenost_for(dotaz1, dotaz2):
    lenght = min(len(dotaz1), len(dotaz2))  # 6
    levenstein = 0
    for i in range(lenght):
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))
    return levenstein


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    #print(levensteinova_vzdalenost(query1, query2))
    #print(levensteinova_vzdalenost(query2, query3))
    #print(levensteinova_vzdalenost(query1, query3))

def deduplikace_dotazu(dotazy):
    """
    tato funkce spocita jaccardovu vzdalenost a levensteinovu vzadelnost a vyradi z seznamu dotazy, polozky, ktere budou mit
    jaccardovu vzdalenost mensi nez 0.5 a levensteinovu vzdalenost <= 1
    """

    export = ["hm"]
    export = export.clear

    for dotaz in dotazy:
        for i in range(0, len(dotaz["serp"])):

            leven = levensteinova_vzdalenost(dotaz["dotaz"], dotaz["serp"][i])
            jaccard = jaccardova_vzdalenost_mnozin(dotaz["dotaz"], dotaz["serp"][i])

            if leven <= 1 and jaccard < 0.5:
                export.append(dotaz["serp"][i])

    return export


if __name__ == "__main__":

    dotaz1 = {
        "dotaz": "seznam",
        "serp": ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    }
    dotaz2 = {
        "dotaz": "seznamka",
        "serp": ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    }
    dotaz3 = {
        "dotaz": "sesnam",
        "serp": ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    }
    dotaz4 = {
        "dotaz": "google",
        "serp": ["https://www.google.com", "https://maps.google.com", "https://www.gmail.com"]
    }
    print(deduplikace_dotazu([dotaz1, dotaz2, dotaz3, dotaz4]))