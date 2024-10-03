# print("Hello World")
# print(1 + 1)
# print(6 / 3)

"""
===================================================
"""

def hello_world():
    print("Hello World")
    
# funkce, která napíše 5 hvězdiček
def five_stars():
    i = 0
    while i < 5:
        print("*")
        i += 1

# funkce, která napíše zadaný počet hvězdiček
def count_numbers(many : int):
    i = 0
    while i < many:
        print("*")
        i += 1

# funkce, která ověří zda je number v rozmezi minimum - maximum a vypíše textový vystup
def in_range(number : int, minimum : int, maximum : int):
    if number > minimum and number < maximum:
        print("In range")
    else:
         print("Out of range")


in_range(1, 100, 1000)
in_range(500, 100, 1000)