"""Test cases for Rectangle and Square classes"""

import math

import pytest

from shapes.rectangle.rectangle import Rectangle, Square


class TestRectangleBasics:
    """Test basic initialization and properties"""

    def test_initialization(self):
        """Test rectangle initialization"""
        rect = Rectangle(4, 6)
        assert rect.width() == 4
        assert rect.height() == 6

    def test_initialization_float(self):
        """Test rectangle initialization with floats"""
        rect = Rectangle(3.5, 7.2)
        assert rect.width() == 3.5
        assert rect.height() == 7.2

    def test_initialization_negative_width(self):
        """Test that negative width raises ValueError"""
        with pytest.raises(ValueError):
            Rectangle(-5, 10)

    def test_initialization_negative_height(self):
        """Test that negative height raises ValueError"""
        with pytest.raises(ValueError):
            Rectangle(5, -10)

    def test_initialization_zero_width(self):
        """Test that zero width raises ValueError"""
        with pytest.raises(ValueError):
            Rectangle(0, 10)

    def test_initialization_zero_height(self):
        """Test that zero height raises ValueError"""
        with pytest.raises(ValueError):
            Rectangle(5, 0)

    def test_area(self):
        """Test area calculation"""
        rect = Rectangle(4, 6)
        assert rect.area() == 24

    def test_area_float(self):
        """Test area calculation with float dimensions"""
        rect = Rectangle(3.5, 2.0)
        assert math.isclose(rect.area(), 7.0)

    def test_perimeter(self):
        """Test perimeter calculation"""
        rect = Rectangle(4, 6)
        assert rect.perimeter() == 20

    def test_perimeter_float(self):
        """Test perimeter calculation with float dimensions"""
        rect = Rectangle(3.5, 4.5)
        assert math.isclose(rect.perimeter(), 16.0)


class TestRectangleGeometry:
    """Test geometric calculations"""

    def test_diagonal(self):
        """Test diagonal calculation"""
        rect = Rectangle(3, 4)
        assert math.isclose(rect.diagonal(), 5)

    def test_diagonal_square(self):
        """Test diagonal of square"""
        rect = Rectangle(5, 5)
        assert math.isclose(rect.diagonal(), 5 * math.sqrt(2))

    def test_aspect_ratio(self):
        """Test aspect ratio calculation"""
        rect = Rectangle(16, 9)
        assert math.isclose(rect.aspect_ratio(), 16 / 9)

    def test_aspect_ratio_square(self):
        """Test aspect ratio of square"""
        rect = Rectangle(5, 5)
        assert math.isclose(rect.aspect_ratio(), 1.0)

    def test_is_square_true(self):
        """Test is_square returns True for square"""
        rect = Rectangle(5, 5)
        assert rect.is_square() is True

    def test_is_square_false(self):
        """Test is_square returns False for non-square"""
        rect = Rectangle(4, 6)
        assert rect.is_square() is False

    def test_is_square_close_values(self):
        """Test is_square with very close values"""
        rect = Rectangle(5.0, 5.0000000001)
        assert rect.is_square() is True

    def test_circumradius(self):
        """Test circumradius calculation"""
        rect = Rectangle(3, 4)
        assert math.isclose(rect.circumradius(), 2.5)

    def test_circumradius_square(self):
        """Test circumradius of square"""
        rect = Rectangle(4, 4)
        assert math.isclose(rect.circumradius(), 2 * math.sqrt(2))

    def test_inradius(self):
        """Test inradius calculation"""
        rect = Rectangle(6, 8)
        assert math.isclose(rect.inradius(), 3)

    def test_inradius_square(self):
        """Test inradius of square"""
        rect = Rectangle(10, 10)
        assert math.isclose(rect.inradius(), 5)

    def test_angle_diagonal(self):
        """Test angle between diagonal and width"""
        rect = Rectangle(1, 1)
        assert math.isclose(rect.angle_diagonal(), math.pi / 4)

    def test_angle_diagonal_3_4_5(self):
        """Test angle diagonal for 3-4-5 triangle"""
        rect = Rectangle(3, 4)
        assert math.isclose(rect.angle_diagonal(), math.atan(4 / 3))


