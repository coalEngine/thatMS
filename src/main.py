import pygame
import sprites
from entity import Entity


# Initialization
pygame.init()


# Window Handling
pygame.display.set_caption("Traveling Magical Swordsmen")
window = pygame.display.set_mode((800, 600))
BG = (50, 50, 50)
BLACK = (0,0,0)

# Sprites
player_img = pygame.image.load("res/tmdS.png").convert_alpha()
Sprite = sprites.Spritesheet(player_img)
# Animation
animation_list = []
player_animation_steps = [2, 2]
action = 0
last_Time = pygame.time.get_ticks()
animation_runtime = 1000
frame = 0
step_counter = 0


for animation in player_animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(Sprite.get_sprite(step_counter, 32, 32, 3))
        step_counter += 1
    animation_list.append(temp_img_list)

run = True
while run:
    window.fill(BG)
    # Update Animation
    current_time = pygame.time.get_ticks()

    if current_time - last_Time >= animation_runtime:
        frame += 1
        last_Time = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    window.blit(animation_list[action][frame], (0, 0))
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            run = False
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_d:
                action = 0
            if evt.key == pygame.K_a:
                action = 1

    pygame.display.update()

pygame.quit()