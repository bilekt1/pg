def nejvetsi(seznam_cisel):

    nejvetsi_cislo = 0

    #return max(seznam_cisel)

    for Number in seznam_cisel:
        if Number > nejvetsi_cislo:
            nejvetsi_cislo = Number

    return nejvetsi_cislo

def test_nejvetsi():
    assert nejvetsi([1, 5, 3, 4, 9, 6]) == 9
    assert nejvetsi([1, 5, 3, 4, 0, 2]) == 5