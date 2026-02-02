from pygame.math import Vector2
from engine.body import Circle


class Forces:
    def applyGravity(circle, g=(0,500)):
        circle.acceleration += Vector2(g)
