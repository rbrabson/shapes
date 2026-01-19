# Shapes Package

A Python package for working with geometric shapes, providing comprehensive calculations for triangles and circles.

## Features

### Triangles

- **Multiple Triangle Types**: Support for `RightTriangle`, `AcuteTriangle`, and `ObtuseTriangle`
- **Object-Oriented Design**: Base `Triangle` class with inheritance hierarchy
- **Geometric Properties**: Calculate area, perimeter, inradius, circumradius, and altitudes
- **Angle Calculations**: Compute all angles using law of cosines
- **Trigonometric Functions**: Full set of trig functions for right triangles
- **Input Validation**: Automatic validation of triangle inequality and angle constraints

### Circles

- **Comprehensive Circle Calculations**: Diameter, circumference, area
- **Advanced Properties**: Arc length, sector area, chord length, segment area
- **Angle-Based Calculations**: Support for calculations with central angles in radians

### Common Features

- **Scaling Operations**: Scale shapes by area with intuitive operators (`*`, `/`, `*=`, `/=`)
- **Comparisons**: Compare shapes by area with full ordering support
- **Type Safety**: Full type hints using Python's typing module with `Self` support

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

### Triangles

#### Basic Usage - Right Triangle

```python
from triangles import RightTriangle

# Create a 3-4-5 right triangle
triangle = RightTriangle(3, 4)

# Access properties
print(f"Opposite: {triangle.opposite()}")      # 3
print(f"Adjacent: {triangle.adjacent()}")      # 4
print(f"Hypotenuse: {triangle.hypotenuse()}")  # 5.0
print(f"Area: {triangle.area()}")              # 6.0
```# Acute Triangle

```python
from triangle
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

#### Obtuse Triangle

```python
from triangle import ObtuseTriangle

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

#### Input Validation

```python
from triangle import AcuteTriangle, ObtuseTriangle

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

#### Geometric Calculations

```python
from triangle import RightTriangle

triangle = RightTriangle(3, 4)

print(f"Area: {triangle.area()}")                    # 6.0
print(f"Perimeter: {triangle.perimeter()}")          # 12.0
print(f"Inradius: {triangle.inradius()}")            # 1.0
print(f"Circumradius: {triangle.circumradius()}")    # 2.5
print(f"Altitude: {triangle.altitude()}")            # 2.4
```# Trigonometric Functions

```python
from triangle import RightTriangle
nometric Functions

```python
triangle = RightTriangle(3, 4)

print(f"sin: {triangle.sin()}")      # 0.6
print(f"cos: {triangle.cos()}")      # 0.8
print(f"tan: {triangle.tan()}")      # 0.75
pri# Scaling Operations

```python
from triangle import RightTriangle


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
# Comparisons

```python
from triangle.area())  # 12.0
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

# # Circles

#### Basic Usage

```python
from circle import Circle

# Create a circle with radius 5
circle = Circle(5)

# Basic properties
print(f"Radius: {circle.radius}")              # 5.0
print(f"Diameter: {circle.diameter()}")        # 10.0
print(f"Circumference: {circle.circumference()}")  # 31.42...
print(f"Area: {circle.area()}")                # 78.54...
```

#### Advanced Circle Calculations

```python
from circle import Circle
import math

circle = Circle(10)

# Arc length for a given angle (in radians)
arc = circle.arc_length(math.pi / 2)  # Quarter circle arc
print(f"Arc length (90°): {arc}")      # 15.71...

# Sector area (pizza slice)
sector = circle.sector_area(math.pi / 2)
print(f"Sector area (90°): {sector}")  # 78.54...

# Chord length for a central angle
chord = circle.chord_length(math.pi / 3)  # 60° central angle
print(f"Chord length (60°): {chord}")     # 10.0

# Segment area (between chord and arc)
segment = circle.segment_area(math.pi / 3)
print(f"Segment area (60°): {segment}")   # 13.09...
```

#### Scaling Circles

```python
from circle import Circle

