import sys
import pygame

pygame.init()

width = 1200
height = 1000

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("MOVE IMAGE WITH KEYBOARD")

my_color = (255, 160, 40)
white = (255, 255, 255)

image = pygame.image.load("PYGAME/Images/Aorus.png")
rect = image.get_rect()
rect.center = (width/2, height/2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] or pressed[119]:
        rect.y -=1

    if pressed[pygame.K_DOWN] or pressed[115]:
        rect.y +=1

    if pressed[pygame.K_LEFT] or pressed[97]:
        rect.x -=1

    if pressed[pygame.K_RIGHT] or pressed[100]:
        rect.x +=1

#CONDICONES DE MOVIMIENTO
#LIMITES DE LA PANTALLA
    if rect.top < -40:
        rect.top = -40

    if rect.bottom > (height + 40):
        rect.bottom = (height + 40)

    if rect.left < -100:
        rect.left = -100

    if rect.right > (width + 100):
        rect.right = (width + 100)

    surface.fill(my_color)
    surface.blit(image, rect)
    pygame.display.update()