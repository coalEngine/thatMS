import pygame

class Spritesheet():
    def __init__(self, img):
        self.sheet = img

    def get_sprite(self, frame, width, height, scale):
        img = pygame.Surface((width, height)).convert_alpha()
        img.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        img = pygame.transform.scale(img, (width * scale, height * scale))
        return img

    def play_animation(self, frames, width, height, scale, runtime):
        pass