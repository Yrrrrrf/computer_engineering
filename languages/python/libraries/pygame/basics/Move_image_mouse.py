import sys
import pygame

pygame.init()

width = 1200
height = 1000

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("MOVE IMAGE WOTH MOUSE")

my_color = (247, 159, 40)

aorus = pygame.image.load("PYGAME/Images/Aorus.png")
rect = aorus.get_rect()
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect.center = pygame.mouse.get_pos()

    surface.fill(my_color)
    surface.blit(aorus, (rect))

    pygame.display.update()