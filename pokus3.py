def my_range(start, stop, step=1):
    
    results = []

    cislo = start

    while cislo < stop:

        results.append(cislo)

        cislo += step

    return results

""" 
if __name__ == "__main__":

    seznam = list(range(1,10))
    print(seznam)

    seznam = my_range(1, 10, 2)
    print(seznam)
"""

def my_enumerate(iterable, start=0):
    """
    Nase vlastni implementace enumerate()
    """
    results = []
    index = start
    for value in iterable:
        results.append( (index, value) )
        index += 1
    return results


def while_enumerate(iterable, start=0):
    results = []
    i = 0
    while i < len(iterable):
        results.append( (start + i, iterable[i]) )
        i += 1
    return results


if __name__ == "__main__":

    seznam = list(enumerate(["ahoj", "cau", "jak", "se", "mas"], 2))
    print(seznam)

    seznam = while_enumerate(["ahoj", "cau", "jak", "se", "mas"], 2)
    print(seznam)

    # for i, hodnota in seznam:
    #     print(f'Slovo {hodnota} je na {i}. pozici')


def my_zip(*iterables):

    results = []

    length = len(iterables[0])
    i = 0

    while i < length:
        subresult = []
        for iterable in iterables:
            subresult.append(iterable[i])
        results.append(tuple(subresult))
        i += 1

    return results

    

if __name__ == "__main__":

    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
    vek = [30, 20, 24, 18, 27]
    vaha = [50, 34, 45, 34, 47]

    print(my_zip(jmena, vek, vaha))
