import pygame
import sys
from tilesheet import Tiles




class World():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.bg_color = pygame.Color("White")

        self.tiles = Tiles("res/tmsSprites.png", 32, 32, 2, 4)

    def handle_events(self):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.window.fill(self.bg_color)
        # self.tiles.draw(self.window)
        self.window.blit(self.tiles.grab_tile(2, 0), (200,200))
        pygame.display.flip()


class Entity():

    def __init__(self, name, hp, mana, x, y ):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.x = x
        self.y = y

    def draw(self, window_catalyst, filename, x, y):
        window_catalyst.blit(filename, (x, y))

    def update(self, y):
        gravity = 0.2
        y += gravity

