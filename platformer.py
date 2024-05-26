import pygame
from sys import exit
import random

pygame.init()

#player settings

speed = 15
gravity = 1.1
base_fall_rate = 5
going_up = True
jump_frames = 10
if_jump = False

#player setings end

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

class Platform:
    def __init__(self, height, length, x, y, image):
        self.height = height
        self.length = length
        self.x = x
        self.y = y
        self.image = image
class Enemy:
    def __init__(self, speed, image, x, y):
        self.speed = speed
        self.image = image
        self.x = x
        self.y = y

basic_slime = Enemy(5, pygame.image.load("graphics/sprites/basic_slime.png"), 750, 650)
basic_slime.image = pygame.transform.scale(basic_slime.image, (150, 150))
basic_slime_rect = basic_slime.image.get_rect(midbottom = (basic_slime.x, basic_slime.y))

basic_slime2 = Enemy(5, pygame.image.load("graphics/sprites/basic_slime.png"), 1700, 650)
basic_slime2.image = pygame.transform.scale(basic_slime.image, (150, 150))
basic_slime2_rect = basic_slime2.image.get_rect(midbottom = (basic_slime2.x, basic_slime.y))

fast_slime = Enemy(15, pygame.image.load("graphics/sprites/fast_slime.png"), 3000, 650)
fast_slime.image = pygame.transform.scale(fast_slime.image, (150, 150))
fast_slime_rect = fast_slime.image.get_rect(midbottom = (fast_slime.x, fast_slime.y))

basic_slime3 = Enemy(5, pygame.image.load("graphics/sprites/basic_slime.png"), 3000, 650)
basic_slime3.image = pygame.transform.scale(basic_slime3.image, (150, 150))
basic_slime3_rect = basic_slime3.image.get_rect(midbottom = (basic_slime3.x, basic_slime3.y))

fast_slime2 = Enemy(15, pygame.image.load("graphics/sprites/fast_slime.png"), 5000, 650)
fast_slime2.image = pygame.transform.scale(fast_slime2.image, (150, 150))
fast_slime2_rect = fast_slime2.image.get_rect(midbottom = (fast_slime2.x, fast_slime2.y))

winged_slime = Enemy(25, pygame.image.load("graphics/sprites/winged_slime.png"), 6000, 200)
winged_slime.image = pygame.transform.scale(winged_slime.image, (150, 150))
winged_slime_rect = winged_slime.image.get_rect(midbottom = (winged_slime.x, winged_slime.y))

p1 = Platform(0, 100, 750, 200, pygame.image.load("graphics/sprites/platform.png"))
p1.image = pygame.transform.scale(p1.image, (400, 200))
p1_rect = p1.image.get_rect(midtop = (p1.x, p1.y))

p2 = Platform(0, 100, 2000, 150, pygame.image.load("graphics/sprites/platform.png"))
p2.image = pygame.transform.scale(p2.image, (400, 200))
p2_rect = p2.image.get_rect(midtop = (p2.x, p2.y))

p3 = Platform(0, 100, 3000, 400, pygame.image.load("graphics/sprites/platform.png"))
p3.image = pygame.transform.scale(p3.image, (400, 200))
p3_rect = p3.image.get_rect(topleft = (p3.x, p3.y))

p4 = Platform(0, 100, 6000, 400, pygame.image.load("graphics/sprites/platform.png"))
p4.image = pygame.transform.scale(p4.image, (400, 200))
p4_rect = p4.image.get_rect(topleft = (p4.x, p4.y))

p5  = Platform(0, 100, 6400, 200, pygame.image.load("graphics/sprites/platform.png"))
p5.image = pygame.transform.scale(p5.image, (400, 150))
p5_rect = p5.image.get_rect(topleft = (p5.x, p5.y))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ground = pygame.image.load("graphics/ground.png").convert_alpha()
ground = pygame.transform.scale(ground, (1500, 400))
ground_rect = ground.get_rect(midtop = (750,600))

