"""Module to represent and calculate properties of triangles"""

import math
from abc import ABC, abstractmethod
from functools import total_ordering
from typing import Self


@total_ordering
class Triangle(ABC):
    """Base Triangle class with common properties and methods"""

    def __init__(self, a: float, b: float, c: float) -> None:
        """Initialize the Triangle with sides a, b, and c
        Args:
            a (float): length of side a
            b (float): length of side b
            c (float): length of side c
        """
        self.a: float = a
        self.b: float = b
        self.c: float = c

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the triangle"""

    def perimeter(self) -> float:
        """Calculate the perimeter of the triangle"""
        return self.a + self.b + self.c

    def inradius(self) -> float:
        """Calculate the inradius of the triangle"""
        return self.area() / (0.5 * self.perimeter())

    def angle_a(self) -> float:
        """Calculate angle A (opposite to side a) in radians using law of cosines"""
        cos_a = (self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)
        return math.acos(cos_a)

    def angle_b(self) -> float:
        """Calculate angle B (opposite to side b) in radians using law of cosines"""
        cos_b = (self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)
        return math.acos(cos_b)

    def angle_c(self) -> float:
        """Calculate angle C (opposite to side c) in radians using law of cosines"""
        cos_c = (self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)
        return math.acos(cos_c)

    @abstractmethod
    def __imul__(self, scale: float) -> Self:
        """In-place scale the area of the triangle by a factor"""

    def __itruediv__(self, scale: int | float) -> Self:
        """In-place scale the area of the triangle down by a factor"""
        self *= 1 / scale
        return self

    def __eq__(self, other) -> bool:
        """Equality comparison for Triangle"""
        if not isinstance(other, Triangle):
            raise TypeError("Can only compare Triangle with another Triangle")
        return (
            math.isclose(self.a, other.a)
            and math.isclose(self.b, other.b)
            and math.isclose(self.c, other.c)
        )

    def __lt__(self, other) -> bool:
        """Less-than comparison for Triangle based on area"""
        if not isinstance(other, Triangle):
            raise TypeError("Can only compare Triangle with another Triangle")
        return self.area() < other.area()

    def __str__(self) -> str:
        """String representation of the Triangle"""
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"

    def __repr__(self) -> str:
        """String representation of the Triangle"""
        return f"a={self.a}, b={self.b}, c={self.c}"


@total_ordering
class RightTriangle(Triangle):
    """RightTriangle class to represent a right-angled triangle"""

    def __init__(self, a: int | float, b: int | float) -> None:
        """Initialize the RightTriangle with sides a and b
        Args:
            a (float): length of the side opposite the angle
            b (float): length of the side adjacent to the angle
        """
        c = math.sqrt(a**2 + b**2)
        super().__init__(a, b, c)

    def adjacent(self) -> float:
        """Return the length of the adjacent side"""
        return self.b

    def opposite(self) -> float:
        """Return the length of the opposite side"""
        return self.a

    def hypotenuse(self) -> float:
        """Calculate the hypotenuse of the triangle"""
        return self.c

    def area(self) -> float:
        """Calculate the area of the triangle"""
        return 0.5 * self.opposite() * self.adjacent()

    def circumradius(self) -> float:
        """Calculate the circumradius of the triangle"""
        return self.hypotenuse() / 2

    def altitude(self) -> float:
        """Calculate the altitude from the right angle to the hypotenuse"""
        return (self.opposite() * self.adjacent()) / self.hypotenuse()

    def alpha(self) -> float:
        """Calculate angle alpha in radians"""
        return math.atan(self.opposite() / self.adjacent())

    def beta(self) -> float:
        """Calculate angle beta in radians"""
        return math.atan(self.adjacent() / self.opposite())

    def angle_a(self) -> float:
        """Calculate angle A (opposite to side a) in radians"""
        return math.atan(self.a / self.b)

    def angle_b(self) -> float:
        """Calculate angle B (opposite to side b) in radians"""
        return math.atan(self.b / self.a)

    def angle_c(self) -> float:
        """Calculate angle C (the right angle) in radians"""
        return math.pi / 2

    def sin(self) -> float:
        """Calculate sine of the angle"""
        return self.opposite() / self.hypotenuse()

    def cos(self) -> float:
        """Calculate cosine of the angle"""
        return self.adjacent() / self.hypotenuse()

    def tan(self) -> float:
        """Calculate tangent of the angle"""
        return self.opposite() / self.adjacent()

    def sec(self) -> float:
        """Calculate secant of the angle"""
        return self.hypotenuse() / self.adjacent()

    def cot(self) -> float:
        """Calculate cotangent of the angle"""
        return self.adjacent() / self.opposite()

    def csc(self) -> float:
        """Calculate cosecant of the angle"""
        return self.hypotenuse() / self.opposite()

    def __imul__(self, scale: float) -> Self:
        """In-place scale the area of the triangle by a factor"""
        self.a *= math.sqrt(scale)
        self.b *= math.sqrt(scale)
        self.c *= math.sqrt(scale)
        return self

    def __mul__(self, scale: int | float) -> "RightTriangle":
        """Scale the area of the triangle by a factor"""
        new = RightTriangle(self.a, self.b)
        new *= scale
        return new

    def __truediv__(self, scale: int | float) -> "RightTriangle":
        """Scale the area of the triangle down by a factor"""
        new = RightTriangle(self.a, self.b)
        new /= scale
        return new

    def __eq__(self, other) -> bool:
        """Equality comparison for RightTriangle"""
        if not isinstance(other, RightTriangle):
            raise TypeError(
                "Can only compare RightTriangle with another RightTriangle")
        return super().__eq__(other)

    def __lt__(self, other) -> bool:
        """Less-than comparison for RightTriangle based on area"""
        if not isinstance(other, RightTriangle):
            raise TypeError(
                "Can only compare RightTriangle with another RightTriangle")
        return super().__lt__(other)

    def __str__(self) -> str:
        """String representation of the RightTriangle"""
        return f"RightTriangle(a={self.a}, b={self.b}, c={self.c})"

    def __repr__(self) -> str:
        """String representation of the RightTriangle"""
        return f"a={self.a}, b={self.b}, c={self.c}"


@total_ordering
class AcuteTriangle(Triangle):
    """AcuteTriangle class to represent a triangle with all angles less than 90 degrees"""

    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        """Initialize the AcuteTriangle with sides a, b, and c
        Args:
            a (float): length of side a
            b (float): length of side b
            c (float): length of side c
        Raises:
            ValueError: if sides don't form a valid triangle or if not all angles are acute
        """
        # Check triangle inequality
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Sides must satisfy triangle inequality")

        # Check that all angles are acute (using law of cosines)
        # For an acute triangle: a² + b² > c², a² + c² > b², b² + c² > a²
        if not (a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2):
            raise ValueError("All angles must be acute (less than 90 degrees)")

        super().__init__(a, b, c)

    def area(self) -> float:
        """Calculate the area of the triangle using Heron's formula"""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def circumradius(self) -> float:
        """Calculate the circumradius of the triangle"""
        return (self.a * self.b * self.c) / (4 * self.area())

    def altitude_a(self) -> float:
        """Calculate the altitude from vertex A to side a"""
        return 2 * self.area() / self.a

    def altitude_b(self) -> float:
        """Calculate the altitude from vertex B to side b"""
        return 2 * self.area() / self.b

    def altitude_c(self) -> float:
        """Calculate the altitude from vertex C to side c"""
        return 2 * self.area() / self.c

    def __imul__(self, scale: float) -> Self:
        """In-place scale the area of the triangle by a factor"""
        factor = math.sqrt(scale)
        self.a *= factor
        self.b *= factor
        self.c *= factor
        return self

    def __mul__(self, scale: int | float) -> "AcuteTriangle":
        """Scale the area of the triangle by a factor"""
        new = AcuteTriangle(self.a, self.b, self.c)
        new *= scale
        return new

    def __truediv__(self, scale: int | float) -> "AcuteTriangle":
        """Scale the area of the triangle down by a factor"""
        new = AcuteTriangle(self.a, self.b, self.c)
        new /= scale
        return new

    def __eq__(self, other) -> bool:
        """Equality comparison for AcuteTriangle"""
        if not isinstance(other, AcuteTriangle):
            raise TypeError(
                "Can only compare AcuteTriangle with another AcuteTriangle")
        return super().__eq__(other)

    def __lt__(self, other) -> bool:
        """Less-than comparison for AcuteTriangle based on area"""
        if not isinstance(other, AcuteTriangle):
            raise TypeError(
                "Can only compare AcuteTriangle with another AcuteTriangle")
        return super().__lt__(other)

    def __str__(self) -> str:
        """String representation of the AcuteTriangle"""
        return f"AcuteTriangle(a={self.a}, b={self.b}, c={self.c})"

    def __repr__(self) -> str:
        """String representation of the AcuteTriangle"""
        return f"a={self.a}, b={self.b}, c={self.c}"


