# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

import math

class Shape:

    def area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        
        self.width = width
        self.height = height

    def area(self):
        
        return self.width * self.height  # vynásobit délku obdélníku s šířkou obdélníku

class Circle(Shape):
    def __init__(self, radius):
        
        self.radius = radius

    def area(self):

        return math.pi * (self.radius ** 2) # obsah kruhu je (S = π * r²)
    
    
from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3