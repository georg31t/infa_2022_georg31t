import pygame
from pygame.draw import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle (screen, YELLOW, (200,200), 150)
circle (screen, RED, (150,150), 20)
circle (screen, RED, (250,150), 20)
circle (screen, BLACK, (150,150), 10)
circle (screen, BLACK, (250,150), 10)
polygon (screen, BLACK, [(120,110),(120,120),(180,140),(180,130)])
polygon (screen, BLACK, [(220,130),(220,140),(280,120),(280,110)])
arc (screen, BLACK, (100, 100, 200, 200), 3.14, 3.14*2, 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
