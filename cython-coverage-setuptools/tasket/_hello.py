import math

class A:
    def __init__(self, x):
        self.x = x

    def sin_squared(self):
        return math.sin(self.x * self.x)

    def cos_squared(self):
        return math.cos(self.x * self.x)
