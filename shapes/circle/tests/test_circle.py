"""Test cases for Circle class"""

import math

import pytest

from shapes import Circle


class TestCircleBasics:
    """Test basic initialization and properties"""

    def test_initialization(self):
        """Test circle initialization"""
        circle = Circle(5)
        assert circle.radius() == 5

    def test_initialization_float(self):
        """Test circle initialization with float"""
        circle = Circle(3.5)
        assert circle.radius() == 3.5

    def test_initialization_negative_radius(self):
        """Test that negative radius raises ValueError"""
        with pytest.raises(ValueError):
            Circle(-5)

    def test_initialization_zero_radius(self):
        """Test that zero radius raises ValueError"""
        with pytest.raises(ValueError):
            Circle(0)

    def test_diameter(self):
        """Test diameter calculation"""
        circle = Circle(5)
        assert circle.diameter() == 10

    def test_diameter_float(self):
        """Test diameter calculation with float radius"""
        circle = Circle(3.5)
        assert circle.diameter() == 7.0


class TestCircleGeometry:
    """Test geometric calculations"""

    def test_circumference(self):
        """Test circumference calculation"""
        circle = Circle(1)
        assert math.isclose(circle.circumference(), 2 * math.pi)

    def test_circumference_radius_5(self):
        """Test circumference with radius 5"""
        circle = Circle(5)
        assert math.isclose(circle.circumference(), 10 * math.pi)

    def test_area(self):
        """Test area calculation"""
        circle = Circle(1)
        assert math.isclose(circle.area(), math.pi)

    def test_area_radius_5(self):
        """Test area with radius 5"""
        circle = Circle(5)
        assert math.isclose(circle.area(), 25 * math.pi)

    def test_arc_length(self):
        """Test arc length calculation"""
        circle = Circle(5)
        # Arc length for pi/2 radians (quarter circle)
        assert math.isclose(circle.arc_length(math.pi / 2), 5 * math.pi / 2)

    def test_arc_length_full_circle(self):
        """Test arc length for full circle"""
        circle = Circle(3)
        assert math.isclose(circle.arc_length(2 * math.pi), circle.circumference())

    def test_sector_area(self):
        """Test sector area calculation"""
        circle = Circle(4)
        # Sector area for pi/2 radians (quarter circle)
        assert math.isclose(circle.sector_area(math.pi / 2), 0.5 * 16 * math.pi / 2)

    def test_sector_area_full_circle(self):
        """Test sector area for full circle"""
        circle = Circle(5)
        assert math.isclose(circle.sector_area(2 * math.pi), circle.area())

    def test_chord_length(self):
        """Test chord length calculation"""
        circle = Circle(5)
        # Chord length for pi radians (diameter)
        assert math.isclose(circle.chord_length(math.pi), 10)

    def test_chord_length_right_angle(self):
        """Test chord length for right angle"""
        circle = Circle(1)
        # Chord length for pi/2 radians
        assert math.isclose(circle.chord_length(math.pi / 2), math.sqrt(2))

    def test_segment_area(self):
        """Test segment area calculation"""
        circle = Circle(5)
        # Segment area for pi/2 radians
        angle = math.pi / 2
        expected = 0.5 * 25 * (angle - math.sin(angle))
        assert math.isclose(circle.segment_area(angle), expected)

    def test_segment_area_semicircle(self):
        """Test segment area for semicircle"""
        circle = Circle(3)
        # For pi radians, segment is half the circle
        segment = circle.segment_area(math.pi)
        assert math.isclose(segment, circle.area() / 2)


class TestCircleScaling:
    """Test scaling operations"""

    def test_multiply_by_2(self):
        """Test scaling area by 2"""
        circle = Circle(5)
        scaled = circle * 2
        assert math.isclose(scaled.area(), circle.area() * 2)

    def test_multiply_by_4(self):
        """Test scaling area by 4"""
        circle = Circle(3)
        scaled = circle * 4
        assert math.isclose(scaled.radius(), 6)
        assert math.isclose(scaled.area(), circle.area() * 4)

    def test_divide_by_2(self):
        """Test scaling area down by 2"""
        circle = Circle(10)
        scaled = circle / 2
        assert math.isclose(scaled.area(), circle.area() / 2)

    def test_divide_by_4(self):
        """Test scaling area down by 4"""
        circle = Circle(8)
        scaled = circle / 4
        assert math.isclose(scaled.radius(), 4)
        assert math.isclose(scaled.area(), circle.area() / 4)

    def test_inplace_multiply(self):
        """Test in-place multiplication"""
        circle = Circle(5)
        original_area = circle.area()
        circle *= 2
        assert math.isclose(circle.area(), original_area * 2)

    def test_inplace_divide(self):
        """Test in-place division"""
        circle = Circle(10)
        original_area = circle.area()
        circle /= 2
        assert math.isclose(circle.area(), original_area / 2)

    def test_scaling_preserves_type(self):
        """Test that scaling returns Circle instance"""
        circle = Circle(5)
        scaled = circle * 2
        assert isinstance(scaled, Circle)