class TestRectangleTransformations:
    """Test transformation methods"""

    def test_scale_to_area(self):
        """Test scaling to specific area"""
        rect = Rectangle(4, 6)
        scaled = rect.scale_to_area(48)
        assert math.isclose(scaled.area(), 48)
        assert math.isclose(scaled.aspect_ratio(), rect.aspect_ratio())

    def test_scale_to_area_double(self):
        """Test scaling area to double"""
        rect = Rectangle(3, 4)
        scaled = rect.scale_to_area(24)
        assert math.isclose(scaled.area(), 24)
        assert math.isclose(scaled.width(), 3 * math.sqrt(2))

    def test_scale_to_fit_width_constraint(self):
        """Test scale to fit with width as limiting factor"""
        rect = Rectangle(100, 50)
        fitted = rect.scale_to_fit(50, 100)
        assert math.isclose(fitted.width(), 50)
        assert math.isclose(fitted.height(), 25)

    def test_scale_to_fit_height_constraint(self):
        """Test scale to fit with height as limiting factor"""
        rect = Rectangle(50, 100)
        fitted = rect.scale_to_fit(100, 50)
        assert math.isclose(fitted.width(), 25)
        assert math.isclose(fitted.height(), 50)

    def test_scale_to_fit_already_fits(self):
        """Test scale to fit when already fits"""
        rect = Rectangle(30, 40)
        fitted = rect.scale_to_fit(100, 100)
        assert fitted.width() > rect.width()
        assert fitted.height() > rect.height()

    def test_rotate_90(self):
        """Test 90-degree rotation"""
        rect = Rectangle(4, 6)
        rotated = rect.rotate_90()
        assert rotated.width() == 6
        assert rotated.height() == 4

    def test_rotate_90_square(self):
        """Test 90-degree rotation of square"""
        rect = Rectangle(5, 5)
        rotated = rect.rotate_90()
        assert rotated.width() == 5
        assert rotated.height() == 5


class TestRectangleScaling:
    """Test scaling operations"""

    def test_multiply_by_2(self):
        """Test scaling area by 2"""
        rect = Rectangle(4, 6)
        scaled = rect * 2
        assert math.isclose(scaled.area(), rect.area() * 2)

    def test_multiply_by_4(self):
        """Test scaling area by 4"""
        rect = Rectangle(3, 5)
        scaled = rect * 4
        assert math.isclose(scaled.area(), rect.area() * 4)
        assert math.isclose(scaled.width(), 6)
        assert math.isclose(scaled.height(), 10)

    def test_divide_by_2(self):
        """Test scaling area down by 2"""
        rect = Rectangle(10, 20)
        scaled = rect / 2
        assert math.isclose(scaled.area(), rect.area() / 2)

    def test_divide_by_4(self):
        """Test scaling area down by 4"""
        rect = Rectangle(8, 12)
        scaled = rect / 4
        assert math.isclose(scaled.area(), rect.area() / 4)
        assert math.isclose(scaled.width(), 4)
        assert math.isclose(scaled.height(), 6)

    def test_inplace_multiply(self):
        """Test in-place multiplication"""
        rect = Rectangle(5, 10)
        original_area = rect.area()
        rect *= 2
        assert math.isclose(rect.area(), original_area * 2)

    def test_inplace_divide(self):
        """Test in-place division"""
        rect = Rectangle(10, 20)
        original_area = rect.area()
        rect /= 2
        assert math.isclose(rect.area(), original_area / 2)

    def test_scaling_preserves_type(self):
        """Test that scaling returns Rectangle instance"""
        rect = Rectangle(5, 10)
        scaled = rect * 2
        assert isinstance(scaled, Rectangle)

    def test_scaling_preserves_aspect_ratio(self):
        """Test that scaling preserves aspect ratio"""
        rect = Rectangle(4, 6)
        scaled = rect * 2
        assert math.isclose(scaled.aspect_ratio(), rect.aspect_ratio())


class TestRectangleComparison:
    """Test comparison operations"""

    def test_equality_same_dimensions(self):
        """Test equality for rectangles with same dimensions"""
        rect1 = Rectangle(5, 10)
        rect2 = Rectangle(5, 10)
        assert rect1 == rect2

    def test_equality_different_dimensions(self):
        """Test inequality for rectangles with different dimensions"""
        rect1 = Rectangle(5, 10)
        rect2 = Rectangle(6, 10)
        assert rect1 != rect2

    def test_equality_swapped_dimensions(self):
        """Test that swapped dimensions are not equal"""
        rect1 = Rectangle(5, 10)
        rect2 = Rectangle(10, 5)
        assert rect1 != rect2

    def test_less_than(self):
        """Test less-than comparison"""
        rect1 = Rectangle(3, 4)
        rect2 = Rectangle(5, 6)
        assert rect1 < rect2

    def test_less_than_equal(self):
        """Test less-than-or-equal comparison"""
        rect1 = Rectangle(3, 4)
        rect2 = Rectangle(5, 6)
        rect3 = Rectangle(3, 4)
        assert rect1 <= rect2
        assert rect1 <= rect3

    def test_greater_than(self):
        """Test greater-than comparison"""
        rect1 = Rectangle(5, 6)
        rect2 = Rectangle(3, 4)
        assert rect1 > rect2

    def test_greater_than_equal(self):
        """Test greater-than-or-equal comparison"""
        rect1 = Rectangle(5, 6)
        rect2 = Rectangle(3, 4)
        rect3 = Rectangle(5, 6)
        assert rect1 >= rect2
        assert rect1 >= rect3

    def test_comparison_based_on_area(self):
        """Test that comparison is based on area"""
        rect1 = Rectangle(4, 6)  # area = 24
        rect2 = Rectangle(3, 8)  # area = 24
        # Same area, so neither should be strictly less than the other
        assert rect1 >= rect2
        assert rect2 >= rect1

    def test_comparison_with_non_rectangle_raises_error(self):
        """Test comparison with non-rectangle raises TypeError"""
        rect = Rectangle(5, 10)
        with pytest.raises(TypeError):
            _ = rect == 5

    def test_less_than_with_non_rectangle_raises_error(self):
        """Test less-than with non-rectangle raises TypeError"""
        rect = Rectangle(5, 10)
        with pytest.raises(TypeError):
            _ = rect < 5


