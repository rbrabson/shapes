"""Test cases for Triangle classes"""
import math
import pytest
from triangles import RightTriangle, AcuteTriangle, ObtuseTriangle


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
        assert repr(triangle) == "a=3, b=4, c=5.0"


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


class TestAcuteTriangleBasics:
    """Test basic initialization and properties"""

    def test_initialization(self):
        """Test acute triangle initialization"""
        triangle = AcuteTriangle(5, 6, 7)
        assert triangle.a == 5
        assert triangle.b == 6
        assert triangle.c == 7

    def test_invalid_triangle_inequality(self):
        """Test that invalid triangles raise ValueError"""
        with pytest.raises(ValueError, match="triangle inequality"):
            AcuteTriangle(1, 2, 10)

    def test_right_triangle_rejected(self):
        """Test that right triangles are rejected"""
        with pytest.raises(ValueError, match="acute"):
            AcuteTriangle(3, 4, 5)

    def test_obtuse_triangle_rejected(self):
        """Test that obtuse triangles are rejected"""
        with pytest.raises(ValueError, match="acute"):
            AcuteTriangle(3, 4, 6)


class TestAcuteTriangleGeometry:
    """Test geometric calculations"""

    def test_area(self):
        """Test area calculation using Heron's formula"""
        triangle = AcuteTriangle(5, 6, 7)
        expected_area = 14.696938456699069
        assert math.isclose(triangle.area(), expected_area)

    def test_perimeter(self):
        """Test perimeter calculation"""
        triangle = AcuteTriangle(5, 6, 7)
        assert triangle.perimeter() == 18

    def test_inradius(self):
        """Test inradius calculation"""
        triangle = AcuteTriangle(5, 6, 7)
        expected_inradius = triangle.area() / (0.5 * triangle.perimeter())
        assert math.isclose(triangle.inradius(), expected_inradius)

    def test_circumradius(self):
        """Test circumradius calculation"""
        triangle = AcuteTriangle(5, 6, 7)
        expected_circumradius = (5 * 6 * 7) / (4 * triangle.area())
        assert math.isclose(triangle.circumradius(), expected_circumradius)

    def test_altitudes(self):
        """Test altitude calculations"""
        triangle = AcuteTriangle(5, 6, 7)
        area = triangle.area()
        assert math.isclose(triangle.altitude_a(), 2 * area / 5)
        assert math.isclose(triangle.altitude_b(), 2 * area / 6)
        assert math.isclose(triangle.altitude_c(), 2 * area / 7)


class TestAcuteTriangleAngles:
    """Test angle calculations"""

    def test_angles_sum_to_pi(self):
        """Test that angles sum to π radians"""
        triangle = AcuteTriangle(5, 6, 7)
        angle_sum = triangle.angle_a() + triangle.angle_b() + triangle.angle_c()
        assert math.isclose(angle_sum, math.pi)

    def test_all_angles_acute(self):
        """Test that all angles are less than π/2"""
        triangle = AcuteTriangle(5, 6, 7)
        assert triangle.angle_a() < math.pi / 2
        assert triangle.angle_b() < math.pi / 2
        assert triangle.angle_c() < math.pi / 2

    def test_equilateral_triangle(self):
        """Test angles in an equilateral triangle"""
        triangle = AcuteTriangle(5, 5, 5)
        expected_angle = math.pi / 3  # 60 degrees
        assert math.isclose(triangle.angle_a(), expected_angle)
        assert math.isclose(triangle.angle_b(), expected_angle)
        assert math.isclose(triangle.angle_c(), expected_angle)


