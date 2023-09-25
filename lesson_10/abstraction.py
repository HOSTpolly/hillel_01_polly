from math import pi
from typing import Protocol


class CanCalculateArea(Protocol):
    def calculate_area(self) -> float:
        ...


class Circle:
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return pi * self.radius ** 2


class Square:
    def __init__(self, side: int) -> None:
        self.side = side

    def calculate_area(self) -> float:
        return self.side ** 2


class Diamond:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def calculate_area(self) -> float:
        return self.a * self.b


def validate(shape: CanCalculateArea, max_limit: float) -> CanCalculateArea:
    if shape.calculate_area() > max_limit:
        raise ValueError("The area is too big")
    return shape


if __name__ == "__main__":
    c1 = Circle(radius=12)
    s2 = Square(side=10)

    shape1 = validate(c1, 1222)
    shape2 = validate(s2, 1323)

    print(shape1)
    print(shape2)


def foo(a: int):
    pass


# Однакові типи аргументів у викликах функції тут
foo(42)
