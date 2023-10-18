# 1 Реализовать класс вектора на плоскости. Используя перегрузку операторов, реализовать:
# +	Сложение и вычитание векторов
# +	Сравнение векторов (равно/не равно)
# +	Умножение вектора на число
# +	Скалярное произведение векторов
# +	Получение длины вектора
# +	Вывод вектора в консоль при помощи функции print() в формате <x; y>
# +	Отображение вектора при работе с интерпретатором в формате  <x; y>

from math import sqrt


class Vector2D:
    """ Класс вектора"""

    def __init__(self, x=0, y=0):
        """Конструктор"""
        self.x = x
        self.y = y

    def __add__(self, other):  # сложение x + y
        """ Сложение векторов """
        temp = Vector2D()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp

    def __sub__(self, other):  # вычитание x - y
        """ Вычитание векторов """
        temp = Vector2D()
        temp.x = self.x - other.x
        temp.x = self.y - other.y
        return temp

    def __eq__(self, other):  # x == y
        """ Равенство векторов """
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):  # x != y
        """ Неравенство векторов """
        return (self.x != other.x) or (self.y != other.y)

    def __mul__(self, other):  # умножение(x * y)
        """ Умножение """
        if (type(other) is int) or (type(other) is float):
            return Vector2D(self.x * other, self.y * other)
        elif type(other) is Vector2D:
            return self.x * other.x + self.y * other.y
        else:
            raise Exception('Unknown argument type')

    def __rmul__(self, other):  # умножение(x * y)
        """ Умножение с другой стороны """
        return self * other

    def __str__(self):
        """ Перевод в строку(для печати)"""
        return "<{}; {}>".format(self.x, self.y)

    def __repr__(self):
        """ Сырое представление"""
        return str(self)

    def __len__(self):
        """ Модуль вектора с округлением до целочисленного """
        return int(sqrt(self.x ** 2 + self.y ** 2))

    def __abs__(self):
        """ Модуль вектора """
        return sqrt(self.x ** 2 + self.y ** 2)


if __name__ == "__main__":
    vec = Vector2D(3, 5)
    vec2 = Vector2D(4, 5)
    vec3 = vec + vec2
    print(vec3)
    print("Сложение: " + str(vec + vec2))
    a = len(vec)
    a = abs(vec)
    print(a)
    print(vec)
    print(vec * 2.0)
    print(2 * vec)
    print(vec * vec)