circle = Circle(5)
original_area = circle.area()  # ~78.54

# Scale by area (multiply)
scaled = circle * 4
print(f"Scaled radius: {scaled.radius}")  # 10.0 (radius doubles when area quadruples)
print(f"Scaled area: {scaled.area()}")    # ~314.16 (4x original)

# Scale down by area (divide)
smaller = circle / 2
print(f"Smaller area: {smaller.area()}")  # ~39.27 (half original)

# In-place scaling
circle *= 2
print(f"New area: {circle.area()}")       # ~157.08
```

#### Comparing Circles

```python
from circle import Circle

c1 = Circle(3)   # area ≈ 28.27
c2 = Circle(5)   # area ≈ 78.54
c3 = Circle(3)   # area ≈ 28.27

# Compare by area
print(c1 < c2)   # True
print(c1 == c3)  # True
print(c2 > c1)   # True

# Sort circles by area
circles = [c2, c1, c3]
circles.sort()
print([c.radius for c in circles])  # [3.0, 3.0, 5.0]
```

#### Input Validation

```python
from circle import Circle

# Negative radius
try:
    circle = Circle(-5)
except ValueError as e:
    print(e)  # "Radius must be positive"

# Zero radius
try:
    circle = Circle(0)
except ValueError as e:
    print(e)  # "Radius must be positive"
```

## API Reference

### Circle

```python
Circle(radius: int | float)
```

Creates a circle with the specified radius.

**Parameters:**

- `radius`: Radius of the circle (must be positive)

**Raises:**

- `ValueError`: If radius is not positive

**Properties:**

- `radius: float`: The circle's radius

**Methods:**

- `diameter() -> float`: Returns the diameter (2r)
- `circumference() -> float`: Returns the circumference (2πr)
- `area() -> float`: Returns the area (πr²)
- `arc_length(angle: float) -> float`: Arc length for given angle in radians
- `sector_area(angle: float) -> float`: Sector area for given angle in radians
- `chord_length(angle: float) -> float`: Chord length for given central angle in radians
- `segment_area(angle: float) -> float`: Circular segment area for given angle in radians

**Operators:**

- `*`, `/`, `*=`, `/=`: Scaling operations (scale by area)
- `==`, `!=`, `<`, `>`, `<=`, `>=`: Comparison operators (compare by area)

**String Representations:**

- `str(circle)`: Returns "Circle(radius=r)"
- `repr(circle)`: Returns "radius=r"riangle types
triangles = [t1, t2, t3]
triangles.sort()  # Sorts by area
print([t.area() for t in triangles])  # [~5.33, 6.0, ~14.7]

``` code

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
pytest

# Run triangle tests only
pytest triangle/tests/test_triangle.py -v

# Run circle tests only
pytest circle/tests/test_circle.py -v

# Run tests for specific triangle type
pytest triangle/tests/test_triangle.py::TestRightTriangle -v
pytest triangle/tests/test_triangle.py::TestAcuteTriangle -v
pytest triangle/tests/test_triangle.py::TestObtuseTriangle -v

