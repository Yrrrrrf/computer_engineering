import sys
import pygame

pygame.init()

width = 600
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("UPDATE TEXT")

white = pygame.Color(255, 255, 255)
my_color = (247, 159, 40)

font = pygame.font.Font("freesansbold.ttf", 60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)

    time = pygame.time.get_ticks()//1000
    txt = font.render(str(time), True, white)
    text = txt.get_rect()
    text.center = (width//2, height//2)

    surface.blit(txt, (text))
    
    pygame.display.update()