''''''
'''
Дополнительное практическое задание по модулю: "Наследование классов."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

Задание "Они все так похожи":
Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216
Файл с кодом (module6hard.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub 
репозиторий с файлом решения.
'''
from math import pi, sqrt


# импорт значения pi и вычисление корня sqrt

class Figure:
    # Родительский класс
    sides_count = 0

    def __init__(self, sides: int, color):
        self.__sides = sides
        # список сторон(целые числа)
        self.__color = color
        # список цветов в формате RGB
        self.filled = False
        # закрашенный, bool

    def get_color(self):
        # возвращает список RGB цветов
        return list(self.__color)

    def get_sides(self):
        return list(self.__sides)

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and (
                isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
            return True
        else:
            return False

        # проверяет корректность переданных значений gеред установкой нового цвета.

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        for side_new in sides:
            if len(sides) == self.sides_count and isinstance(side_new, int) and side_new > 0:
                return True
            else:
                return False

    def __len__(self):
        self.perimetr = 0
        for len_side in self.__sides:
            self.perimetr += len_side
        return self.perimetr

    def set_sides(self, *new_sides):

        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides


class Circle(Figure):
    # Круг
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(sides, color)
        self.__radius = sides / (2 * pi)
        print(f'радиус {round(self.__radius, 2)}')
        print(f'сторона {sides}')

    def get_square(self):
        # возврат площади по формуле
        # Длина окружности в квадратный корень разделить на 4 умноженное на pi
        # округлено ло 2 знаков после запятой
        return round((self.get_sides()[0] ** 2) / (4 * pi), 2)


class Triangle(Figure):
    # Треугольник
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(sides, color)

    def get_square(self):
        # возврат площади по формуле Герона S=sqrt(p*(p-a)*(p-b)*(p-c)
        # где p=полупериметр, a,b,c - стороны
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]

        return round(sqrt((0.5 * (self.__len__())) *
                          ((0.5 * (self.__len__())) - a) *
                          ((0.5 * (self.__len__())) - b) *
                          ((0.5 * (self.__len__())) - c)), 2)
        # возврат площади с округлением до 2 знаков после запятой


class Cube(Figure):
    # Куб
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__([sides] * 12, color)
        self.__sides = sides

    def get_volume(self):
        # Возврат объема куба
        return self.get_sides()[0] ** 3


print(f'{"*" * 2} Код для проверки: {"*" * 30}')
circle1 = Circle((200, 200, 100), 10)
# (Цвет, стороны круга)
cube1 = Cube((222, 35, 130), 6)
# (Цвет, стороны куба)

print(f'{"*" * 2} Проверка на изменение цветов: {"*" * 20}')
circle1.set_color(55, 66, 77)
# Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  #
# Не изменится
print(cube1.get_color())

print(f'{"*" * 2} Проверка на изменение сторон: {"*" * 20}')

cube1.set_sides(5, 3, 12, 4, 5)
# Не изменится
print(cube1.get_sides())
circle1.set_sides(15)
# Изменится
print(circle1.get_sides())

print(f'{"*" * 2} Проверка периметра круга (длина круга) {"*" * 10}')
print(len(circle1))

print(f'{"*" * 2} Проверка объёма (куба): {"*" * 25}')
print(cube1.get_volume())
