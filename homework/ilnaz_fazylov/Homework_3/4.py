class TriangleException(Exception):
    pass


class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hypothesis(self):
        if self.a >= 0 and self.b >= 0:
            return (self.a ** 2 + self.b ** 2) ** 0.5
        else:
            raise TriangleException('Expected positive a and b')

    def square(self):
        return self.a * self.b / 2
