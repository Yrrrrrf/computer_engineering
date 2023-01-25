import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("TIME")

my_color = (10, 240, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    print(pygame.time.get_ticks()/1000)

    surface.fill(my_color)
    pygame.display.update()