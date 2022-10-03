import pygame
from src.entity import Entity


# Initialization
pygame.init()


# Window Handling
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("That Magic Swordsmen")


# Entities
player = Entity("Magus Flame", 100, 100, 0, 0)



running = True
while running:
    window.fill((0, 0, 0))
    pygame.display.update()
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False



