"""Module to represent and calculate properties of circles"""

import math
from functools import total_ordering
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self
else:
    try:
        from typing import Self
    except ImportError:
        from typing_extensions import Self


@total_ordering
class Circle:
    """Circle class to represent a circle with comprehensive geometric calculations"""

    def __init__(self, radius: int | float) -> None:
        """Initialize the Circle with a radius
        Args:
            radius: radius of the circle
        Raises:
            ValueError: if radius is not positive
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self._radius: float = float(radius)

    def radius(self) -> float:
        """Get the radius of the circle"""
        return self._radius

    def diameter(self) -> float:
        """Calculate the diameter of the circle"""
        return 2 * self._radius

    def circumference(self) -> float:
        """Calculate the circumference of the circle"""
        return 2 * math.pi * self._radius

    def area(self) -> float:
        """Calculate the area of the circle"""
        return math.pi * self._radius**2

    def arc_length(self, angle: int | float) -> float:
        """Calculate the arc length for a given angle in radians
        Args:
            angle: angle in radians
        """
        return self._radius * float(angle)

    def sector_area(self, angle: int | float) -> float:
        """Calculate the area of a sector for a given angle in radians
        Args:
            angle: angle in radians
        """
        return 0.5 * self._radius**2 * float(angle)

    def chord_length(self, angle: int | float) -> float:
        """Calculate the length of a chord for a given central angle in radians
        Args:
            angle: central angle in radians
        """
        return 2 * self._radius * math.sin(float(angle) / 2)

    def segment_area(self, angle: int | float) -> float:
        """Calculate the area of a circular segment for a given angle in radians
        Args:
            angle: central angle in radians
        """
        return 0.5 * self._radius**2 * (float(angle) - math.sin(float(angle)))

    def __imul__(self, scale: int | float) -> Self:
        """In-place scale the area of the circle by a factor"""
        self._radius *= math.sqrt(scale)
        return self

    def __itruediv__(self, scale: int | float) -> Self:
        """In-place scale the area of the circle down by a factor"""
        self *= 1 / scale  # type: ignore[assignment]
        return self

    def __mul__(self, scale: int | float) -> "Circle":
        """Scale the area of the circle by a factor"""
        new = Circle(self._radius)
        new *= scale
        return new

    def __truediv__(self, scale: int | float) -> "Circle":
        """Scale the area of the circle down by a factor"""
        new = Circle(self._radius)
        new /= scale
        return new

    def __eq__(self, other: object) -> bool:
        """Equality comparison for Circle"""
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with another Circle")
        return math.isclose(self._radius, other.radius())

    def __lt__(self, other: object) -> bool:
        """Less-than comparison for Circle based on area"""
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with another Circle")
        return self.area() < other.area()

    def __str__(self) -> str:
        """String representation of the Circle"""
        return f"Circle(radius={self._radius})"

    def __repr__(self) -> str:
        """String representation of the Circle"""
        return f"radius={self._radius}"
