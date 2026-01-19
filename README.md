# Triangles Package

A Python package for working with triangles, providing comprehensive geometric calculations for right-angled, acute, and obtuse triangles.

## Features

- **Multiple Triangle Types**: Support for `RightTriangle`, `AcuteTriangle`, and `ObtuseTriangle`
- **Object-Oriented Design**: Base `Triangle` class with inheritance hierarchy
- **Geometric Properties**: Calculate area, perimeter, inradius, circumradius, and altitudes
- **Angle Calculations**: Compute all angles using law of cosines
- **Trigonometric Functions**: Full set of trig functions for right triangles
- **Scaling Operations**: Scale triangles by area with intuitive operators (`*`, `/`, `*=`, `/=`)
- **Comparisons**: Compare triangles by area with full ordering support
- **Type Safety**: Full type hints using Python's typing module with `Self` support
- **Input Validation**: Automatic validation of triangle inequality and angle constraints

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd test

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage - Right Triangle

```python
from triangles import RightTriangle

# Create a 3-4-5 right triangle
triangle = RightTriangle(3, 4)

# Access properties
print(f"Opposite: {triangle.opposite()}")      # 3
print(f"Adjacent: {triangle.adjacent()}")      # 4
print(f"Hypotenuse: {triangle.hypotenuse()}")  # 5.0
print(f"Area: {triangle.area()}")              # 6.0
```

### Acute Triangle

```python
from triangles import AcuteTriangle

# Create an acute triangle (all angles < 90°)
triangle = AcuteTriangle(5, 6, 7)

print(f"Area: {triangle.area()}")                    # ~14.70
print(f"Perimeter: {triangle.perimeter()}")          # 18
print(f"Angle A: {triangle.angle_a()}")              # radians
print(f"Angle B: {triangle.angle_b()}")              # radians
print(f"Angle C: {triangle.angle_c()}")              # radians

# Get altitudes
print(f"Altitude to side a: {triangle.altitude_a()}")
print(f"Altitude to side b: {triangle.altitude_b()}")
print(f"Altitude to side c: {triangle.altitude_c()}")
```

### Obtuse Triangle

```python
from triangles import ObtuseTriangle

# Create an obtuse triangle (one angle > 90°)
triangle = ObtuseTriangle(3, 4, 6)

print(f"Area: {triangle.area()}")                    # ~5.33
print(f"Perimeter: {triangle.perimeter()}")          # 13
print(f"Circumradius: {triangle.circumradius()}")    # radius of circumscribed circle

# Check angles
angles = [triangle.angle_a(), triangle.angle_b(), triangle.angle_c()]
obtuse_angles = [a for a in angles if a > 1.5708]  # > π/2
print(f"Obtuse angles: {len(obtuse_angles)}")        # 1
```

### Input Validation

```python
from triangles import AcuteTriangle, ObtuseTriangle

# Triangle inequality violation
try:
    triangle = AcuteTriangle(1, 2, 10)
except ValueError as e:
    print(e)  # "Sides must satisfy triangle inequality"

# Wrong triangle type
try:
    triangle = AcuteTriangle(3, 4, 5)  # This is a right triangle
except ValueError as e:
    print(e)  # "All angles must be acute (less than 90 degrees)"

try:
    triangle = ObtuseTriangle(5, 6, 7)  # This is an acute triangle
except ValueError as e:
    print(e)  # "Exactly one angle must be obtuse (greater than 90 degrees)"
```

### Geometric Calculations

```python
triangle = RightTriangle(3, 4)

print(f"Area: {triangle.area()}")                    # 6.0
print(f"Perimeter: {triangle.perimeter()}")          # 12.0
print(f"Inradius: {triangle.inradius()}")            # 1.0
print(f"Circumradius: {triangle.circumradius()}")    # 2.5
print(f"Altitude: {triangle.altitude()}")            # 2.4
```

### Trigonometric Functions

```python
triangle = RightTriangle(3, 4)

print(f"sin: {triangle.sin()}")      # 0.6
print(f"cos: {triangle.cos()}")      # 0.8
print(f"tan: {triangle.tan()}")      # 0.75
print(f"alpha: {triangle.alpha()}")  # ~0.6435 radians
print(f"beta: {triangle.beta()}")    # ~0.9273 radians
```

### Scaling Operations