class TestRectangleStringRepresentation:
    """Test string representations"""

    def test_str_representation(self):
        """Test __str__ method"""
        rect = Rectangle(5, 10)
        assert str(rect) == "Rectangle(width=5.0, height=10.0)"

    def test_repr_representation(self):
        """Test __repr__ method"""
        rect = Rectangle(5, 10)
        assert repr(rect) == "width=5.0, height=10.0"

    def test_str_with_float_dimensions(self):
        """Test __str__ with float dimensions"""
        rect = Rectangle(3.5, 7.2)
        assert str(rect) == "Rectangle(width=3.5, height=7.2)"


class TestRectangleEdgeCases:
    """Test edge cases and special scenarios"""

    def test_very_small_dimensions(self):
        """Test rectangle with very small dimensions"""
        rect = Rectangle(0.001, 0.002)
        assert rect.width() == 0.001
        assert rect.height() == 0.002
        assert rect.area() > 0

    def test_very_large_dimensions(self):
        """Test rectangle with very large dimensions"""
        rect = Rectangle(1e6, 1e6)
        assert rect.width() == 1e6
        assert rect.height() == 1e6
        assert rect.area() > 0

    def test_scaling_chain(self):
        """Test chaining multiple scaling operations"""
        rect = Rectangle(2, 3)
        scaled = rect * 4 / 2
        assert math.isclose(scaled.area(), rect.area() * 2)

    def test_inplace_scaling_chain(self):
        """Test chaining multiple in-place scaling operations"""
        rect = Rectangle(2, 3)
        original_area = rect.area()
        rect *= 4
        rect /= 2
        assert math.isclose(rect.area(), original_area * 2)

    def test_comparison_with_scaled_rectangle(self):
        """Test comparison with scaled rectangle"""
        rect1 = Rectangle(5, 10)
        rect2 = Rectangle(5, 10)
        rect2 *= 2
        assert rect1 < rect2

    def test_extreme_aspect_ratio(self):
        """Test rectangle with extreme aspect ratio"""
        rect = Rectangle(100, 1)
        assert math.isclose(rect.aspect_ratio(), 100)
        assert rect.is_square() is False


# Square Tests


class TestSquareBasics:
    """Test basic initialization and properties of Square"""

    def test_initialization(self):
        """Test square initialization"""
        square = Square(5)
        assert square.side() == 5
        assert square.width() == 5
        assert square.height() == 5

    def test_initialization_float(self):
        """Test square initialization with float"""
        square = Square(3.5)
        assert square.side() == 3.5

    def test_initialization_negative_side(self):
        """Test that negative side raises ValueError"""
        with pytest.raises(ValueError):
            Square(-5)

    def test_initialization_zero_side(self):
        """Test that zero side raises ValueError"""
        with pytest.raises(ValueError):
            Square(0)

    def test_area(self):
        """Test area calculation"""
        square = Square(5)
        assert square.area() == 25

    def test_perimeter(self):
        """Test perimeter calculation"""
        square = Square(5)
        assert square.perimeter() == 20

    def test_is_square(self):
        """Test that Square is identified as square"""
        square = Square(5)
        assert square.is_square() is True


class TestSquareGeometry:
    """Test geometric calculations for Square"""

    def test_diagonal(self):
        """Test diagonal calculation"""
        square = Square(5)
        assert math.isclose(square.diagonal(), 5 * math.sqrt(2))

    def test_diagonal_unit_square(self):
        """Test diagonal of unit square"""
        square = Square(1)
        assert math.isclose(square.diagonal(), math.sqrt(2))

    def test_circumradius(self):
        """Test circumradius calculation"""
        square = Square(4)
        assert math.isclose(square.circumradius(), 2 * math.sqrt(2))

    def test_inradius(self):
        """Test inradius calculation"""
        square = Square(10)
        assert math.isclose(square.inradius(), 5)

    def test_apothem(self):
        """Test apothem calculation"""
        square = Square(8)
        assert math.isclose(square.apothem(), 4)

    def test_aspect_ratio(self):
        """Test aspect ratio is always 1"""
        square = Square(7)
        assert math.isclose(square.aspect_ratio(), 1.0)

    def test_angle_diagonal(self):
        """Test angle diagonal is always 45 degrees"""
        square = Square(5)
        assert math.isclose(square.angle_diagonal(), math.pi / 4)


