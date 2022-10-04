import pygame


pygame.init()

class Entity():

    def __init__(self, name, hp, mana, x, y ):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.x = x
        self.y = y

    def draw(self, window_1, filename, x, y):
        window_1.blit(filename, (x, y))

    def update(self, time, y):
        gravity = 0.2
        y += gravity

