import pygame
from engine.body import Circle
from rendering.render import Render
from engine.forces import Forces


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("PyGame Window")
clock = pygame.time.Clock()

renderer = Render(screen)
forces = Forces

circles = [
    Circle((200, 300), 20, (255, 0, 0), 5),
    Circle((400,300), 10, (0, 255, 255), 10),
    Circle((100, 20), 5, (0, 0, 0), 2)
]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30,30,30))

    dt = clock.tick(60) / 1000

    floor = 600

    for c in circles:
        if c.pos.y + c.radius >= floor:
            c.velocity = (0,0)
            c.pos.y = floor - c.radius
        else: 
            forces.applyGravity(c)
            c.velocity += c.acceleration * dt
            c.pos += c.velocity * dt


        renderer.drawCircle(c)


    pygame.display.flip()
    clock.tick(60)


pygame.quit()