import pygame
from engine.body import Circle
from engine.body import Rectangle
from rendering.render import Render
from engine.forces import Forces
from engine.collisions.collision import Collisions


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("PyGame Window")
clock = pygame.time.Clock()

renderer = Render(screen)
forces = Forces()
collisions = Collisions()

objects = [
    Circle((200, 300), 20, (255, 0, 0), 5),
    Circle((400,300), 10, (0, 255, 255), 10),
    Circle((100, 20), 5, (0, 0, 0), 2),
    Rectangle((0, 580), 800, 20, (0,0,0), 100)
]



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))    

    dt = clock.tick(60) / 1000

    collisions.check(objects)

    for o in objects:
        forces.applyGravity(o)     
        if isinstance(o, Circle):
            o.velocity += o.acceleration * dt
            o.pos += o.velocity * dt 
            renderer.drawCircle(o)
        elif isinstance(o, Rectangle):
            renderer.drawRectangle(o)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()