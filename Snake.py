import pygame
from pygame import color
from pygame.constants import WINDOWHITTEST
from pygame import RESIZABLE
import random
import time
from pygame.time import Clock
pygame.init()
pygame.display.set_caption("Snake by Vadim")
GRAY = (40, 40, 40)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 150, 0)
LIGHTGRAY = (80, 80, 80)
clock = pygame.time.Clock()
sc = pygame.display.set_mode((480, 480))
sc.fill(GRAY)
pygame.display.update()
FPS = 7
while True:
    reload = False
    snake = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for p in range(0, 20):
        for i in range(0, 20):
            snake[p].append("o")
    snake[9][9] = "x"
    def printsnake(y, color):
        for f in range(0, 20):
            for h in range(0, 20):
                if snake[f][h] == y:
                    dx = h * 24
                    dy = f * 24
                    pygame.draw.rect(sc, color, (dx, dy, 24, 24))
    dvizh = 0
    apple = True
    m = 1
    tall = 3
    snak = []
    died = False
    mode = "hard"
    while True:
        sc.fill(GRAY)
        press = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and not dvizh == 3 and not press:
                    dvizh = 1
                    press = True
                if event.key == pygame.K_d and not dvizh == 4 and not press:
                    dvizh = 2
                    press = True
                if event.key == pygame.K_s and not dvizh == 1 and not press:
                    dvizh = 3
                    press = True
                if event.key == pygame.K_a and not dvizh == 2 and not press:
                    dvizh = 4
                    press = True
                if event.key == pygame.K_r:
                    reload = True
                if event.key == pygame.K_1:
                    mode = "hard"
                if event.key == pygame.K_2:
                    mode = "easy"
                if event.key == pygame.K_e:
                    apple = True
        for i in range(len(snake)):
            for j in range(len(snake[i])):
                if snake[i][j] == "x":
                    gk = i
                    gp = j
                    a = [gk, gp]
                    snak.append(a)
                    break;
        if apple:
            e = random.randint(0, 19)
            ee = random.randint(0, 19)
            if snake[e][ee] == "o":
                snake[e][ee] = "a"
                apple = False
        if mode == "hard":
            if dvizh == 1:
                if (gk - 1) == -1 or snake[gk - 1][gp] == "z":
                    died = True
                if not died and snake[gk - 1][gp] == "a":
                    tall += 1
                    apple = True
                if not died:
                    snake[gk - 1][gp] = "x"
                    snake[gk][gp] = "z"
            if dvizh == 2:
                if (gp + 1) == 20 or snake[gk][gp + 1] == "z":
                    died = True
                if not died and snake[gk][gp + 1] == "a":
                    tall += 1
                    apple = True
                if not died:
                    snake[gk][gp + 1] = "x"
                    snake[gk][gp] = "z"
            if dvizh == 3:
                if (gk + 1) == 20 or snake[gk + 1][gp] == "z":
                    died = True
                if not died and snake[gk + 1][gp] == "a":
                    tall += 1
                    apple = True
                if not died:
                    snake[gk + 1][gp] = "x"
                    snake[gk][gp] = "z"
            if dvizh == 4:
                if (gp - 1) == -1 or snake[gk][gp - 1] == "z":
                    died = True
                if not died and snake[gk][gp - 1] == "a":
                    tall += 1
                    apple = True
                if not died:
                    snake[gk][gp - 1] = "x"
                    snake[gk][gp] = "z"
        if mode == "easy":
            if dvizh == 1:
                if snake[gk - 1][gp] == "z":
                    died = True
                if not died and snake[gk - 1][gp] == "a":
                    tall += 1
                    apple = True
                if (gk - 1) == -1:
                    snake[19][gp] = "x"
                    snake[gk][gp] = "z"
                elif not died:
                    snake[gk - 1][gp] = "x"
                    snake[gk][gp] = "z"
            if dvizh == 2:
                if not (gp + 1) == 20 and snake[gk][gp + 1] == "z":
                    died = True
                if not (gp + 1) == 20 and not died and snake[gk][gp + 1] == "a":
                    tall += 1
                    apple = True
                if (gp + 1) == 20:
                    snake[gk][0] = "x"
                    snake[gk][gp] = "z"
                elif not died:
                    snake[gk][gp + 1] = "x"
                    snake[gk][gp] = "z"
            if dvizh == 3:
                if not (gk + 1) == 20 and snake[gk + 1][gp] == "z":
                    died = True
                if not (gk + 1) == 20 and not died and snake[gk + 1][gp] == "a":
                    tall += 1
                    apple = True
                if (gk + 1) == 20:
                    snake[0][gp] = "x"
                    snake[gk][gp] = "z"
                elif not died:
                    snake[gk + 1][gp] = "x"
                    snake[gk][gp] = "z"
            if dvizh == 4:
                if not (gp - 1) == -1 and snake[gk][gp - 1] == "z":
                    died = True
                if not (gp - 1) == -1 and not died and snake[gk][gp - 1] == "a":
                    tall += 1
                    apple = True
                if (gp - 1) == -1:
                    snake[gk][19] = "x"
                    snake[gk][gp] = "z"
                elif not died:
                    snake[gk][gp - 1] = "x"
                    snake[gk][gp] = "z"
        if len(snak) > tall:
            snak.remove(snak[0])
        if len(snak) == tall:
            snake[snak[0][0]][snak[0][1]] = "o"
        printsnake("x", GREEN)
        printsnake("z", DARKGREEN)
        printsnake("a", RED)
        if died:
            sc.fill(GRAY)
            fontObj = pygame.font.Font(None, 40)
            textSurfaceObj = fontObj.render('You score is: ' + str(tall), True, LIGHTGRAY, GRAY)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (240, 240)
            sc.blit(textSurfaceObj, textRectObj)
            fontObj = pygame.font.Font(None, 20)
            textSurfaceObj = fontObj.render('Press "R" to reload', True, LIGHTGRAY, GRAY)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (240, 280)
            sc.blit(textSurfaceObj, textRectObj)
            if reload:
                break;
        pygame.display.update()
        clock.tick(FPS)
