import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("JUEGO")

my_color = (10, 240, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

            if event.button == 1:
                print("Clic izquierdo")
            if event.button == 2:
                print("Clic rueda")
            if event.button == 3:
                print("Clic derecho")
            if event.button == 4:
                print("Scroll arriba")
            if event.button == 5:
                print("Scroll abajo")

        if event.type == pygame.MOUSEBUTTONUP:
            #print("Boton liberado")
            pass

    surface.fill(my_color)
    pygame.display.update()