﻿class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width},{self.height}'

    def find_area(self):
        return self.width*self.height

r1 = Rectangle(5,10,50,100)
print(r1)
print(r1.find_area())


