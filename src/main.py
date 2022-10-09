import pygame


# Initialization
pygame.init()


# Window Handling
pygame.display.set_caption("That Magical Swordsmen")
window = pygame.display.set_mode((800, 600))
BG = (50, 50, 50)
BLACK = (0,0,0)

# Sprites
player_img = pygame.image.load("res/tmdS.png").convert_alpha()


def get_sprite(sheet, width, height, scale):
    img = pygame.Surface((width, height)).convert_alpha()
    img.blit(sheet, (0,0), (0,0,width,height))
    img = pygame.transform.scale(img, (width * scale, height * scale))
    return img


frame_0 = get_sprite(player_img, 32, 32, 3)
run = True
while run:
    window.fill(BG)
    window.blit(frame_0, (0,0))
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()