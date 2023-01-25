import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("RECTANGLES")

my_color = (255, 255, 255)
purple = pygame.Color(255, 0, 255)
cyan = pygame.Color(0, 255, 255)

rect = pygame.Rect(100, 150, 120, 60)
rect.center = (width//2, height//2) 
print(rect.x)
print(rect.y)

rect2 = (100, 100, 80, 120)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)

    pygame.draw.rect(surface, purple, rect)
    pygame.draw.rect(surface, cyan, rect2)

    pygame.display.update()