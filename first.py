# otestuje číslo, zda je liché nebo sudé
def sudy_nebo_lichy(cislo : int):
    if cislo % 2 == 0:
        return f"Číslo {cislo} je sudé"
    else:
        return f"Číslo {cislo} je liché"
    
m = sudy_nebo_lichy(5)
print(m)

m = sudy_nebo_lichy(1000000)
print(m)