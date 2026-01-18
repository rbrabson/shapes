""" Module to define a RightTriangle class and demonstrate its functionality """
from shapes.triangle import RightTriangle


def main():
    """ Main function to demonstrate RightTriangle class functionality """

    triangle = RightTriangle(3, 4)
    print(triangle)
    print("hypotenuse:", triangle.hypotenuse())

    print("area:", triangle.area())
    print("perimeter:", triangle.perimeter())
    print("sin:", triangle.sin())
    print("cos:", triangle.cos())
    print("tan:", triangle.tan())
    print("alpha (radians):", triangle.alpha())
    print("beta (radians):", triangle.beta())

    if triangle.opposite() > triangle.adjacent():
        print("Opposite side is longer than adjacent side.")
    elif triangle.opposite() < triangle.adjacent():
        print("Adjacent side is longer than opposite side.")
    else:
        print("Opposite and adjacent sides are of equal length.")
    triangle *= 3
    print("After scaling by 3:")
    print(triangle)
    print("area", triangle.area())
    print("perimeter", triangle.perimeter())
    print("sin:", triangle.sin())

    f = float(3)
    print(f)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