class TestSquareScaling:
    """Test scaling operations for Square"""

    def test_multiply_by_2(self):
        """Test scaling area by 2"""
        square = Square(5)
        scaled = square * 2
        assert math.isclose(scaled.area(), square.area() * 2)

    def test_multiply_by_4(self):
        """Test scaling area by 4"""
        square = Square(3)
        scaled = square * 4
        assert math.isclose(scaled.side(), 6)
        assert math.isclose(scaled.area(), square.area() * 4)

    def test_divide_by_2(self):
        """Test scaling area down by 2"""
        square = Square(10)
        scaled = square / 2
        assert math.isclose(scaled.area(), square.area() / 2)

    def test_divide_by_4(self):
        """Test scaling area down by 4"""
        square = Square(8)
        scaled = square / 4
        assert math.isclose(scaled.side(), 4)
        assert math.isclose(scaled.area(), square.area() / 4)

    def test_inplace_multiply(self):
        """Test in-place multiplication"""
        square = Square(5)
        original_area = square.area()
        square *= 2
        assert math.isclose(square.area(), original_area * 2)
        assert math.isclose(square.side(), 5 * math.sqrt(2))

    def test_inplace_divide(self):
        """Test in-place division"""
        square = Square(10)
        original_area = square.area()
        square /= 2
        assert math.isclose(square.area(), original_area / 2)

    def test_scaling_preserves_type(self):
        """Test that scaling returns Square instance"""
        square = Square(5)
        scaled = square * 2
        assert isinstance(scaled, Square)

    def test_scaled_remains_square(self):
        """Test that scaled square remains square"""
        square = Square(5)
        scaled = square * 3
        assert scaled.is_square() is True


class TestSquareComparison:
    """Test comparison operations for Square"""

    def test_equality_same_side(self):
        """Test equality for squares with same side"""
        square1 = Square(5)
        square2 = Square(5)
        assert square1 == square2

    def test_equality_different_side(self):
        """Test inequality for squares with different sides"""
        square1 = Square(5)
        square2 = Square(6)
        assert square1 != square2

    def test_less_than(self):
        """Test less-than comparison"""
        square1 = Square(3)
        square2 = Square(5)
        assert square1 < square2

    def test_greater_than(self):
        """Test greater-than comparison"""
        square1 = Square(5)
        square2 = Square(3)
        assert square1 > square2

    def test_square_vs_rectangle_same_area(self):
        """Test comparison between square and rectangle with same area"""
        square = Square(4)  # area = 16
        rect = Rectangle(2, 8)  # area = 16
        # Both have area of 16, so their areas are equal
        assert math.isclose(square.area(), rect.area())
        # Neither is strictly less than the other when areas are equal
        assert square >= rect


class TestSquareStringRepresentation:
    """Test string representations for Square"""

    def test_str_representation(self):
        """Test __str__ method"""
        square = Square(5)
        assert str(square) == "Square(side=5.0)"

    def test_repr_representation(self):
        """Test __repr__ method"""
        square = Square(5)
        assert repr(square) == "side=5.0"

    def test_str_with_float_side(self):
        """Test __str__ with float side"""
        square = Square(3.5)
        assert str(square) == "Square(side=3.5)"


class TestSquareEdgeCases:
    """Test edge cases and special scenarios for Square"""

    def test_very_small_side(self):
        """Test square with very small side"""
        square = Square(0.001)
        assert square.side() == 0.001
        assert square.area() > 0

    def test_very_large_side(self):
        """Test square with very large side"""
        square = Square(1e6)
        assert square.side() == 1e6
        assert square.area() > 0

    def test_scaling_chain(self):
        """Test chaining multiple scaling operations"""
        square = Square(2)
        scaled = square * 4 / 2
        assert math.isclose(scaled.area(), square.area() * 2)

    def test_inplace_scaling_chain(self):
        """Test chaining multiple in-place scaling operations"""
        square = Square(2)
        original_area = square.area()
        square *= 4
        square /= 2
        assert math.isclose(square.area(), original_area * 2)

    def test_rotate_90_square(self):
        """Test that rotating square gives same square"""
        square = Square(5)
        rotated = square.rotate_90()
        assert rotated.width() == 5
        assert rotated.height() == 5
        assert rotated.area() == square.area()
