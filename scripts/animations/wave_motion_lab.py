import pygame as pg
from math import tau, sin, cos, tan, atan, atan2
from collections import deque

def counter():
    count = 0
    def countFunction() -> int:
        nonlocal count
        count += 1
        return count
    return countFunction

def linearMapX(x: float, origin: float, scale: float, inverse=False) -> float:
    return (x - origin) / scale if not inverse else (x * scale) + origin

def linearMapY(y: float, origin: float, scale: float, inverse=False) -> float:
    return (origin - y) / scale if not inverse else origin - (y * scale)

def linearMapXY(coors, origin, scale, inverse=False) -> tuple[float, float]:
    return (linearMapX(coors[0], origin[0], scale[0], inverse),
            linearMapY(coors[1], origin[1], scale[1], inverse))

def setWindow(title: str, size: tuple[int, int], icon_file: str) -> pg.surface.Surface:
    pg.display.set_caption(title)
    icon = pg.image.load(icon_file)
    pg.display.set_icon(icon)
    return pg.display.set_mode(size)

def surface(width: int, height: int, color: pg.color.Color) -> pg.surface.Surface:
    surface = pg.Surface((width, height))
    surface.fill(color)
    return surface

def main() -> None:
    FPS = 60
    WIDTH, HEIGHT = 900, 400
    TITLE = "Wave Motion Lab"
    ICON = 'img/math_circle.png' # https://www.flaticon.com/free-icons/trigonometry
    FONT = 'fonts/AzeretMono-SemiBold.ttf'
    FONTSIZE = 16
    LINEHEIGHT = FONTSIZE
    INDENT = FONTSIZE
    # LINEHEIGHT = HEIGHT//FONTSIZE
    # INDENT = WIDTH//LINEHEIGHT

    pg.init()
    clock = pg.time.Clock()
    window = setWindow(TITLE, (WIDTH, HEIGHT), ICON)
    text_font = pg.font.Font(FONT, FONTSIZE)
    def labelBlit(position: tuple[int, int], text: str, font=text_font, surface=window, color='white', antialiasing=True) -> None:
        surface.blit(font.render(text, antialiasing, color), position)

    # origin = (WIDTH//2, HEIGHT//2)
    # scale = (WIDTH//20, HEIGHT//3)
    origin = {'x': WIDTH//2, 'y': HEIGHT//2}
    scale = {'x': WIDTH//20, 'y': HEIGHT//3}
    trigMapX = lambda x, inv=False: linearMapX(x, origin['x'], scale['x'], inv)
    trigMapY = lambda y, inv=False: linearMapY(y, origin['y'], scale['y'], inv)
    trigMapXY = lambda coors, inv=False: linearMapXY(coors, origin, scale, inv)
    rounded = lambda x: round(x, 4)

    photon_img = pg.image.load('img/photon.png')
    dot = pg.transform.rotozoom(photon_img, 0, 1/4)

    frequency = 0
    period = 0
    angle = 0
    angle_diff = deque((0.0, 0.0), maxlen=2)
    dot_pos_x = 0
    x_pos_step = 10
    x_pos_step_change_on_key_press = 1
    angle_update_step = tau/48
    angle_update_step_change_on_key_press = tau/360

    ticks = 0
    running = True
    while running:
        ticks += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_h:
                    x_pos_step -= x_pos_step_change_on_key_press
                if event.key == pg.K_l:
                    x_pos_step += x_pos_step_change_on_key_press
                if event.key == pg.K_j:
                    angle_update_step -= angle_update_step_change_on_key_press
                if event.key == pg.K_k:
                    angle_update_step += angle_update_step_change_on_key_press
            if event.type == pg.KEYUP:
                pass

        angle += angle_update_step

        y = sin(angle)

        if ticks == FPS:
            angle_diff.append(angle)
            angle_len = angle_diff[1] - angle_diff[0]
            frequency = rounded(angle_len/tau)
            period = rounded(1/frequency)
            ticks = 0

        dot_pos_x += x_pos_step
        dot_pos_y = trigMapY(y, inv=True)

        if dot_pos_x > WIDTH: dot_pos_x = 0
        if dot_pos_x < 0: dot_pos_x = WIDTH

        # wavelength, amplitude
        labelBlit((INDENT, LINEHEIGHT*2), f"{frequency} Hz")
        labelBlit((INDENT, LINEHEIGHT*3), f"{period} sec")
        labelBlit((INDENT, HEIGHT-LINEHEIGHT*5), f"{round(angle_update_step, 8):<10} angle_update_step")
        labelBlit((INDENT, HEIGHT-LINEHEIGHT*4), f"{rounded(angle_diff[0]):<10} angle_diff[0]")
        labelBlit((INDENT, HEIGHT-LINEHEIGHT*3), f"{rounded(angle_diff[1]):<10} angle_diff[1]")
        labelBlit((INDENT, HEIGHT-LINEHEIGHT*2), f"{int(angle):<10} angle")

        window.blit(dot, (dot_pos_x, dot_pos_y))
        # line_start_end = ((0, dot_pos_y), (WIDTH, dot_pos_y))
        # pg.draw.line(window, 'white', *line_start_end, 1)
        line_start_end = ((0, origin['y']), (WIDTH, origin['y']))
        pg.draw.line(window, 'white', *line_start_end, 1)
        line_start_end = ((origin['x'], 0), (origin['x'], HEIGHT))
        pg.draw.line(window, 'white', *line_start_end, 1)

        pg.display.update()
        clock.tick(FPS)
        window.fill('black')

    pg.quit()


if __name__ == '__main__':
    main()

