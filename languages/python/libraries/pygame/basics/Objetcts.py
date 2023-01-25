import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("OBJETCTS")

my_color = (255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(255, 0, 255)
cyan = pygame.Color(0, 255, 255)
yellow = pygame.Color(255, 255, 0)

rect = pygame.Rect(100, 150, 220, 260)
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)
#############################################################DIBUJAR FIGURAS
    pygame.draw.rect(surface, purple, rect)
    pygame.draw.rect(surface, cyan, (10, 20, 60, 40))

    pygame.draw.circle(surface, yellow,(200, 300), 100)
    pygame.draw.line(surface, blue, (100, 100), (300, 300), 12)

    pygame.draw.polygon(surface, red, ((30, 50),(100, 300),(400, 400)))

    pygame.draw.polygon(surface, green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

    pygame.display.update()