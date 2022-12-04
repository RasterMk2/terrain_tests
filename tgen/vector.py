from __future__ import annotations
from math import sqrt
from typing import Self


def pyth(a: float, b: float) -> float:
    return sqrt(a ** 2 + b ** 2)


class Vector2:
    __slots__ = '_x', '_y'

    _x: float
    _y: float

    def __init__(self, x: float, y: float):
        pass

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def magnitude(self) -> float:
        return pyth(self.x, self.y)

    def normalize(self) -> Self:
        mag = self.magnitude()
        if mag == 0:
            return self
        return self / mag

    def __add__(self, other: Vector2) -> Self:
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2) -> Self:
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int |Vector2) -> Self:
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)

    def __add__(self, other: Vector2) -> Self:
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
