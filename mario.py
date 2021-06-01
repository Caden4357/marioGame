import pygame 
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mariah')


sun_image = pygame.image.load("_python/mario/images/sun.png")
bg_image = pygame.image.load("_python/mario/images/sky.png")

run = True
title_size = 200



class world():
    def __init__(self, data):
        self.tile_list = []
        dirt_image = sun_image = pygame.image.load("_python/mario/images/dirt.png")
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_image,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img.rect.x = col_count*tile_size
                    img.rect.y = col_count*tile_size
                    tile = (img,img_rect)
                    self.tile_list.append()







world_data = [
[1,1,1,1,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,1,1,1,1],
]





def draw_grid():
    for line in range(0,6):
        pygame.draw.line(screen,(255,255,255), (0,line*title_size), (screen_width,line*title_size))
        pygame.draw.line(screen,(255,255,255), (line*title_size,0), (line*title_size, screen_width))
while run:
    screen.blit(bg_image,(0,0))
    screen.blit(sun_image,(100,100))
    draw_grid()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()