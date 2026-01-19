"""Module to represent and calculate properties of rectangles"""

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
class Rectangle:
    """Rectangle class to represent a rectangle with comprehensive geometric calculations"""

    def __init__(self, width: int | float, height: int | float) -> None:
        """Initialize the Rectangle with width and height
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            ValueError: if width or height is not positive
        """
        if width <= 0:
            raise ValueError("Width must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self._width: float = float(width)
        self._height: float = float(height)

    def width(self) -> float:
        """Get the width of the rectangle"""
        return self._width

    def height(self) -> float:
        """Get the height of the rectangle"""
        return self._height

    def area(self) -> float:
        """Calculate the area of the rectangle"""
        return self._width * self._height

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle"""
        return 2 * (self._width + self._height)

    def diagonal(self) -> float:
        """Calculate the diagonal length of the rectangle"""
        return math.sqrt(self._width**2 + self._height**2)

    def aspect_ratio(self) -> float:
        """Calculate the aspect ratio (width / height) of the rectangle"""
        return self._width / self._height

    def is_square(self) -> bool:
        """Check if the rectangle is a square"""
        return math.isclose(self._width, self._height)

    def circumradius(self) -> float:
        """Calculate the circumradius (radius of circumscribed circle)"""
        return self.diagonal() / 2

    def inradius(self) -> float:
        """Calculate the inradius (radius of largest inscribed circle)"""
        return min(self._width, self._height) / 2

    def angle_diagonal(self) -> float:
        """Calculate the angle between the diagonal and width in radians"""
        return math.atan(self._height / self._width)

    def scale_to_area(self, target_area: int | float) -> "Rectangle":
        """Create a new rectangle with the same aspect ratio scaled to a target area
        Args:
            target_area: desired area of the new rectangle
        Returns:
            New Rectangle with same aspect ratio and specified area
        """
        scale_factor = math.sqrt(target_area / self.area())
        return Rectangle(self._width * scale_factor, self._height * scale_factor)

    def scale_to_fit(self, max_width: int | float, max_height: int | float) -> "Rectangle":
        """Create a new rectangle scaled to fit within given dimensions maintaining aspect ratio
        Args:
            max_width: maximum width constraint
            max_height: maximum height constraint
        Returns:
            New Rectangle that fits within constraints
        """
        width_scale = max_width / self._width
        height_scale = max_height / self._height
        scale = min(width_scale, height_scale)
        return Rectangle(self._width * scale, self._height * scale)

    def rotate_90(self) -> "Rectangle":
        """Create a new rectangle rotated 90 degrees (swap width and height)"""
        return Rectangle(self._height, self._width)

    def __imul__(self, scale: int | float) -> Self:
        """In-place scale the area of the rectangle by a factor"""
        scale_factor = math.sqrt(scale)
        self._width *= scale_factor
        self._height *= scale_factor
        return self

    def __itruediv__(self, scale: int | float) -> Self:
        """In-place scale the area of the rectangle down by a factor"""
        self *= 1 / scale  # type: ignore[assignment]
        return self

    def __mul__(self, scale: int | float) -> "Rectangle":
        """Scale the area of the rectangle by a factor"""
        new = Rectangle(self._width, self._height)
        new *= scale
        return new

    def __truediv__(self, scale: int | float) -> "Rectangle":
        """Scale the area of the rectangle down by a factor"""
        new = Rectangle(self._width, self._height)
        new /= scale
        return new

    def __eq__(self, other: object) -> bool:
        """Equality comparison for Rectangle"""
        if not isinstance(other, Rectangle):
            raise TypeError("Can only compare Rectangle with another Rectangle")
        return math.isclose(self._width, other.width()) and math.isclose(
            self._height, other.height()
        )

    def __lt__(self, other: object) -> bool:
        """Less-than comparison for Rectangle based on area"""
        if not isinstance(other, Rectangle):
            raise TypeError("Can only compare Rectangle with another Rectangle")
        # Use a small threshold for floating point comparison
        # to avoid issues with numerically equal areas
        area_diff = self.area() - other.area()
        if abs(area_diff) < 1e-9:  # Areas are essentially equal
            return False
        return area_diff < 0

    def __str__(self) -> str:
        """String representation of the Rectangle"""
        return f"Rectangle(width={self._width}, height={self._height})"

    def __repr__(self) -> str:
        """String representation of the Rectangle"""
        return f"width={self._width}, height={self._height}"


@total_ordering
class Square(Rectangle):
    """Square class to represent a square (special case of rectangle)"""

    def __init__(self, side: int | float) -> None:
        """Initialize the Square with a side length
        Args:
            side: side length of the square
        Raises:
            ValueError: if side is not positive
        """
        super().__init__(side, side)
        self._side: float = float(side)

    def side(self) -> float:
        """Get the side length of the square"""
        return self._side

    def diagonal(self) -> float:
        """Calculate the diagonal length of the square"""
        return self._side * math.sqrt(2)

    def circumradius(self) -> float:
        """Calculate the circumradius (radius of circumscribed circle)"""
        return self._side * math.sqrt(2) / 2

    def inradius(self) -> float:
        """Calculate the inradius (radius of inscribed circle)"""
        return self._side / 2

    def apothem(self) -> float:
        """Calculate the apothem (distance from center to midpoint of a side)"""
        return self._side / 2

    def __imul__(self, scale: int | float) -> Self:
        """In-place scale the area of the square by a factor"""
        self._side *= math.sqrt(scale)
        self._width = self._side
        self._height = self._side
        return self

    def __mul__(self, scale: int | float) -> "Square":
        """Scale the area of the square by a factor"""
        new = Square(self._side)
        new *= scale
        return new

    def __truediv__(self, scale: int | float) -> "Square":
        """Scale the area of the square down by a factor"""
        new = Square(self._side)
        new /= scale
        return new

    def __str__(self) -> str:
        """String representation of the Square"""
        return f"Square(side={self._side})"

    def __repr__(self) -> str:
        """String representation of the Square"""
        return f"side={self._side}"
