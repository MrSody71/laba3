from math import pi

class Shape:
    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределен")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() должен быть переопределен")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


circle = Circle(5)

print(f"Круг: площадь={circle.area():.2f}, периметр={circle.perimeter():.2f}")