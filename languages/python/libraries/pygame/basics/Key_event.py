import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("KEY EVENT")

my_color = (10, 240, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(event)
            
            if event.key == 119 or event.key == pygame.K_UP:
                print("ARRIBA")

            if event.key == 115 or event.key == pygame.K_DOWN:
                print("ABAJO")

            if event.key == 97 or event.key == pygame.K_LEFT:
                print("IZQUIERDA")

            if event.key == 100 or event.key == pygame.K_RIGHT:
                print("DERECHA")

        if event.type == pygame.KEYUP:
            #print("Tecla liberada")
            pass

    surface.fill(my_color)
    pygame.display.update()