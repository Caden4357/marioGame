import pygame 
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mariah')


sun_image = pygame.image.load("_python/mario/images/sun.png")
bg_image = pygame.image.load("_python/mario/images/sky.png")

run = True

class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        for num in range(1,5):
            img_right = pygame.image.load(f'_python/mario/images/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40,80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
    def update(self):
        dx = 0 
        dy = 0
        walk_cooldown = 5


        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y =- 15
            self.jumped = True
        if key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction =- 1
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            
            if self.direction ==- 1:
                self.image = self.images_left[self.index]



        #Animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            self.image = self.images_right[self.index]
            if self.direction == 1:
                self.image = self.images_right[self.index]
            
            if self.direction ==- 1:
                self.image = self.images_left[self.index]




        #gravity 
        self.vel_y+=1
        if self.vel_y > 10:
            self.vel_y = 10

        dy += self.vel_y

        #check for collision
        for tile in world.tile_list:
            #x collision 
            if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                dx = 0

            #y collisions 
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #im jumping when vel = 0
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy=tile[1].top - self.rect.bottom
                    self.vel_y = 0




        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0



        screen.blit(self.image, self.rect) 
        pygame.draw.rect(screen, (255,255,255), self.rect,2)
blob_group = pygame.sprite.Group()
class World():
    def __init__(self, data):
        self.tile_list = []
        dirt_image = pygame.image.load("_python/mario/images/dirt.png")
        grass_image = pygame.image.load("_python/mario/images/grass.png")
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_image,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_image,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)

                if tile == 3:
                    blob = Enemy(col_count*tile_size, row_count*tile_size)
                    blob_group.add(blob)


                col_count += 1
            row_count += 1

    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255,255,255), tile[1],2)




class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("_python/mario/images/blob.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y







world_data = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,8,1],
[1,0,0,0,0,2,0,0,0,0,0,7,0,0,0,0,0,0,2,1,1],
[1,0,0,0,0,0,0,0,0,2,2,0,7,0,5,0,0,0,0,1,1],
[1,0,0,0,0,0,0,0,5,0,0,0,2,2,0,0,0,0,0,1,1],
[1,7,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,0,0,0,0,0,0,0,0,0,0,7,0,0,7,0,0,0,0,1,1],
[1,0,2,0,0,7,0,7,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,0,0,2,0,0,4,0,0,0,0,3,0,0,3,0,0,0,0,1,1],
[1,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,0,0,0,0,0,0,0,0,0,7,0,7,0,0,0,0,2,0,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,0,0,0,0,0,0,0,0,0,2,0,2,0,2,2,2,2,1,1,1],
[1,0,0,0,0,0,2,2,2,6,6,6,6,6,1,1,1,1,1,1,1],
[1,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],

]



tile_size = 50

def draw_grid():
    for line in range(0,20):
        pygame.draw.line(screen,(255,255,255), (0,line*tile_size), (screen_width,line*tile_size))
        pygame.draw.line(screen,(255,255,255), (line*tile_size,0), (line*tile_size, screen_width))


player = Player(200, screen_height-180)

blob_group = pygame.sprite.Group()

world = World(world_data)

while run:
    clock.tick(fps)
    screen.blit(bg_image,(0,0))
    screen.blit(sun_image,(100,100))
    world.draw()
    blob_group.draw(screen)

    # draw_grid()
    player.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()