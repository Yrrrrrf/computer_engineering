import sys
import pygame

pygame.init()

width = 1200
height = 1000

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("MOVE IMAGE WITH KEYBOARD AND COORDINATES")

my_color = (255, 160, 40)
white = (255, 255, 255)
font = pygame.font.Font("freesansbold.ttf", 16)

image = pygame.image.load("PYGAME/Images/Aorus.png")
rect = image.get_rect()
rect.center = (width/2, height/2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#MOVE IMAGE COMANDS
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] or pressed[119]:
        rect.y -=1

    if pressed[pygame.K_DOWN] or pressed[115]:
        rect.y +=1

    if pressed[pygame.K_LEFT] or pressed[97]:
        rect.x -=1

    if pressed[pygame.K_RIGHT] or pressed[100]:
        rect.x +=1

#MOVE IMAGE LIMITS
    if rect.top < -40:
        rect.top = -40

    if rect.bottom > (height + 40):
        rect.bottom = (height + 40)

    if rect.left < -100:
        rect.left = -100
        
    if rect.right > (width + 100):
        rect.right = (width + 100)

    pos_x, pos_y = rect.x, rect.y
    c = ("X: %s     Y: %s" %(pos_x, pos_y))
    coordinates = font.render(c, True, white)

    surface.fill(my_color)
    surface.blit(image, rect)
    surface.blit(coordinates, (pos_x + 200, pos_y + 200))
    pygame.display.update()