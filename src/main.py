import pygame, sys
import entity
import sprites
from settings import *

# Initialization


class Game():
    def __init__(self,):
        pygame.init()
        # Window Handling
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.name = pygame.display.set_caption("Traveling Magical Swordsmen")
        self.BG = (50, 50, 50)

    def run(self):
        while True:
            self.screen.fill(self.BG)

            # Update Animation
            current_time = pygame.time.get_ticks()

            if current_time - last_Time >= animation_runtime:
                frame += 1
                last_Time = current_time
                if frame >= len(animation_list[action]):
                    frame = 0

            Player.y += Player.gravity
            if Player.y >= 504:
                Player.gravity = 0
                Player.y = 504

            Player.spawn(Player.x, Player.y, animation_list[action][frame], window)

            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evt.type == pygame.KEYDOWN:
                    if evt.key == pygame.K_d:
                        action = 0
                        Player.x += Player.speed
                    if evt.key == pygame.K_a:
                        action = 1
                        Player.x -= Player.speed
            self.screen.fill(self.BG)
            self.clock.tick(FPS)
            self.name.screen = self.name


# Sprites
player_img = pygame.image.load("gfx/art/tmdS.png").convert_alpha()
Sprite = sprites.Spritesheet(player_img)


# Animation
animation_list = []
animation_steps = [2, 2]
action = 0
last_Time = pygame.time.get_ticks()
animation_runtime = 1000
frame = 0
step_counter = 0

# Entity
Player = entity.Entity(Sprite, "tms", 100, 100, 100, 6)


for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(Sprite.get_sprite(step_counter, 32, 32, 3))
        step_counter += 1
    animation_list.append(temp_img_list)


if __name__ == "__main__":
    game = Game()
    game.run()