@total_ordering
class ObtuseTriangle(Triangle):
    """ObtuseTriangle class to represent a triangle with one angle greater than 90 degrees"""

    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        """Initialize the ObtuseTriangle with sides a, b, and c
        Args:
            a (float): length of side a
            b (float): length of side b
            c (float): length of side c
        Raises:
            ValueError: if sides don't form a valid triangle or if no angle is obtuse
        """
        # Check triangle inequality
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Sides must satisfy triangle inequality")

        # Check that exactly one angle is obtuse (using law of cosines)
        # For an obtuse triangle: one of a² + b² < c², a² + c² < b², or b² + c² < a² must be true
        obtuse_count = sum([a**2 + b**2 < c**2, a**2 + c **
                           2 < b**2, b**2 + c**2 < a**2])
        if obtuse_count != 1:
            raise ValueError(
                "Exactly one angle must be obtuse (greater than 90 degrees)")

        super().__init__(a, b, c)

    def area(self) -> float:
        """Calculate the area of the triangle using Heron's formula"""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def circumradius(self) -> float:
        """Calculate the circumradius of the triangle"""
        return (self.a * self.b * self.c) / (4 * self.area())

    def altitude_a(self) -> float:
        """Calculate the altitude from vertex A to side a"""
        return 2 * self.area() / self.a

    def altitude_b(self) -> float:
        """Calculate the altitude from vertex B to side b"""
        return 2 * self.area() / self.b

    def altitude_c(self) -> float:
        """Calculate the altitude from vertex C to side c"""
        return 2 * self.area() / self.c

    def __imul__(self, scale: float) -> Self:
        """In-place scale the area of the triangle by a factor"""
        factor = math.sqrt(scale)
        self.a *= factor
        self.b *= factor
        self.c *= factor
        return self

    def __mul__(self, scale: int | float) -> "ObtuseTriangle":
        """Scale the area of the triangle by a factor"""
        new = ObtuseTriangle(self.a, self.b, self.c)
        new *= scale
        return new

    def __truediv__(self, scale: int | float) -> "ObtuseTriangle":
        """Scale the area of the triangle down by a factor"""
        new = ObtuseTriangle(self.a, self.b, self.c)
        new /= scale
        return new

    def __eq__(self, other) -> bool:
        """Equality comparison for ObtuseTriangle"""
        if not isinstance(other, ObtuseTriangle):
            raise TypeError(
                "Can only compare ObtuseTriangle with another ObtuseTriangle")
        return super().__eq__(other)

    def __lt__(self, other) -> bool:
        """Less-than comparison for ObtuseTriangle based on area"""
        if not isinstance(other, ObtuseTriangle):
            raise TypeError(
                "Can only compare ObtuseTriangle with another ObtuseTriangle")
        return super().__lt__(other)

    def __str__(self) -> str:
        """String representation of the ObtuseTriangle"""
        return f"ObtuseTriangle(a={self.a}, b={self.b}, c={self.c})"

    def __repr__(self) -> str:
        """String representation of the ObtuseTriangle"""
        return f"a={self.a}, b={self.b}, c={self.c}"
