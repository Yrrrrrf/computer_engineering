import sys
import pygame

pygame.init()

width = 1200
height = 1000

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("IMAGES")

my_color = (247, 159, 40)
white = (255, 255, 255)
font = pygame.font.Font("freesansbold.ttf", 16)

aorus = pygame.image.load("PYGAME/Images/Aorus.png")
rect = aorus.get_rect()
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect.center = pygame.mouse.get_pos()
    pos_x, pos_y = rect.x, rect.y
    c = ("X: %s     Y: %s" %(pos_x, pos_y))
    coordinates = font.render(c, True, white)

    surface.fill(my_color)
    surface.blit(aorus, (rect))
    surface.blit(coordinates, (pos_x + 200, pos_y + 200))
    pygame.display.update()