import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("KEY PRESSED")

my_color = (10, 240, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        print("ARRIBA")

    if pressed[pygame.K_DOWN]:
        print("ABAJO")

    if pressed[pygame.K_LEFT]:
        print("IZQUIERDA")

    if pressed[pygame.K_RIGHT]:
        print("DERECHA")

    surface.fill(my_color)
    pygame.display.update()