""" Module to represent and calculate properties of triangles """
from functools import total_ordering
import math
from typing import Self


@total_ordering
class RightTriangle:
    """ RightTriangle class to represent a right-angled triangle """

    def __init__(self, a: float, b: float) -> None:
        """ Initialize the RightTriangle with sides a and b
            Args:
                a (float): length of the side opposite the angle
                b (float): length of the side adjacent to the angle
        """
        self.a: float = a
        self.b: float = b
        self.c: float = math.sqrt(a**2 + b**2)

    def adjacent(self) -> float:
        """ Return the length of the adjacent side """
        return self.b

    def opposite(self) -> float:
        """ Return the length of the opposite side """
        return self.a

    def hypotenuse(self) -> float:
        """ Calculate the hypotenuse of the triangle """
        return self.c

    def area(self) -> float:
        """ Calculate the area of the triangle """
        return 0.5 * self.opposite() * self.adjacent()

    def perimeter(self) -> float:
        """ Calculate the perimeter of the triangle """
        return self.opposite() + self.adjacent() + self.hypotenuse()

    def inradius(self) -> float:
        """ Calculate the inradius of the triangle """
        return self.area() / (0.5 * self.perimeter())

    def circumradius(self) -> float:
        """ Calculate the circumradius of the triangle """
        return self.hypotenuse() / 2

    def altitude(self) -> float:
        """ Calculate the altitude from the right angle to the hypotenuse """
        return (self.opposite() * self.adjacent()) / self.hypotenuse()

    def alpha(self) -> float:
        """ Calculate angle alpha in radians """
        return math.atan(self.opposite() / self.adjacent())

    def beta(self) -> float:
        """ Calculate angle beta in radians """
        return math.atan(self.adjacent() / self.opposite())

    def sin(self) -> float:
        """ Calculate sine of the angle """
        return self.opposite() / self.hypotenuse()

    def cos(self) -> float:
        """ Calculate cosine of the angle """
        return self.adjacent() / self.hypotenuse()

    def tan(self) -> float:
        """ Calculate tangent of the angle """
        return self.opposite() / self.adjacent()

    def sec(self) -> float:
        """ Calculate secant of the angle """
        return self.hypotenuse() / self.adjacent()

    def cot(self) -> float:
        """ Calculate cotangent of the angle """
        return self.adjacent() / self.opposite()

    def csc(self) -> float:
        """ Calculate cosecant of the angle """
        return self.hypotenuse() / self.opposite()

    def __imul__(self, scale: float) -> Self:
        """ In-place scale the area of the triangle by a factor """
        self.a *= math.sqrt(scale)
        self.b *= math.sqrt(scale)
        self.c *= math.sqrt(scale)
        return self

    def __itruediv__(self, scale: float) -> Self:
        """ In-place scale the area of the triangle down by a factor """
        self *= (1/scale)
        return self

    def __mul__(self, scale: float):
        """ Scale the area of the triangle by a factor """
        new = RightTriangle(self.a, self.b)
        new *= scale
        return new

    def __truediv__(self, scale: float) -> RightTriangle:
        """ Scale the area of the triangle down by a factor """
        new = RightTriangle(self.a, self.b)
        new /= scale
        return new

    def __eq__(self, other) -> bool:
        """ Equality comparison for RightTriangle """
        return self.a == other.a and self.b == other.b and self.c == other.c

    def __lt__(self, other) -> bool:
        """ Less-than comparison for RightTriangle based on area """
        return self.area() < other.area()

    def __str__(self) -> str:
        """ String representation of the RightTriangle """
        return f"RightTriangle(a={self.a}, b={self.b}, c={self.c})"

    def __repr__(self) -> str:
        """ String representation of the RightTriangle """
        return f"{self.a}, {self.b}, {self.c}"
