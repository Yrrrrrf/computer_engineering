import pygame
import random

pygame.init()

width = 1200
height = 1000

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

centro = (width//2, height//2)
j_altura = height//6
margens = height//20
margeni = height - margens
p_pos_x = width//2
p_pos_y = height//2

j1_pos_y = 5 * height//12
j2_pos_y = 5 * height//12

puntos_j1 = 0
puntos_j2 = 0

#COLORES
black = (0, 0, 0)
white = (255, 255, 255)
grey = (40, 40, 40)

font = pygame.font.Font("freesansbold.ttf", 48)
fontt = pygame.font.Font("freesansbold.ttf", 20)

game_over = False
move = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    surface.fill(black)
    
    #DISEÑO DEL CAMPO
    pygame.draw.line(surface, grey, (0, margeni), (width, margeni), 3)
    pygame.draw.line(surface, grey, (0, margens), (width, margens), 3)
    pygame.draw.line(surface, grey, (width//2, margens), (width//2, margeni), 3)
    pygame.draw.circle(surface, grey, centro, width//10, 3)

    #POSICIÓN INICIAL
    j1 = pygame.draw.rect(surface, white, ((margens, j1_pos_y), (width//100, j_altura)))
    j2 = pygame.draw.rect(surface, white, ((width - width//100 - margens, j2_pos_y), (width//100, j_altura)))
    ball = pygame.draw.circle(surface, white, (p_pos_x, p_pos_y), width//80)

    pressed = pygame.key.get_pressed()
    #MOVIMIENTO JUGADOR 1
    if pressed[87] or pressed[119]:
        j1_pos_y -=3
    if pressed[83]or pressed[115]:
        j1_pos_y +=3

    if j1_pos_y <= margens:
        j1_pos_y = margens
    if j1_pos_y >= height*(5/6) - margens:
        j1_pos_y = height*(5/6) - margens

    #MOVIMIENTO JUGADOR 2
    if pressed[pygame.K_UP]:
        j2_pos_y -=3
    if pressed[pygame.K_DOWN]:
        j2_pos_y +=3

    if j2_pos_y <= margens:
        j2_pos_y = margens
    if j2_pos_y >= height*(5/6) - margens:
        j2_pos_y = height*(5/6) - margens

    #MOVIMIENTO BALL
    if move == 0:
        x = random.randrange(-4, 5, 4)
        y = random.randrange(-4, 5, 2)
        if x == 0 or x == 1 or x == -1: move = 0
        elif y == 0 or y == 1 or y == -1: move = 0
        else: move = 1
    p_pos_x += x
    p_pos_y += y

    if p_pos_y > margeni or p_pos_y < margens:
        y = -y

    if ball.colliderect(j1):
        p_pos_x = margens + width//100 + 20
        x = -x
    if ball.colliderect(j2):
        p_pos_x = width - width//100 - margens - 20
        x = -x

    #PUNTIACIONES
    if p_pos_x < 0:
        puntos_j2 +=1
        move = 0
        p_pos_x = width//2
        p_pos_y = height//2
    if p_pos_x > width:
        puntos_j1 +=1
        move = 0
        p_pos_x = width//2
        p_pos_y = height//2

    pj1 = "Puntos: {}".format(puntos_j1)
    pj2 = "Puntos: {}".format(puntos_j2)
    
    titulo = font.render("PONG", True, white)
    text = titulo.get_rect()
    text.center = (width//2, margens//2)

    j1t = fontt.render(pj1, True, white)
    j2t = fontt.render(pj2, True, white)

    surface.blit(titulo, text)
    surface.blit(j1t, (margens, margens//2))
    surface.blit(j2t, (width - margens*3, margens//2))

    if puntos_j1 == 5:
        victory = font.render("GANA JUGADOR 1", True, white)
    elif puntos_j2 == 5:
        victory = font.render("GANA JUGADOR 2", True, white)
    if puntos_j1 == 5 or puntos_j2 == 5:
        victorytext = victory.get_rect()
        victorytext.center = (width//2, height//2 - margens)
        surface.blit(victory, victorytext)
        p_pos_x = width//2
        p_pos_y = height//2
        x = 0
        y = 0

        ng = fontt.render("Presiona R para volver a jugar", True, white)
        ngt = ng.get_rect()
        ngt.center = (width//2, height//2 + margens)
        surface.blit(ng, ngt)

        if pressed[82] or pressed[114]:
            move = 0
            puntos_j1 = 0
            puntos_j2 = 0

    clock.tick(60)
    pygame.display.flip()