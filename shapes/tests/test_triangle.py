"""Test cases for RightTriangle class"""
import math
from shapes.triangle import RightTriangle


class TestRightTriangleBasics:
    """Test basic initialization and properties"""

    def test_initialization(self):
        """Test triangle initialization"""
        triangle = RightTriangle(3, 4)
        assert triangle.a == 3
        assert triangle.b == 4
        assert triangle.c == 5

    def test_opposite(self):
        """Test opposite side"""
        triangle = RightTriangle(3, 4)
        assert triangle.opposite() == 3

    def test_adjacent(self):
        """Test adjacent side"""
        triangle = RightTriangle(3, 4)
        assert triangle.adjacent() == 4

    def test_hypotenuse(self):
        """Test hypotenuse calculation"""
        triangle = RightTriangle(3, 4)
        assert triangle.hypotenuse() == 5

    def test_hypotenuse_non_integer(self):
        """Test hypotenuse with non-integer result"""
        triangle = RightTriangle(1, 1)
        assert math.isclose(triangle.hypotenuse(), math.sqrt(2))


class TestRightTriangleGeometry:
    """Test geometric calculations"""

    def test_area(self):
        """Test area calculation"""
        triangle = RightTriangle(3, 4)
        assert triangle.area() == 6

    def test_perimeter(self):
        """Test perimeter calculation"""
        triangle = RightTriangle(3, 4)
        assert triangle.perimeter() == 12

    def test_inradius(self):
        """Test inradius calculation"""
        triangle = RightTriangle(3, 4)
        assert triangle.inradius() == 1

    def test_circumradius(self):
        """Test circumradius calculation"""
        triangle = RightTriangle(3, 4)
        assert triangle.circumradius() == 2.5

    def test_altitude(self):
        """Test altitude calculation"""
        triangle = RightTriangle(3, 4)
        assert triangle.altitude() == 2.4


class TestRightTriangleTrigonometry:
    """Test trigonometric functions"""

    def test_sin(self):
        """Test sine calculation"""
        triangle = RightTriangle(3, 4)
        assert triangle.sin() == 0.6

    def test_cos(self):
        """Test cosine calculation"""
        triangle = RightTriangle(3, 4)
        assert triangle.cos() == 0.8

    def test_tan(self):
        """Test tangent calculation"""
        triangle = RightTriangle(3, 4)
        assert triangle.tan() == 0.75

    def test_sec(self):
        """Test secant calculation"""
        triangle = RightTriangle(3, 4)
        assert triangle.sec() == 1.25

    def test_csc(self):
        """Test cosecant calculation"""
        triangle = RightTriangle(3, 4)
        assert math.isclose(triangle.csc(), 5/3)

    def test_cot(self):
        """Test cotangent calculation"""
        triangle = RightTriangle(3, 4)
        assert math.isclose(triangle.cot(), 4/3)

    def test_alpha(self):
        """Test alpha angle calculation"""
        triangle = RightTriangle(3, 4)
        expected = math.atan(3/4)
        assert math.isclose(triangle.alpha(), expected)

    def test_beta(self):
        """Test beta angle calculation"""
        triangle = RightTriangle(3, 4)
        expected = math.atan(4/3)
        assert math.isclose(triangle.beta(), expected)

    def test_angles_sum_to_90_degrees(self):
        """Test that alpha and beta sum to 90 degrees"""
        triangle = RightTriangle(3, 4)
        angle_sum = triangle.alpha() + triangle.beta()
        assert math.isclose(angle_sum, math.pi / 2)


class TestRightTriangleScaling:
    """Test scaling operations"""

    def test_multiply_scale_area(self):
        """Test multiplication scales area correctly"""
        triangle = RightTriangle(3, 4)
        original_area = triangle.area()
        scaled = triangle * 4
        assert math.isclose(scaled.area(), original_area * 4)

    def test_imul_scale_area(self):
        """Test in-place multiplication scales area correctly"""
        triangle = RightTriangle(3, 4)
        original_area = triangle.area()
        triangle *= 4
        assert math.isclose(triangle.area(), original_area * 4)

    def test_divide_scale_area(self):
        """Test division scales area correctly"""
        triangle = RightTriangle(3, 4)
        original_area = triangle.area()
        scaled = triangle / 4
        assert math.isclose(scaled.area(), original_area / 4)

    def test_itruediv_scale_area(self):
        """Test in-place division scales area correctly"""
        triangle = RightTriangle(3, 4)
        original_area = triangle.area()
        triangle /= 4
        assert math.isclose(triangle.area(), original_area / 4)

    def test_multiply_preserves_original(self):
        """Test that multiplication doesn't modify original triangle"""
        triangle = RightTriangle(3, 4)
        original_a = triangle.a
        original_b = triangle.b
        _ = triangle * 2
        assert triangle.a == original_a
        assert triangle.b == original_b

    def test_divide_preserves_original(self):
        """Test that division doesn't modify original triangle"""
        triangle = RightTriangle(3, 4)
        original_a = triangle.a
        original_b = triangle.b
        _ = triangle / 2
        assert triangle.a == original_a
        assert triangle.b == original_b

    def test_scaling_maintains_right_angle(self):
        """Test that scaling maintains right triangle properties"""
        triangle = RightTriangle(3, 4)
        triangle *= 2
        # Check Pythagorean theorem still holds
        assert math.isclose(triangle.a**2 + triangle.b**2, triangle.c**2)


