import pygame
from pygame.draw import *
from random import randint
from math import cos, sin
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Поймай шарик")


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
t = 0

# шарики типа 1 --------------------------------------------
# ----------------------------------------------------------

def ball_1_xyz():
    
    global x1, y1, r1, color
    x1 = randint(100,1100)
    y1 = randint(100,800)
    r1 = randint(30,50)
    color = COLORS[randint(0, 5)]

def ball_type_1():
    
    circle(screen, color, (x1, y1), r1)

def delt1():  
    global delta1 
    (X, Y) = event.pos
    delta1 = (x1 - X)^2 + (y1 - Y)^2 - r1^2

# шарики типа 2 --------------------------------------------
# ----------------------------------------------------------

def ball_type_2():
    global x2, y2, r2
    m = 1/6
    h = 7/6
    x2 = int(800 + 100*((m+1)*cos(m*t) - h*cos((m+1)*t)))
    y2 = int(500 + 100*((m+1)*sin(m*t) - h*sin((m+1)*t)))
    r2 = 30
    circle (screen, YELLOW, (x2, y2), r2)
    circle (screen, RED, (x2-10, y2-10), 4)
    circle (screen, RED, (x2+10, y2-10), 4)
    circle (screen, BLACK, (x2-10, y2-10), 2)
    circle (screen, BLACK, (x2+10, y2-10), 2)
    polygon (screen, BLACK, [(x2-16, y2-18),(x2-16, y2-16),(x2-4, y2-12),(x2-4, y2-14)])
    polygon (screen, BLACK, [(x2+4, y2-14),(x2+4, y2-12),(x2+16, y2-16),(x2+16, y2-18)])
    
def delt2():  
    global delta2 
    (X, Y) = event.pos
    delta2 = (x2 - X)^2 + (y2 - Y)^2 - r2^2

# ----------------------------------------------------------

while not finished:   
    my_font = pygame.font.match_font("Arial")
    f1 = pygame.font.Font(my_font, 36)
    text1 = f1.render("Счет " + str(score), True, (255,255,255))
    
    ball_1_xyz()
    for i in range(60):
        ball_type_1()
        ball_type_2()
       
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    delt1()
                    if delta1 < 0:
                        score += 1
                    delt2()
                    if delta2 < 0:
                        score += 3

        t += 0.1
        screen.blit(text1, (10, 10))
        pygame.display.update()
        screen.fill(BLACK)
                    
pygame.quit()


