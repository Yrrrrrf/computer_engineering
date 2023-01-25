#HOLI :v ME DICES SI VES ESTO xd
import sys
import pygame
import numpy as np
import time

pygame.init()

width = 1000
height = 1000

screen = pygame.display.set_mode((height, width))
#DISPLAY BACKGROUNG
background = (25, 25, 25)
screen.fill(background)

# NÚMERO DE CELDAS
nxC = 50
nyC = 50
# TAMAÑO DE LAS CELDAS
dimCW = width / nxC
dimCH = height / nyC

# ESTADO DE LAS CELDAS
# 1 = VIVA, 0 = MUERTA
gameState = np.zeros((nxC, nyC))

#ESTADOS INICIALES:
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

#PAUSAR EJECUCIÓN. PARA EDIRAR CONDICIONES INICIALES
pauseExect = False

# BUCLE EN EJECUCIÓN
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    newGameState = np.copy(gameState)

    screen.fill(background)
    time.sleep(0.1)

    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        
        mouseClick = pygame.mouse.get_pressed()
        
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]

    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pauseExect:

                #CALCULAR EL NÚMERO DE VECINOS CERCANOS
                n_neigh = gameState[(x-1) % nxC, (y-1) % nyC] + \
                          gameState[(x)   % nxC, (y-1) % nyC] + \
                          gameState[(x+1) % nxC, (y-1) % nyC] + \
                          gameState[(x-1) % nxC,   (y) % nyC] + \
                          gameState[(x+1) % nxC,   (y) % nyC] + \
                          gameState[(x-1) % nxC, (y+1) % nyC] + \
                          gameState[(x)   % nxC, (y+1) % nyC] + \
                          gameState[(x+1) % nxC, (y+1) % nyC]

        #REGLA 1 : UNA CÉLULA MUERTA VUELVE A LA VIDA CON EXACTAMENTE 3 VECINAS VIVOS, "REVIVE".
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

        #REGLA 2: UN CÉLULA VIVA CON MENOS DE 2 O MÁS DE 3 VECINAS VIVAS, "MUERE".
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            #POLIGONO DE CADA CELDA A DIBUJAR
            poly = [((x) * dimCW, (y) * dimCH),
                    ((x + 1) * dimCW, (y) * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x) * dimCW, (y + 1) * dimCH)]

            # ESTADO DE LAS CELDAS
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = np.copy(newGameState)

    pygame.display.flip()

