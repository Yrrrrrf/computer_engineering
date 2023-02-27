# [pygame](https://www.pygame.org/news)

Is a [python](/languages/python/python.md) library that allows you to **create games**.

## Installation

```bash
pip install pygame
```

## [Usage](pygame.ipynb)

```python
import pygame  # import the library


pygame.init()  # initialize pygame
screen = pygame.display.set_mode((720, 480))  # create a screen
pygame.display.set_caption("My Game")  # set the title of the windoW
clock = pygame.time.Clock()  # create a clock object

# game loop
running = True
while running:
    clock.tick(60)  # set the fps to 60
    for event in pygame.event.get():  # get all the events
        if event.type == pygame.QUIT:  # if the event is QUIT
            running = False  # stop the game loop
    screen.fill((0, 0, 0))  # fill the screen with black
    pygame.display.flip()  # update the screen

pygame.quit()  # quit pygame
```
 
