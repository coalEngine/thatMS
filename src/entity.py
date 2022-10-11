import pygame
import sprites
pygame.init()

class Entity():
    def __init__(self, Sprite, nM, HP, MP, ST, S):
        self.character = Sprite
        self.name = nM
        self.health_points = HP
        self.mana_points = MP
        self.stamina = ST
        self.x = 0
        self.y = 0
        self.gravity = 2
        self.speed = S
    def spawn(self, x, y, sprite, window):
        window.blit(sprite, (x, y))

    def destroy(self):
        pass