import pygame
from math import sin

def main():
    FPS = 20
    WIDTH, HEIGHT = 720, 480
    RESOLUTION = 20
    FONT = 'fonts/AzeretMono-Light.ttf'
    FONTSIZE = int(HEIGHT / RESOLUTION)
    LINEHEIGHT = FONTSIZE
    INDENT = RESOLUTION
    LINESEP = RESOLUTION / 4
    time = 0
    speed = 0.05
    speed_step = 0.02
    amplitude = 50
    amplitude_step = 5
    periodicity = 10
    periodicity_step = 1
    x_origin = int(WIDTH * 2 / 3)
    x_step = int(WIDTH / (4 * RESOLUTION))
    dx = 2

    def sine_wave(x, y, time):
        return y + amplitude * sin(periodicity * x + time)

    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.Font(FONT, FONTSIZE)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sine Wave Animation")

    running = True
    while running:

        screen.fill('black')
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            amplitude -= amplitude_step
        if keys[pygame.K_UP]:
            amplitude += amplitude_step

        if keys[pygame.K_LEFT]:
            periodicity -= periodicity_step
        if keys[pygame.K_RIGHT]:
            periodicity += periodicity_step

        if keys[pygame.K_s]:
            speed -= speed_step
        if keys[pygame.K_w]:
            speed += speed_step

        if keys[pygame.K_a]:
            x_origin -= int((x_step + WIDTH) % WIDTH)
        if keys[pygame.K_d]:
            x_origin += int((x_step + WIDTH) % WIDTH)

        if keys[pygame.K_q]:
            dx -= 1
        if keys[pygame.K_e]:
            dx += 1

        time += speed
        for x in range(0, x_origin, dx):
            y1 = sine_wave(x / WIDTH, HEIGHT / 2, time)
            y2 = sine_wave((x + dx) / WIDTH, HEIGHT / 2, time)
            pygame.draw.line(screen, 'white', (x, y1), (x + dx, y2), 1)

        y_pos = sine_wave(x_origin / WIDTH, HEIGHT / 2, time)
        center = (x_origin, y_pos)
        pygame.draw.circle(screen, 'white', center, 2)

        amplitude_label = font.render(f"Amplitude: {amplitude}", 1, 'white')
        periodicity_label = font.render(f"Periodicity: {periodicity}", 1, 'white')
        speed_label = font.render(f"Speed: {round(speed, 2)}", 1, 'white')

        screen.blit(amplitude_label, (INDENT, (LINESEP + LINEHEIGHT * 0)))
        screen.blit(periodicity_label, (INDENT, (LINESEP + LINEHEIGHT) * 1))
        screen.blit(speed_label, (INDENT, (LINESEP + LINEHEIGHT) * 2))
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

if __name__ == "__main__":
    main()