class TestRightTriangleComparison:
    """Test comparison operations"""

    def test_equality_same_dimensions(self):
        """Test equality for triangles with same dimensions"""
        t1 = RightTriangle(3, 4)
        t2 = RightTriangle(3, 4)
        assert t1 == t2

    def test_inequality_different_dimensions(self):
        """Test inequality for triangles with different dimensions"""
        t1 = RightTriangle(3, 4)
        t2 = RightTriangle(5, 12)
        assert t1 != t2

    def test_less_than_by_area(self):
        """Test less-than comparison based on area"""
        t1 = RightTriangle(3, 4)  # area = 6
        t2 = RightTriangle(5, 12)  # area = 30
        assert t1 < t2

    def test_greater_than_by_area(self):
        """Test greater-than comparison based on area"""
        t1 = RightTriangle(5, 12)  # area = 30
        t2 = RightTriangle(3, 4)  # area = 6
        assert t1 > t2

    def test_less_than_or_equal(self):
        """Test less-than-or-equal comparison"""
        t1 = RightTriangle(3, 4)
        t2 = RightTriangle(3, 4)
        t3 = RightTriangle(5, 12)
        assert t1 <= t2
        assert t1 <= t3

    def test_greater_than_or_equal(self):
        """Test greater-than-or-equal comparison"""
        t1 = RightTriangle(3, 4)
        t2 = RightTriangle(3, 4)
        t3 = RightTriangle(1, 1)
        assert t1 >= t2
        assert t1 >= t3


class TestRightTriangleStringRepresentation:
    """Test string representations"""

    def test_str(self):
        """Test __str__ method"""
        triangle = RightTriangle(3, 4)
        assert str(triangle) == "RightTriangle(a=3, b=4, c=5.0)"

    def test_repr(self):
        """Test __repr__ method"""
        triangle = RightTriangle(3, 4)
        assert repr(triangle) == "3, 4, 5.0"


class TestRightTriangleEdgeCases:
    """Test edge cases and special scenarios"""

    def test_isosceles_right_triangle(self):
        """Test isosceles right triangle (45-45-90)"""
        triangle = RightTriangle(1, 1)
        assert math.isclose(triangle.hypotenuse(), math.sqrt(2))
        assert math.isclose(triangle.alpha(), math.pi / 4)
        assert math.isclose(triangle.beta(), math.pi / 4)

    def test_30_60_90_triangle(self):
        """Test 30-60-90 special right triangle"""
        triangle = RightTriangle(1, math.sqrt(3))
        assert math.isclose(triangle.hypotenuse(), 2)

    def test_small_values(self):
        """Test with very small values"""
        triangle = RightTriangle(0.001, 0.001)
        assert math.isclose(triangle.hypotenuse(), 0.001 * math.sqrt(2))
        assert math.isclose(triangle.area(), 0.0000005)

    def test_large_values(self):
        """Test with very large values"""
        triangle = RightTriangle(1e6, 1e6)
        assert math.isclose(triangle.hypotenuse(), 1e6 * math.sqrt(2))

    def test_multiple_scaling_operations(self):
        """Test multiple successive scaling operations"""
        triangle = RightTriangle(3, 4)
        original_area = triangle.area()
        triangle *= 2
        triangle *= 2
        triangle /= 2
        assert math.isclose(triangle.area(), original_area * 2)

    def test_pythagorean_theorem(self):
        """Test that Pythagorean theorem holds"""
        test_cases = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
        for a, b, expected_c in test_cases:
            triangle = RightTriangle(a, b)
            assert math.isclose(triangle.c, expected_c)
            assert math.isclose(triangle.a**2 + triangle.b**2, triangle.c**2)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