```python
triangle = RightTriangle(3, 4)
original_area = triangle.area()  # 6.0

# Scale by area (multiply)
scaled = triangle * 4
print(scaled.area())  # 24.0 (4x the original area)

# Scale down by area (divide)
smaller = triangle / 2
print(smaller.area())  # 3.0 (half the original area)

# In-place scaling
triangle *= 2
print(triangle.area())  # 12.0
```

### Comparisons

```python
from triangles import RightTriangle, AcuteTriangle, ObtuseTriangle

t1 = RightTriangle(3, 4)          # area = 6
t2 = AcuteTriangle(5, 6, 7)       # area ≈ 14.7
t3 = ObtuseTriangle(3, 4, 6)      # area ≈ 5.33

# Compare by area
print(t1 > t3)   # True (6 > 5.33)
print(t2 > t1)   # True (14.7 > 6)
print(t1 == RightTriangle(3, 4))  # True

# Works across triangle types
triangles = [t1, t2, t3]
triangles.sort()  # Sorts by area
print([t.area() for t in triangles])  # [~5.33, 6.0, ~14.7]
```

## API Reference

### Triangle (Base Class)

Abstract base class for all triangle types.

**Common Properties:**

- `a`, `b`, `c`: Side lengths

**Common Methods:**

- `area() -> float`: Triangle area (abstract, implemented by subclasses)
- `perimeter() -> float`: Triangle perimeter
- `inradius() -> float`: Radius of inscribed circle

**Common Operators:**

- `*`, `/`, `*=`, `/=`: Scaling operations
- `==`, `!=`, `<`, `>`, `<=`, `>=`: Comparison operators

### RightTriangle

```python
RightTriangle(a: float, b: float)
```

Creates a right triangle with:

- `a`: length of the opposite side
- `b`: length of the adjacent side
- `c`: automatically calculated hypotenuse (√(a² + b²))

**Unique Methods:**

- `opposite() -> float`: Returns the opposite side length
- `adjacent() -> float`: Returns the adjacent side length
- `hypotenuse() -> float`: Returns the hypotenuse length
- `altitude() -> float`: Altitude from right angle to hypotenuse
- Trigonometric: `sin()`, `cos()`, `tan()`, `sec()`, `csc()`, `cot()`
- Angles: `alpha()`, `beta()` in radians

### AcuteTriangle

```python
AcuteTriangle(a: float, b: float, c: float)
```

Creates an acute triangle where all angles are less than 90°.

**Validation:** Raises `ValueError` if:

- Triangle inequality is violated
- Any angle is ≥ 90° (not acute)

**Unique Methods:**

- `circumradius() -> float`: Radius of circumscribed circle
- `altitude_a() -> float`: Altitude to side a
- `altitude_b() -> float`: Altitude to side b
- `altitude_c() -> float`: Altitude to side c
- `angle_a() -> float`: Angle opposite side a (radians)
- `angle_b() -> float`: Angle opposite side b (radians)
- `angle_c() -> float`: Angle opposite side c (radians)

### ObtuseTriangle

```python
ObtuseTriangle(a: float, b: float, c: float)
```

Creates an obtuse triangle where exactly one angle is greater than 90°.

**Validation:** Raises `ValueError` if:

- Triangle inequality is violated
- Zero or multiple angles are obtuse

**Unique Methods:**
Same as `AcuteTriangle`:

- `circumradius() -> float`: Radius of circumscribed circle
- `altitude_a()`, `altitude_b()`, `altitude_c() -> float`: Altitudes
- `angle_a()`, `angle_b()`, `angle_c() -> float`: Angles in radians

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest triangles/tests/test_triangle.py -v

# Run tests for specific triangle type
pytest triangles/tests/test_triangle.py::TestRightTriangle -v
pytest triangles/tests/test_triangle.py::TestAcuteTriangle -v
pytest triangles/tests/test_triangle.py::TestObtuseTriangle -v

