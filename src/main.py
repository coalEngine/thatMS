import pygame
from game import World
from game import Entity


# Initialization



# Window Handling
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("That Magic Swordsmen")


# Entities
player = Entity("Magus Flame", 100, 100, 0, 0)

if __name__ == "__main__":
    world = World()


while True:
    world.update()
    world.handle_events()
    world.draw()