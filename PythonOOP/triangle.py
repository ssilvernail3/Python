from math import sqrt
from random import randint


class Triangle:
    """
    A class used to represent a right Triangle

    Attributes
    -------------------
    a: int
        len of side a
    b: int
        len of side b
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'<Triangle a = {self.a} & b = {self.b}>'

    def __str__(self):
        return self.describe()

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b 


    @classmethod
    # this acts as a factory for making new triangles 'cls' refers to the 'class Triangle'!
    def random(cls):
        """Class Method which returns triangle with random sides"""
        return cls(randint(5, 100), randint(5, 100))

    def get_hypotenuse(self):
        """Calculates hypotenuse (3rd side of right triangle)"""
        return sqrt(self.a ** 2 + self.b ** 2)

    def get_area(self):
        """Calculates area of right triangle (a * b) / 2"""
        return self.a * self.b / 2

    def describe(self):
        """returns string representing triangle"""
        return f"I am a triangle with sides: {self.a} & {self.b}"
