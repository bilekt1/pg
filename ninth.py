'''def dec_to_bin2(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"

    cislo = int(cislo)

    maxcislo = 0
    i = 0

    while maxcislo < cislo:
        
        maxcislo = 2 ** i

        i += 1
    
    binary =  ""
    moc = i

    while i >= len(binary):
        print(len(binary))
        
        if (cislo - (2 ** moc)) > cislo:
            binary += "1"
        else:
            binary += "0"

        moc -= 1

    return binary'''

def dec_to_bin(cislo):
    cislo = int(cislo)
    if cislo == 0:
        return "0"
    elif cislo == 1:
        return "1"
    else:
        return dec_to_bin(cislo // 2) + str(cislo % 2)


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"

'''if __name__ == "__main__":
    dec_to_bin(100)'''