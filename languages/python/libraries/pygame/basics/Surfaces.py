import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("SURFACES")

white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
cyan = pygame.Color(0, 255, 255)
purple = pygame.Color(255, 0, 255)
yellow = pygame.Color(255, 255, 0)
black = pygame.Color(0, 0, 0)
my_color = (10, 240, 200)

surface2 = pygame.Surface((200, 200))
surface2.fill(red)

r = surface2.get_rect()
r.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    
    surface.blit(surface2, (r))

    pygame.draw.rect(surface2, purple, (50, 60, 60, 80))

    pygame.display.update()