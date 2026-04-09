from pygame.math import Vector2


class Body:
    def __init__(self, pos, mass, velocity, acceleration, movable):
        self.pos = Vector2(pos)
        self.mass = mass
        self.velocity = Vector2(velocity)
        self.acceleration = Vector2(acceleration)
        self.movable = movable

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.pos += self.velocity * dt

class Circle(Body):
    def __init__(self, pos, radius, color, mass, velocity, acceleration, movable):
        super().__init__(pos, mass, velocity, acceleration, movable)
        self.radius = radius
        self.color = color
  

class Rectangle(Body):
    def __init__(self, pos, width, height, color, mass, velocity, acceleration, movable):
        super().__init__(pos, mass, velocity, acceleration, movable)
        self.width = width
        self.height = height
        self.color = color
