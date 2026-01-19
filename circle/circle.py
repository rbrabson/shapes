""" Module to represent and calculate properties of circles """
from functools import total_ordering
from typing import Self
import math


@total_ordering
class Circle:
    """ Circle class to represent a circle with comprehensive geometric calculations """

    def __init__(self, radius: int | float) -> None:
        """ Initialize the Circle with a radius
            Args:
                radius (float): radius of the circle
            Raises:
                ValueError: if radius is not positive
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius: float = float(radius)

    def diameter(self) -> float:
        """ Calculate the diameter of the circle """
        return 2 * self.radius

    def circumference(self) -> float:
        """ Calculate the circumference of the circle """
        return 2 * math.pi * self.radius

    def area(self) -> float:
        """ Calculate the area of the circle """
        return math.pi * self.radius ** 2

    def arc_length(self, angle: float) -> float:
        """ Calculate the arc length for a given angle in radians
            Args:
                angle (float): angle in radians
        """
        return self.radius * angle

    def sector_area(self, angle: float) -> float:
        """ Calculate the area of a sector for a given angle in radians
            Args:
                angle (float): angle in radians
        """
        return 0.5 * self.radius ** 2 * angle

    def chord_length(self, angle: float) -> float:
        """ Calculate the length of a chord for a given central angle in radians
            Args:
                angle (float): central angle in radians
        """
        return 2 * self.radius * math.sin(angle / 2)

    def segment_area(self, angle: float) -> float:
        """ Calculate the area of a circular segment for a given angle in radians
            Args:
                angle (float): central angle in radians
        """
        return 0.5 * self.radius ** 2 * (angle - math.sin(angle))

    def __imul__(self, scale: float) -> Self:
        """ In-place scale the area of the circle by a factor """
        self.radius *= math.sqrt(scale)
        return self

    def __itruediv__(self, scale: int | float) -> Self:
        """ In-place scale the area of the circle down by a factor """
        self *= (1 / scale)
        return self

    def __mul__(self, scale: int | float) -> 'Circle':
        """ Scale the area of the circle by a factor """
        new = Circle(self.radius)
        new *= scale
        return new

    def __truediv__(self, scale: int | float) -> 'Circle':
        """ Scale the area of the circle down by a factor """
        new = Circle(self.radius)
        new /= scale
        return new

    def __eq__(self, other) -> bool:
        """ Equality comparison for Circle """
        if not isinstance(other, Circle):
            return NotImplemented
        return math.isclose(self.radius, other.radius)

    def __lt__(self, other) -> bool:
        """ Less-than comparison for Circle based on area """
        if not isinstance(other, Circle):
            return NotImplemented
        return self.area() < other.area()

    def __str__(self) -> str:
        """ String representation of the Circle """
        return f"Circle(radius={self.radius})"

    def __repr__(self) -> str:
        """ String representation of the Circle """
        return f"radius={self.radius}"