background = pygame.image.load("graphics/background.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

poppy_y_pos = 600
poppy_x_pos = 100
poppy_surface = pygame.image.load("graphics/sprites/Kirbo.png").convert_alpha()
poppy_surface = pygame.transform.scale(poppy_surface, (250, 250))
poppy_rect = poppy_surface.get_rect(midbottom = (poppy_x_pos, poppy_y_pos))

flag_x_pos = 7000

flag = pygame.image.load("graphics/flag.png")
flag = pygame.transform.scale(flag, (200,SCREEN_HEIGHT))
flag_rect =  flag.get_rect(midbottom = (flag_x_pos, 650))

winning_screen = pygame.image.load("graphics/winner.png")
winning_screen = pygame.transform.scale(winning_screen, (SCREEN_WIDTH, SCREEN_HEIGHT))

won = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        p1.x += speed
        p2.x += speed
        p3.x += speed
        p4.x += speed
        p5.x += speed
        basic_slime.x -= -5
        basic_slime2.x -= -5
        fast_slime.x -= -20
        basic_slime3.x -= -5
        fast_slime2.x -= -20
        winged_slime.x -= -10
        flag_x_pos -= -speed
    elif key[pygame.K_d] == True:
        p1.x -= speed
        p2.x -= speed
        p3.x -= speed
        p4.x -= speed
        p5.x -= speed
        basic_slime.x -= 20
        basic_slime2.x -= 20
        fast_slime.x -= 40
        basic_slime3.x -= 15
        fast_slime2.x -= 40
        winged_slime.x -= 60
        flag_x_pos -= speed
    if key[pygame.K_a] == False and key[pygame.K_d] == False:
        basic_slime.x -= 5
        basic_slime2.x -= 5
        fast_slime.x -= 15
        basic_slime3.x -= 5
        fast_slime2.x -= 15
        winged_slime.x -= 25

    if key[pygame.K_SPACE]:
        if_jump = True
        base_fall_rate = 5
    if if_jump == True and jump_frames >= 0:
        poppy_y_pos -= 30
        jump_frames -= 1
    if jump_frames <= 0:
        poppy_y_pos += base_fall_rate
        base_fall_rate *= gravity
    if poppy_rect.colliderect(ground_rect):
        jump_frames = 10
        if_jump = False
        base_fall_rate = 0
    if poppy_rect.colliderect(p1_rect):
        poppy_y_pos = p1.y
        if_jump = False
        base_fall_rate = 0
        jump_frames = 10
    elif poppy_rect.colliderect(p2_rect):
        poppy_y_pos = p2.y
        if_jump = False
        base_fall_rate = 0
        jump_frames = 10
    elif poppy_rect.colliderect(p3_rect):
        poppy_y_pos = p3.y
        if_jump = False
        base_fall_rate = 0
        jump_frames = 10
    elif poppy_rect.colliderect(p4_rect):
        poppy_y_pos = p4.y
        if_jump = False
        base_fall_rate = 0
        jump_frames = 10
    elif poppy_rect.colliderect(p5_rect):
        poppy_y_pos = p5.y
        if_jump = False
        base_fall_rate = 0
        jump_frames = 10

    if poppy_rect.colliderect(ground_rect) == False:
        if base_fall_rate == 0:
            base_fall_rate = 5
        base_fall_rate *= gravity
    if poppy_x_pos <= 100:
        poppy_x_pos = 100
    if poppy_x_pos >= 1400:
        poppy_x_pos = 1400
    if poppy_rect.colliderect(ground_rect) == False and poppy_rect.colliderect(p1_rect) == False and poppy_y_pos :
        base_fall_rate *= gravity
        poppy_y_pos += base_fall_rate
    if poppy_rect.colliderect(ground_rect):
        base_fall_rate = 0
    if poppy_rect.colliderect(flag_rect):
        won = True
    if poppy_rect.colliderect(basic_slime_rect):
        exit()
    elif poppy_rect.colliderect(basic_slime2_rect):
        exit()
    elif poppy_rect.colliderect(basic_slime3_rect):
        exit()
    elif poppy_rect.colliderect(fast_slime_rect):
        exit()
    elif poppy_rect.colliderect(fast_slime2_rect):
        exit()
    elif poppy_rect.colliderect(winged_slime_rect):
        exit()
    if basic_slime.x < 0:
        basic_slime.x =flag_x_pos
    elif basic_slime.x < 0:
        basic_slime2.x = flag_x_pos
    elif basic_slime3.x < 0:
        fast_slime.x = flag_x_pos
    elif fast_slime2.x < 0:
        fast_slime2.x =flag_x_pos
    elif winged_slime.x < 0:
        winged_slime.x =flag_x_pos



    poppy_rect = poppy_surface.get_rect(midbottom=(poppy_x_pos, poppy_y_pos))

    p1_rect = p1.image.get_rect(midtop=(p1.x, p1.y))
    p2_rect = p1.image.get_rect(midtop=(p2.x, p2.y))
    p3_rect = p3.image.get_rect(topleft=(p3.x, p3.y))
    p4_rect = p4.image.get_rect(topleft=(p4.x, p4.y))
    p5_rect = p5.image.get_rect(topleft=(p5.x, p5.y))
    basic_slime_rect = basic_slime.image.get_rect(midbottom=(basic_slime.x, basic_slime.y))
    basic_slime2_rect = basic_slime2.image.get_rect(midbottom=(basic_slime2.x, basic_slime2.y))
    fast_slime_rect = fast_slime.image.get_rect(midbottom=(fast_slime.x, fast_slime.y))
    basic_slime3_rect = basic_slime3.image.get_rect(midbottom=(basic_slime3.x, basic_slime3.y))
    fast_slime2_rect = fast_slime2.image.get_rect(midbottom=(fast_slime2.x, fast_slime2.y))
    winged_slime_rect = winged_slime.image.get_rect(midbottom=(winged_slime.x, winged_slime.y))
    flag_rect = flag.get_rect(midbottom=(flag_x_pos, 650))

    screen.blit(background, (0, 0))
    screen.blit(ground, ground_rect)
    screen.blit(poppy_surface, poppy_rect)
    screen.blit(p1.image, p1_rect)
    screen.blit(p2.image, p2_rect)
    screen.blit(p3.image, p3_rect)
    screen.blit(p4.image, p4_rect)
    screen.blit(p5.image, p5_rect)
    screen.blit(basic_slime.image, basic_slime_rect)
    screen.blit(basic_slime2.image, basic_slime2_rect)
    screen.blit(fast_slime.image, fast_slime_rect)
    screen.blit(basic_slime3.image, basic_slime3_rect)
    screen.blit(fast_slime2.image, fast_slime2_rect)
    screen.blit(winged_slime.image, winged_slime_rect)
    screen.blit(flag, flag_rect)
    if won == True:
        screen.blit(winning_screen, (0,0))
        poppy_x_pos = 200000

    clock.tick(60)
    pygame.display.update()