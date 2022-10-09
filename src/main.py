import pygame
import sprites


# Initialization
pygame.init()


# Window Handling
pygame.display.set_caption("That Magical Swordsmen")
window = pygame.display.set_mode((800, 600))
BG = (50, 50, 50)
BLACK = (0,0,0)

# Sprites
player_img = pygame.image.load("res/tmdS.png").convert_alpha()
Sprite = sprites.Spritesheet(player_img)


player_frame_0 = Sprite.get_sprite(0, 32, 32, 3)
player_frame_2 = Sprite.get_sprite(2, 32, 32, 3)
run = True
while run:
    window.fill(BG)
    window.blit(player_frame_0, (0,0))
    window.blit(player_frame_2, (140, 0))
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()