import pygame
from pygame.draw import *
from drawhouse import draw_house

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))
rect (screen, (0,180,255), (0,0,600,200),)
rect (screen,(0,150,10),(0,200,600,200))
circle (screen, (255,165,0), (50,50),50)
draw_house(screen, 300, 100)

pygame.display.update()
while True:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()