class TestAcuteTriangleScaling:
    """Test scaling operations"""

    def test_multiply_scale_area(self):
        """Test multiplication scaling"""
        triangle = AcuteTriangle(5, 6, 7)
        original_area = triangle.area()
        scaled = triangle * 4
        assert math.isclose(scaled.area(), original_area * 4)

    def test_imul_scale_area(self):
        """Test in-place multiplication scaling"""
        triangle = AcuteTriangle(5, 6, 7)
        original_area = triangle.area()
        triangle *= 4
        assert math.isclose(triangle.area(), original_area * 4)

    def test_divide_scale_area(self):
        """Test division scaling"""
        triangle = AcuteTriangle(5, 6, 7)
        original_area = triangle.area()
        scaled = triangle / 4
        assert math.isclose(scaled.area(), original_area / 4)

    def test_scaling_preserves_acute_property(self):
        """Test that scaling maintains acute triangle property"""
        triangle = AcuteTriangle(5, 6, 7)
        scaled = triangle * 2
        # All angles should still be acute
        assert scaled.angle_a() < math.pi / 2
        assert scaled.angle_b() < math.pi / 2
        assert scaled.angle_c() < math.pi / 2


class TestAcuteTriangleComparison:
    """Test comparison operations"""

    def test_equality(self):
        """Test equality comparison"""
        t1 = AcuteTriangle(5, 6, 7)
        t2 = AcuteTriangle(5, 6, 7)
        assert t1 == t2

    def test_inequality(self):
        """Test inequality"""
        t1 = AcuteTriangle(5, 6, 7)
        t2 = AcuteTriangle(3, 4, 4)
        assert t1 != t2

    def test_less_than_by_area(self):
        """Test less than comparison based on area"""
        t1 = AcuteTriangle(3, 4, 4)
        t2 = AcuteTriangle(5, 6, 7)
        assert t1 < t2

    def test_greater_than_by_area(self):
        """Test greater than comparison based on area"""
        t1 = AcuteTriangle(5, 6, 7)
        t2 = AcuteTriangle(3, 4, 4)
        assert t1 > t2


class TestObtuseTriangleBasics:
    """Test basic initialization and properties"""

    def test_initialization(self):
        """Test obtuse triangle initialization"""
        triangle = ObtuseTriangle(3, 4, 6)
        assert triangle.a == 3
        assert triangle.b == 4
        assert triangle.c == 6

    def test_invalid_triangle_inequality(self):
        """Test that invalid triangles raise ValueError"""
        with pytest.raises(ValueError, match="triangle inequality"):
            ObtuseTriangle(1, 2, 10)

    def test_right_triangle_rejected(self):
        """Test that right triangles are rejected"""
        with pytest.raises(ValueError, match="obtuse"):
            ObtuseTriangle(3, 4, 5)

    def test_acute_triangle_rejected(self):
        """Test that acute triangles are rejected"""
        with pytest.raises(ValueError, match="obtuse"):
            ObtuseTriangle(5, 6, 7)


class TestObtuseTriangleGeometry:
    """Test geometric calculations"""

    def test_area(self):
        """Test area calculation using Heron's formula"""
        triangle = ObtuseTriangle(3, 4, 6)
        s = 13 / 2
        expected_area = math.sqrt(s * (s - 3) * (s - 4) * (s - 6))
        assert math.isclose(triangle.area(), expected_area)

    def test_perimeter(self):
        """Test perimeter calculation"""
        triangle = ObtuseTriangle(3, 4, 6)
        assert triangle.perimeter() == 13

    def test_inradius(self):
        """Test inradius calculation"""
        triangle = ObtuseTriangle(3, 4, 6)
        expected_inradius = triangle.area() / (0.5 * triangle.perimeter())
        assert math.isclose(triangle.inradius(), expected_inradius)

    def test_circumradius(self):
        """Test circumradius calculation"""
        triangle = ObtuseTriangle(3, 4, 6)
        expected_circumradius = (3 * 4 * 6) / (4 * triangle.area())
        assert math.isclose(triangle.circumradius(), expected_circumradius)

    def test_altitudes(self):
        """Test altitude calculations"""
        triangle = ObtuseTriangle(3, 4, 6)
        area = triangle.area()
        assert math.isclose(triangle.altitude_a(), 2 * area / 3)
        assert math.isclose(triangle.altitude_b(), 2 * area / 4)
        assert math.isclose(triangle.altitude_c(), 2 * area / 6)


