from pygame.math import Vector2

class Circle:
    def __init__(self, pos, radius, color, mass):
        self.pos = Vector2(pos)
        self.radius = radius
        self.color = color
        self.mass = mass
        self.velocity = Vector2(0,0)
        self.acceleration = Vector2(0,0)

class Rectangle:
    def __init__(self, pos, width, height, color, mass):
        self.pos = Vector2(pos)
        self.width = width
        self.height = height
        self.color = color
        self.mass = mass
        self.velocity = Vector2(0,0)
        self.acceleration = Vector2(0,0)