# Run with coverage
pytest triangles/tests/test_triangle.py --cov=triangles.triangle
```

The test suite includes 83 tests covering:

**RightTriangle (40 tests):**

- Basic initialization and properties
- Geometric calculations
- Trigonometric functions
- Scaling operations
- Comparison operators
- String representations
- Edge cases (special triangles, extreme values)

**AcuteTriangle (20 tests):**

- Initialization and validation
- Geometric calculations (area, perimeter, radii, altitudes)
- Angle calculations and validation
- Scaling operations
- Comparison operators

**ObtuseTriangle (20 tests):**

- Initialization and validation
- Geometric calculations
- Angle calculations (ensuring one obtuse angle)
- Scaling operations
- Comparison operators

**Cross-type comparisons (3 tests):**

- Comparing different triangle types by area

## Project Structure

```
.
├── triangles/
│   ├── __init__.py          # Exports Triangle, RightTriangle, AcuteTriangle, ObtuseTriangle
│   ├── triangle.py          # Triangle base class and implementations
│   └── tests/
│       ├── __init__.py
│       └── test_triangle.py # Comprehensive test suite (83 tests)
├── README.md
└── requirements.txt
```

## Class Hierarchy

```
Triangle (ABC)
├── RightTriangle
├── AcuteTriangle
└── ObtuseTriangle
```

The `Triangle` base class provides common functionality:

- Side storage (`a`, `b`, `c`)
- Perimeter and inradius calculations
- Comparison operators (`==`, `<`, etc.)
- Scaling operators (`*=`, `/=`)

Each subclass implements:

- Specific `area()` calculation
- Validation logic in `__init__`
- Type-specific geometric calculations

## Requirements

- Python 3.10+
- No external dependencies for core functionality
- pytest for running tests

## License

MIT License

## Contributing

Contributions are welcome! Please ensure all tests pass before submitting a pull request.

```bash
# Run all tests
pytest triangles/tests/test_triangle.py -v

# Check for type errors
python -m mypy triangles/triangle.py

# Format code (if using black)
black triangles/
```

## Design Notes

### Inheritance Hierarchy

The package uses an abstract base class `Triangle` to share common functionality across all triangle types, reducing code duplication and ensuring consistent behavior.

### Type Safety

The package uses Python 3.10+ type hints, including:

- `Self` type for proper return type inference in methods
- Abstract methods to enforce implementation in subclasses
- Union types (`int | float`) for flexible numeric inputs

### Validation Strategy

Each triangle type validates its constraints:

- **RightTriangle**: Automatically calculates hypotenuse (no validation needed)
- **AcuteTriangle**: Validates all angles < 90° using law of cosines
- **ObtuseTriangle**: Validates exactly one angle > 90°

All types check the triangle inequality: `a + b > c`, `a + c > b`, `b + c > a`

## Examples

### Working with Different Triangle Types

```python
from triangles import RightTriangle, AcuteTriangle, ObtuseTriangle
import math

# Right triangle - Pythagorean triple
right = RightTriangle(3, 4)
print(f"Right triangle area: {right.area()}")           # 6.0
print(f"sin(alpha): {right.sin()}")                     # 0.6

# Acute triangle - Equilateral
side = 5
equilateral = AcuteTriangle(side, side, side)
print(f"Equilateral area: {equilateral.area()}")        # ~10.83
angle = equilateral.angle_a()
print(f"Each angle: {math.degrees(angle)}°")            # 60°

# Obtuse triangle
obtuse = ObtuseTriangle(3, 4, 6)
print(f"Obtuse area: {obtuse.area()}")                  # ~5.33
angles = [obtuse.angle_a(), obtuse.angle_b(), obtuse.angle_c()]
obtuse_angle = max(angles)
print(f"Largest angle: {math.degrees(obtuse_angle)}°")  # ~117°
```

### Special Right Triangles

```python
# 45-45-90 triangle (isosceles)
iso = RightTriangle(1, 1)
print(f"Hypotenuse: {iso.hypotenuse()}")  # √2 ≈ 1.414

# 30-60-90 triangle
import math
special = RightTriangle(1, math.sqrt(3))
print(f"Hypotenuse: {special.hypotenuse()}")  # 2.0
print(f"Alpha: {math.degrees(special.alpha())}°")  # 30°
print(f"Beta: {math.degrees(special.beta())}°")    # 60°
```

### Pythagorean Triples

```python
# Famous Pythagorean triples
triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]

for a, b, c in triples:
    triangle = RightTriangle(a, b)
    print(f"{a}-{b}-{c}: hypotenuse = {triangle.hypotenuse()}")
```

### Scaling Triangles

```python
from triangles import AcuteTriangle

# Create a triangle
triangle = AcuteTriangle(3, 4, 4)
original_area = triangle.area()

# Scale up - doubles the area
scaled = triangle * 2
print(f"Original: {original_area:.2f}, Scaled: {scaled.area():.2f}")

# Scaling maintains triangle type properties
print(f"Still acute: {all([
    scaled.angle_a() < 1.5708,  # π/2
    scaled.angle_b() < 1.5708,
    scaled.angle_c() < 1.5708
])}")  # True
```
