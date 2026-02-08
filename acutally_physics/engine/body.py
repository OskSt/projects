from pygame.math import Vector2


class Body:
    def __init__(self, pos, mass):
        self.pos = Vector2(pos)
        self.mass = mass
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

class Circle(Body):
    def __init__(self, pos, radius, color, mass):
        super().__init__(pos, mass)
        self.radius = radius
        self.color = color
  

class Rectangle(Body):
    def __init__(self, pos, width, height, color, mass):
        super().__init__(pos, mass)
        self.width = width
        self.height = height
        self.color = color
