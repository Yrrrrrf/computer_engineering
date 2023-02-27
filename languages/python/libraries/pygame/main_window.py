import pygame



pygame.init()  # initialize pygame

# Set Window
screen = pygame.display.set_mode((720, 480))  # create a screen
pygame.display.set_caption("My Game")  # set the title of the windoW
bg_color: tuple = (64, 64, 64)  # background color

# Set Icon
icon = pygame.image.load('languages/python/libraries/pygame/resources/img/star.png')  # load the icon
pygame.display.set_icon(icon)  # set the icon

# Set Clock (FPS)
clock = pygame.time.Clock()  # create a clock object

pygame.display.flip()  # update the screen once to show the icon
# Game Loop
running = True
while running:
    clock.tick(60)  # set the fps to 60
    for event in pygame.event.get():  # get all the events
        if event.type == pygame.QUIT:  # if the event is QUIT
            running = False  # stop the game loop
    screen.fill(bg_color)  # fill the screen with black
    pygame.display.flip()  # update the screen

pygame.quit()  # quit pygame

