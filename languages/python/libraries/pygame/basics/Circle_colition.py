import sys
import pygame
import math

pygame.init()

width = 1200
height = 1000

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("IMAGES COLITION")

my_color = (40, 40, 40)
white = (255, 255, 255)
red = (255, 0, 0)
font = pygame.font.Font("freesansbold.ttf", 60)
f = pygame.font.Font("freesansbold.ttf", 36)

earth = pygame.image.load("PYGAME/Images/Earth.jpg")
rect1 = earth.get_rect()
rect1.center = (width//2, height//2)
#Earth.jpg tiene 240x240p

asteroid = pygame.image.load("PYGAME/Images/Asteroid.png")
rect2 = asteroid.get_rect()
rect2.center = (width//2, height//2)
#Asteroid.png tiene 394x394p

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect2.center = pygame.mouse.get_pos()

    surface.fill(my_color)
    surface.blit(earth, rect1)
    surface.blit(asteroid, rect2)
    
#dist = raiz cuadrada de = (x*x + y*y)
#x = x1 -x2
#y = y1 - y2
    dist = math.hypot((rect1.x + 120) - (rect2.x + 197), (rect1.y + 120) - (rect2.y + 197))

#LONGUITUD DE LA LINEA
    pygame.draw.line(surface, red, rect1.center, rect2.center, 2)
    m = str(dist) + (" pixeles")
    t = f.render(m, True, white)
    rect3 = t.get_rect()
    rect3. center = (width//2, 150)
    surface.blit(t, rect3)

#COLISIÓN DE IMAGENES (CIRCULOS)
    message = ""
    if dist < (317):
        message = "Existe una colisión!"

    text = font.render(message, True, white)
    rect4 = text.get_rect()
    rect4. center = (width//2, 100)
    surface.blit(text, rect4)

    pygame.display.update()