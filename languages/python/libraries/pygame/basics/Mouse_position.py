import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("MOUSE POSITION")

my_color = (10, 240, 200)
white = (255, 255, 255)

font = pygame.font.Font("freesansbold.ttf", 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pos_x, pos_y = pygame.mouse.get_pos()
    c = ("X: %s     Y: %s" %(pos_x, pos_y))
    coordenadas = font.render(c, True, white)
    centro = coordenadas.get_rect()
    centro.center = (width/2, height/2)

    surface.fill(my_color)
    surface.blit(coordenadas, centro)
    pygame.display.update()