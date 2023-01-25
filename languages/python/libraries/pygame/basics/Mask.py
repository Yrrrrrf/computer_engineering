import sys
import pygame

pygame.init()

width = 1200
height = 1000

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("IMAGES")

my_color = (247, 159, 40)
white = (255, 255, 255)
font = pygame.font.Font("freesansbold.ttf", 36)

aorus = pygame.image.load("PYGAME/Images/Aorus.png")
rect = aorus.get_rect()
rect.center = (width//2, height//2)
mask_aorus = pygame.mask.from_surface(aorus)

star = pygame.image.load("PYGAME/Images/Star.png")
rect2 = star.get_rect()
mask_star = pygame.mask.from_surface(star)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect2.center = pygame.mouse.get_pos()

    surface.fill(my_color)
    surface.blit(aorus, rect)
    surface.blit(star, rect2)

    message = ""

    offset = (rect2.x - rect.x, rect2.y - rect.y)
    if mask_aorus.overlap(mask_star, offset):
        message = "Existe una colisión!"

    text = font.render(message, True, white)
    rect3 = text.get_rect()
    rect3.midtop = (width//2, 100)
    surface.blit(text, rect3)

    pygame.display.update()