class TestCircleComparison:
    """Test comparison operations"""

    def test_equality_same_radius(self):
        """Test equality for circles with same radius"""
        circle1 = Circle(5)
        circle2 = Circle(5)
        assert circle1 == circle2

    def test_equality_different_radius(self):
        """Test inequality for circles with different radii"""
        circle1 = Circle(5)
        circle2 = Circle(6)
        assert circle1 != circle2

    def test_less_than(self):
        """Test less-than comparison"""
        circle1 = Circle(3)
        circle2 = Circle(5)
        assert circle1 < circle2

    def test_less_than_equal(self):
        """Test less-than-or-equal comparison"""
        circle1 = Circle(3)
        circle2 = Circle(5)
        circle3 = Circle(3)
        assert circle1 <= circle2
        assert circle1 <= circle3

    def test_greater_than(self):
        """Test greater-than comparison"""
        circle1 = Circle(5)
        circle2 = Circle(3)
        assert circle1 > circle2

    def test_greater_than_equal(self):
        """Test greater-than-or-equal comparison"""
        circle1 = Circle(5)
        circle2 = Circle(3)
        circle3 = Circle(5)
        assert circle1 >= circle2
        assert circle1 >= circle3

    def test_comparison_based_on_area(self):
        """Test that comparison is based on area, not radius"""
        circle1 = Circle(5)
        circle2 = Circle(5)
        assert circle1 >= circle2
        assert circle1 <= circle2


class TestCircleStringRepresentation:
    """Test string representations"""

    def test_str_representation(self):
        """Test __str__ method"""
        circle = Circle(5)
        assert str(circle) == "Circle(radius=5.0)"

    def test_repr_representation(self):
        """Test __repr__ method"""
        circle = Circle(5)
        assert repr(circle) == "radius=5.0"

    def test_str_with_float_radius(self):
        """Test __str__ with float radius"""
        circle = Circle(3.5)
        assert str(circle) == "Circle(radius=3.5)"


class TestCircleEdgeCases:
    """Test edge cases and special scenarios"""

    def test_very_small_radius(self):
        """Test circle with very small radius"""
        circle = Circle(0.001)
        assert circle.radius() == 0.001
        assert circle.area() > 0

    def test_very_large_radius(self):
        """Test circle with very large radius"""
        circle = Circle(1e6)
        assert circle.radius() == 1e6
        assert circle.area() > 0

    def test_scaling_chain(self):
        """Test chaining multiple scaling operations"""
        circle = Circle(2)
        scaled = circle * 4 / 2
        assert math.isclose(scaled.area(), circle.area() * 2)

    def test_inplace_scaling_chain(self):
        """Test chaining multiple in-place scaling operations"""
        circle = Circle(2)
        original_area = circle.area()
        circle *= 4
        circle /= 2
        assert math.isclose(circle.area(), original_area * 2)

    def test_comparison_with_scaled_circle(self):
        """Test comparison with scaled circle"""
        circle1 = Circle(5)
        circle2 = Circle(5)
        circle2 *= 2
        assert circle1 < circle2

    def test_arc_length_zero_angle(self):
        """Test arc length with zero angle"""
        circle = Circle(5)
        assert circle.arc_length(0) == 0

    def test_sector_area_zero_angle(self):
        """Test sector area with zero angle"""
        circle = Circle(5)
        assert circle.sector_area(0) == 0

    def test_chord_length_zero_angle(self):
        """Test chord length with zero angle"""
        circle = Circle(5)
        assert math.isclose(circle.chord_length(0), 0)

    def test_segment_area_zero_angle(self):
        """Test segment area with zero angle"""
        circle = Circle(5)
        assert math.isclose(circle.segment_area(0), 0)
