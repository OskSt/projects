import pygame

class Render:
    def __init__(self, screen):
        self.screen = screen

    def drawCircle(self, circle):
        pygame.draw.circle(
            self.screen,
            circle.color,
            (int(circle.pos.x), int(circle.pos.y)),
            circle.radius
        )