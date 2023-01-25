import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("COLORS")

#RGB RED GREEN BLUE
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
cyan = pygame.Color(0, 255, 255)
purple = pygame.Color(255, 0, 255)
yellow = pygame.Color(255, 255, 0)
black = pygame.Color(0, 0, 0)

#TAMBIEN SE PUEDEN CREAR COLORES CON TUPLAS
my_color = (200, 90, 130) #ENTRE ROSA Y ROJO


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)
    pygame.display.update()