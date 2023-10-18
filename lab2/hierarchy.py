# 2.	Реализовать иерархию классов для расчёта площади плоских фигур:
# Прямоугольника +
# Треугольника +
# Круга +
# Базовый класс должен иметь чисто виртуальный метод square(), переопределения которой должны возвращать площадь фигуры.
# Производные классы фигур должны также иметь член данных для хранения названия фигуры («Circle», «Rectangle», …)

from abc import ABC, abstractmethod

# https://peps.python.org/pep-0698/
# only for python 3.12
from typing import override


class Figure(ABC):
    """Абстрактный класс фигуры"""

    def __init__(self):
        self.name = "Figure"

    @abstractmethod
    def square(self):
        """Виртуальный метод площади"""
        pass


class Rectangle(Figure):
    """Класс прямоугольника"""

    def __init__(self, x=0, y=0):
        """Конструктор прямоугольника"""
        self.name = "Rectangle"
        self.x = x
        self.y = y

    @override
    def square(self):
        """Площадь прямоугольника"""
        return self.x * self.y


from math import sqrt
from math import pi


class Triangle(Figure):
    """Класс прямоугольника"""

    def __init__(self, x=0, y=0, z=0):
        """Конструктор прямоугольника"""
        self.name = "Triangle"
        self.x = x
        self.y = y
        self.z = z

    @override
    def square(self):
        """Площадь прямоугольника"""
        p = 1.0 * (self.x + self.y + self.z) / 2
        return sqrt(p * (p - self.x) * (p - self.y) * (p - self.z))


class Circle(Figure):
    """Класс круга"""

    def __init__(self, R=0):
        """Конструктор круга"""
        self.name = "Circle"
        self.R = R

    @override
    def square(self):
        """Площадь круга"""
        return pi * self.R**2


if __name__ == "__main__":
    rect = Rectangle(3, 4)
    tri = Triangle(3, 4, 5)
    circ = Circle(1)
    print(rect.square())
    print(tri.square())
    print(circ.square())
