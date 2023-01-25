import sys
import pygame

pygame.init()

width = 600
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("PAINT TEXT")

white = pygame.Color(255, 255, 255)
my_color = (247, 159, 40)

#OBTENER UNA FUENTE
font = pygame.font.Font("freesansbold.ttf", 60)

#CREAR EL TEXTO A "PINTAR"
t = font.render("HOLA MUNDO!", True, white) #SURFACE
text = t.get_rect()
text.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)
    surface.blit(t, (text))
    pygame.display.update()