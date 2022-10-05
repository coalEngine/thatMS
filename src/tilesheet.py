import pygame


class Tiles:
    def __init__(self, file_name, width, height, rows, columns):
        img = pygame.image.load(file_name).convert()
        self.tile_table = []
        for tile_x in range(0, columns):
            line = []
            self.tile_table.append(line)
            for tile_y in range(0, rows):
                rect = (tile_x * width, tile_y * height, width, height)
                line.append(img.subsurface(rect))

    def grab_tile(self, x, y):
        return self.tile_table[x][y]
    def draw(self, window):
        for x, row in enumerate(self.tile_table):
            for y, tile in enumerate(row):
                window.blit(tile, (x * 24, y * 24))