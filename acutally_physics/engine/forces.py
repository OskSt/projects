from pygame.math import Vector2


class Forces:
    def __init__(self, gravity=(0, 980)):
        self.gravity = Vector2(gravity)

    def applyGravity(self, obj):
        obj.acceleration += self.gravity