class TestObtuseTriangleAngles:
    """Test angle calculations"""

    def test_angles_sum_to_pi(self):
        """Test that angles sum to π radians"""
        triangle = ObtuseTriangle(3, 4, 6)
        angle_sum = triangle.angle_a() + triangle.angle_b() + triangle.angle_c()
        assert math.isclose(angle_sum, math.pi)

    def test_one_angle_obtuse(self):
        """Test that exactly one angle is greater than π/2"""
        triangle = ObtuseTriangle(3, 4, 6)
        angles = [triangle.angle_a(), triangle.angle_b(), triangle.angle_c()]
        obtuse_count = sum(1 for angle in angles if angle > math.pi / 2)
        assert obtuse_count == 1

    def test_largest_side_opposite_obtuse_angle(self):
        """Test that the largest side is opposite the obtuse angle"""
        triangle = ObtuseTriangle(3, 4, 6)
        # c=6 is the largest side, so angle_c should be obtuse
        assert triangle.angle_c() > math.pi / 2


class TestObtuseTriangleScaling:
    """Test scaling operations"""

    def test_multiply_scale_area(self):
        """Test multiplication scaling"""
        triangle = ObtuseTriangle(3, 4, 6)
        original_area = triangle.area()
        scaled = triangle * 4
        assert math.isclose(scaled.area(), original_area * 4)

    def test_imul_scale_area(self):
        """Test in-place multiplication scaling"""
        triangle = ObtuseTriangle(3, 4, 6)
        original_area = triangle.area()
        triangle *= 4
        assert math.isclose(triangle.area(), original_area * 4)

    def test_divide_scale_area(self):
        """Test division scaling"""
        triangle = ObtuseTriangle(3, 4, 6)
        original_area = triangle.area()
        scaled = triangle / 4
        assert math.isclose(scaled.area(), original_area / 4)

    def test_scaling_preserves_obtuse_property(self):
        """Test that scaling maintains obtuse triangle property"""
        triangle = ObtuseTriangle(3, 4, 6)
        scaled = triangle * 2
        # Should still have exactly one obtuse angle
        angles = [scaled.angle_a(), scaled.angle_b(), scaled.angle_c()]
        obtuse_count = sum(1 for angle in angles if angle > math.pi / 2)
        assert obtuse_count == 1


class TestObtuseTriangleComparison:
    """Test comparison operations"""

    def test_equality(self):
        """Test equality comparison"""
        t1 = ObtuseTriangle(3, 4, 6)
        t2 = ObtuseTriangle(3, 4, 6)
        assert t1 == t2

    def test_inequality(self):
        """Test inequality"""
        t1 = ObtuseTriangle(3, 4, 6)
        t2 = ObtuseTriangle(2, 3, 4)
        assert t1 != t2

    def test_less_than_by_area(self):
        """Test less than comparison based on area"""
        t1 = ObtuseTriangle(2, 3, 4)
        t2 = ObtuseTriangle(3, 4, 6)
        assert t1 < t2

    def test_greater_than_by_area(self):
        """Test greater than comparison based on area"""
        t1 = ObtuseTriangle(3, 4, 6)
        t2 = ObtuseTriangle(2, 3, 4)
        assert t1 > t2


class TestTriangleCrossComparison:
    """Test comparisons between different triangle types"""

    def test_compare_right_and_acute(self):
        """Test comparison between right and acute triangles"""
        right = RightTriangle(3, 4)
        acute = AcuteTriangle(5, 6, 7)
        assert right < acute  # right has area 6, acute has area ~14.7

    def test_compare_right_and_obtuse(self):
        """Test comparison between right and obtuse triangles"""
        right = RightTriangle(3, 4)
        obtuse = ObtuseTriangle(3, 4, 6)
        assert right > obtuse  # right has area 6, obtuse has area ~5.3

    def test_compare_acute_and_obtuse(self):
        """Test comparison between acute and obtuse triangles"""
        acute = AcuteTriangle(5, 6, 7)
        obtuse = ObtuseTriangle(3, 4, 6)
        assert acute > obtuse  # acute has area ~14.7, obtuse has area ~5.3


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
