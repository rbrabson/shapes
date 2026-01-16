# RightTriangle Package

A Python package for working with right-angled triangles, providing comprehensive geometric and trigonometric calculations.

## Features

- **Geometric Properties**: Calculate area, perimeter, inradius, circumradius, and altitude
- **Trigonometric Functions**: Compute sin, cos, tan, sec, csc, cot, and angles (alpha, beta)
- **Scaling Operations**: Scale triangles by area with intuitive operators (`*`, `/`, `*=`, `/=`)
- **Comparisons**: Compare triangles by area with full ordering support
- **Type Safety**: Full type hints using Python's typing module

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

### Basic Usage

```python
from shapes.triangle import RightTriangle

# Create a 3-4-5 right triangle
triangle = RightTriangle(3, 4)

# Access properties
print(f"Opposite: {triangle.opposite()}")      # 3
print(f"Adjacent: {triangle.adjacent()}")      # 4
print(f"Hypotenuse: {triangle.hypotenuse()}")  # 5.0
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
t1 = RightTriangle(3, 4)   # area = 6
t2 = RightTriangle(5, 12)  # area = 30
t3 = RightTriangle(3, 4)   # area = 6

print(t1 == t3)  # True
print(t1 < t2)   # True (compared by area)
print(t2 > t1)   # True
print(t1 <= t3)  # True
```

## API Reference

### Constructor

```python
RightTriangle(a: float, b: float)
```

Creates a right triangle with:

- `a`: length of the opposite side
- `b`: length of the adjacent side
- `c`: automatically calculated hypotenuse

### Properties

- `opposite() -> float`: Returns the opposite side length
- `adjacent() -> float`: Returns the adjacent side length
- `hypotenuse() -> float`: Returns the hypotenuse length

### Geometric Methods

- `area() -> float`: Triangle area
- `perimeter() -> float`: Triangle perimeter
- `inradius() -> float`: Radius of inscribed circle
- `circumradius() -> float`: Radius of circumscribed circle
- `altitude() -> float`: Altitude from right angle to hypotenuse

### Trigonometric Methods

- `sin() -> float`: Sine of angle alpha
- `cos() -> float`: Cosine of angle alpha
- `tan() -> float`: Tangent of angle alpha
- `sec() -> float`: Secant of angle alpha
- `csc() -> float`: Cosecant of angle alpha
- `cot() -> float`: Cotangent of angle alpha
- `alpha() -> float`: Angle in radians (opposite/adjacent)
- `beta() -> float`: Complementary angle in radians

### Operators

- `*`: Scale triangle by area (returns new triangle)
- `/`: Scale down triangle by area (returns new triangle)
- `*=`: In-place scale by area
- `/=`: In-place scale down by area
- `==`, `!=`: Equality comparison
- `<`, `>`, `<=`, `>=`: Ordering by area

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest shapes/tests/test_triangle.py -v

# Run specific test class
pytest shapes/tests/test_triangle.py::TestRightTriangleTrigonometry -v

# Run with coverage
pytest shapes/tests/test_triangle.py --cov=shapes.triangle
```

The test suite includes 40+ tests covering:

- Basic initialization and properties
- Geometric calculations
- Trigonometric functions
- Scaling operations
- Comparison operators
- String representations
- Edge cases (special triangles, extreme values)

## Project Structure

``` code
.
├── shapes/
│   ├── __init__.py
│   ├── triangle.py          # RightTriangle class implementation
│   └── tests/
│       ├── __init__.py
│       └── test_triangle.py # Comprehensive test suite
├── main.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10+
- No external dependencies for core functionality
- pytest for running tests

## License

MIT License

## Contributing

Contributions are welcome! Please ensure all tests pass before submitting a pull request.

```bash
# Run tests
pytest shapes/tests/test_triangle.py -v

# Check code style
flake8 shapes/
```

## Examples

### Special Right Triangles

```python
# 45-45-90 triangle (isosceles)
iso = RightTriangle(1, 1)
print(f"Hypotenuse: {iso.hypotenuse()}")  # √2 ≈ 1.414

# 30-60-90 triangle
import math
special = RightTriangle(1, math.sqrt(3))
print(f"Hypotenuse: {special.hypotenuse()}")  # 2.0
```

### Pythagorean Triples

```python
# Famous Pythagorean triples
triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]

for a, b, c in triples:
    triangle = RightTriangle(a, b)
    print(f"{a}-{b}-{c}: hypotenuse = {triangle.hypotenuse()}")
```
