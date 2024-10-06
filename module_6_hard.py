import math

class Figure:
    filled_ = True # закрашенный
    sides_count = 0
    def __init__(self, color, *new_sides):
        self._color = (255, 255, 255)
        self._sides = [1] * self.sides_count # инициализация списка сторон (по умолчпнию длина стороны равна 1)
        self._sides = self.set_sides(*new_sides)
        if all(0 <= value < 255 for value in color):
            self._color = list(color) # список цветов в формате RGB)

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            if all(x > 0 for x in new_sides):
                return True
        return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = []
            for el in new_sides:
                self._sides.append(int(el))
        return self._sides

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color[0] = int(r)
            self._color[1] = int(g)
            self._color[2] = int(b)
            print('Цвет изменился')
        else:
            print('Цвет не PGB, изменение цвета не возможно')

    def get_color(self):
        return self._color

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *new_sides):
        super().__init__(color, *new_sides)
        self.__radius = new_sides[0] /2 /math.pi# сохраняем радиус как атрибут экземпляра

    def get_square(self):
       return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = sum(self._sides) / 2
        return math.sqrt(p*(p - self._sides[0])*(p - self._sides[1])*(p - self._sides[1]))

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *new_sides):
        super().__init__(color, *new_sides)
        if len(new_sides) > 1:
            self._sides = [1] * 12  # переопределелили согласно ТЗ
        else:
            self._sides = [new_sides[0]] * 12 # переопределелили согласно ТЗ

    def get_volume(self):
        return self._sides[0] ** 3


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
cube2 = Cube((222, 35, 130), 6, 4)
