import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("COLITION")

my_color = (255, 255, 255)
cyan = pygame.Color(0, 255, 255)
purple = pygame.Color(255, 0, 255)
yellow = pygame.Color(255, 255, 0)

rect1 = pygame.Rect(0, 0, 100, 80)
rect1.center = (width//2, height//2)

rect2 = pygame.Rect(0, 0, 100, 80)
rect1.center = (width//2, height//2)

font = pygame.font.Font("freesansbold.ttf", 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)
    rect2.center = pygame.mouse.get_pos()
    pygame.draw.rect(surface, cyan, rect1)
    pygame.draw.rect(surface, purple, rect2)

#MENSAJE DE COLISIÓN
    message = ""

#COLITION
    if rect1.colliderect(rect2):
        sound = pygame.mixer.Sound("PYGAME/Sounds/Coin.wav")
        sound.play()
        message = "Existe una colision!"

    text = font.render(message, True, yellow)
    rect3 = text.get_rect()
    rect3.midtop = (width//2, 100)
    surface.blit(text, rect3)

    pygame.display.update()