# Run with coverage
pytest --cov=triangle --cov=circle
```

The test suite includes 139 tests covering:

**Triangle Tests (83 tests):**

- **RightTriangle (40 tests):**
  - Basic initialization and properties
  - Geometric calculations
  - Trigonometric functions
  - Scaling operations
  - Comparison operators
  - String representations
  - Edge cases (special triangles, extreme values)

- **AcuteTriangle (20 tests):**
  - Initialization and validation
  - Geometric calculations (area, perimeter, radii, altitudes)
  - Angle calculations and validation
  - Scaling operations
  - Comparison operators

- **ObtuseTriangle (20 tests):**
  - Initialization and validation
  - Geometric calculations
  - Angle calculations (ensuring one obtuse angle)
  - Scaling operations
  - Comparison operators

- **Cross-type comparisons (3 tests):**
  - Comparing different triangle types by area

**Circle Tests (56 tests):**

- **TestCircleBasics (7 tests):**
  - Initialization with positive, negative, and zero radius
  - Diameter calculations
  
- **TestCircleGeometry (11 tests):**
  - Circumference and area calculations
  - Arc length for various angles
  - Sector area calculations
  - Chord length calculations
  - Segment area calculations
  
- **TestCircleScaling (7 tests):**
  - Multiplication and division operators
  - In-place scaling operations
  - Type preservation after scaling
  
- **TestCircleComparison (8 tests):**
  - Equality and inequality
  - Less than, greater than comparisons
  - Area-based comparison validation
  
- **TestCircleStringRepresentation (3 tests):**
  - **str** and **repr** methods
  
- **TestCircleEdgeCases (20 tests):**
  - Very small and large radii
  - Chained scaling operations
  - Zero angle calculations
  - Comparison with scaled circles

## Project Structure

``` fixed
.
├── triangle/
│   ├── __init__.py          # Exports Triangle, RightTriangle, AcuteTriangle, ObtuseTriangle
│   ├── triangle.py          # Triangle base class and implementations
│   └── tests/
│       ├── __init__.py
│       └── test_triangle.py # Comprehensive test suite (83 tests)
├── circle/
│   ├── __init__.py          # Exports Circle
│   ├── circle.py            # Circle class implementation
│   └── tests/
│       ├── __init__.py
│       └── test_circle.py   # Comprehensive test suite (56 tests)
├── README.md
└── requirements.txt
```

## Class Hierarchy

**Triangles:**

``` fixed
Triangle (ABC)
├── RightTriangle
├── AcuteTriangle
└── ObtuseTriangle
```

**Circles:**

``` fixed
Circle (standalone class)
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
- pyte

## Check for type errors  

python -m mypy triangle/triangle.py circle/circle.py

## Design Notes

## Circle Design

The `Circle` class provides:

- **Radius-based initialization**: All calculations derive from the radius
- **Comprehensive geometric methods**: Beyond basic properties, includes sector, segment, arc, and chord calculations
- **Angle flexibility**: All angle-based methods accept radians for precision
- **Area-based scaling**: Like triangles, circles scale by area (radius changes by √scale)

## Examples

### Working with Circles and Triangles Together

```python
from circle import Circle
from triangle import RightTriangle
import math

# Create shapes
circle = Circle(5)
triangle = RightTriangle(3, 4)

# Compare areas
print(f"Circle area: {circle.area():.2f}")      # 78.54
print(f"Triangle area: {triangle.area():.2f}")  # 6.00
print(f"Circle is larger: {circle.area() > triangle.area()}")  # True

# Inscribed circle in triangle (approximation)
inradius = triangle.inradius()
inscribed = Circle(inradius)
print(f"Inscribed circle area: {inscribed.area():.2f}")  # 3.14

from triangle import RightTriangle
import math

# Circumscribed circle around right triangle
circumradius = triangle.circumradius()
circumscribed = Circle(circumradius)
print(f"Circumscribed circle area: {circumscribed.area():.2f}")  # 19.63
```

### Circle Sectors and Segments

```python
from circle import Circle
import math

from triangle import RightTriangle

# Pizza with 8 slices
pizza = Circle(12)  # 12 inch radius
slice_angle = 2 * math.pi / 8  # 45 degrees

slice_area = pizza.sector_area(slice_angle)
print(f"Each slice area: {slice_area:.2f} sq in")

# Arc length of crust per slice
crust_length = pizza.arc_length(slice_angle)
print(f"Crustper slice: {crust_length:.2f} inches")

# Calculate segment (bow-tie shape between chord and arc)
segment = pizza.segment_area(slice_angle)
print(f"Segment area: {segment:.2f} sq in")
```

### Working with Different Triangle Types

```python
from triangley

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

``` python
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
