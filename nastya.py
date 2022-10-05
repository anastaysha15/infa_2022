import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))

circle(screen, (0, 0, 255), (100, 100), 5)

pygame.display.update()
while True:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()