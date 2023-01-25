import sys
import pygame

pygame.init()

width = 716
height = 714

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("SOUNDS")

my_color = (10, 240, 200)

pygame.mixer.music.load("PYGAME/Sounds/Sever.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1, 0.0)
#pygame.mixer.music.rewind()
#pygame.mixer.music.pause()
#pygame.mixer.music.stop()
#pygame.mixer.music.fadeout()

cassis = pygame.image.load("PYGAME/Images/Cassis cover.png")
ak = cassis.get_rect()
ak.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)
    surface.blit(cassis, ak)

    pygame.display.update()