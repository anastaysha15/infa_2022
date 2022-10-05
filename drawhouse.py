from pygame.draw import*

def draw_house (screen, x, y):
    
    
    rect (screen, (100,100,110), (x,y,200,150))
    rect (screen, (0,0,0), (x,y,200,150),2)
    rect (screen, (0,130,255), (x+66,y+46,70,60))
    rect (screen, (250,120,0), (x+66,y+46,70,60), 2)
    polygon (screen, (255,0,0), [(x,y),(x+100,y-100),(x+200,y),(x,y)])
    polygon (screen, (0,0,0),[(x,y), (x+100,y-100), (x+200,y),(x,y)],2)
    
if __name__ == "__main__":
    import pygame
    from pygame.draw import *

    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((1000, 1000))

    draw_house(screen, 100, 300)

    pygame.display.update()
    while True:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()