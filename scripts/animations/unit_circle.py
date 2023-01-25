import pygame as pg
import math

def linearMapX(x, origin, scale, inverse=False) -> float:
    return (x - origin) / scale if not inverse else (x * scale) + origin

def linearMapY(y, origin, scale, inverse=False) -> float:
    return (origin - y) / scale if not inverse else origin - (y * scale)

def linearMapXY(coors, origin, scales, inverse=False) -> tuple[float, float]:
    return (linearMapX(coors[0], origin[0], scales[0], inverse),
            linearMapY(coors[1], origin[1], scales[1], inverse))

def rounded(x) -> float:
    return round(x, 8)

def counter():
    count = 0
    def countFunction() -> int:
        nonlocal count
        count += 1
        return count
    return countFunction


# COLORS
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
DARKGRAY = (64, 64, 64)
RED = (255, 44, 44)
ORANGE = (255, 163, 0)
BROWN = (127, 51, 0)
GOLD = (255, 216, 0)
LIGHTLIME = (182, 255, 0)
LIME = (76, 255, 0)
GREEN = (0, 255, 104)
CYAN = (0, 255, 255)
DODGER = (0, 128, 255)
BLUE = (0, 38, 255)
DARKVIOLET = (72, 0, 255)
VIOLET = (178, 0, 255)
FUCHSIA = (255, 0, 240)
DEEPPINK = (255, 0, 110)
WHITE   = (255, 255, 255)



class UnitCircle:
    colors = {
        'sin': FUCHSIA,
        'cos': GREEN,
        'tan': GOLD,
        'cot': CYAN,
        'sec': DODGER,
        'csc': RED,
        'main': WHITE,
        'radius': GRAY,
    }
    trig_thickness = 3
    line_thickness = 2
    radius_thickness = 2
    show_circle = True
    show_radius = True
    show_origin = True
    show_axes = True
    show_arrows = True
    show_sin_cos = True
    show_tan_cot_sec_csc = True
    radius_on_top = False

    def __init__(self, surface, origin, radius, font) -> None:
        self.surface = surface
        self.font = font
        self.radius = radius
        self.origin = {}
        self.origin['x'] = origin[0]
        self.origin['y'] = origin[1]

    def drawLine(self, color, points, thickness=trig_thickness) -> None:
        pg.draw.line(self.surface, color, points[0], points[1], thickness)


    def draw(self) -> None:
        if self.show_axes:
            self.drawAxes(self.show_arrows)

        # Important Points
        originPoint = (self.origin['x'], self.origin['y'])
        circlePoint = (self.cos, self.sin)
        sinPoint = (self.origin['x'], self.sin)
        cscPoint = (self.origin['x'], self.csc)
        cosPoint = (self.cos, self.origin['y'])
        secPoint = (self.sec, self.origin['y'])

        # Circumference
        if self.show_circle:
            pg.draw.circle(self.surface, self.colors['main'], originPoint, self.radius, self.line_thickness)
        # Radius
        if self.show_radius and not self.radius_on_top:
            self.drawLine(self.colors['radius'], (originPoint, circlePoint), self.radius_thickness)

        # Trigonometric Lines
        if self.show_tan_cot_sec_csc:
            if not math.isnan(self.sec) and not math.isnan(self.csc):
                self.drawLine(self.colors['sec'], (originPoint, secPoint))
                self.drawLine(self.colors['csc'], (originPoint, cscPoint))
                self.drawLine(self.colors['tan'], (circlePoint, secPoint))
                self.drawLine(self.colors['cot'], (circlePoint, cscPoint))
        if self.show_sin_cos:
            self.drawLine(self.colors['sin'], (circlePoint, cosPoint))
            self.drawLine(self.colors['cos'], (circlePoint, sinPoint))

        # Origin
        if self.show_origin:
            pg.draw.circle(self.surface, self.colors['main'], originPoint, self.trig_thickness)

        # Radius on Top
        if self.show_radius and self.radius_on_top:
            self.drawLine(self.colors['radius'], (originPoint, circlePoint), self.trig_thickness)


    def drawAxes(self, arrows) -> None:
        axisStretch = self.radius if not arrows else (6*self.radius)//5
        # Axis Points
        xAxisLeft  = (self.origin['x'] - axisStretch, self.origin['y'])
        xAxisRight = (self.origin['x'] + axisStretch, self.origin['y'])
        yAxisTop    = (self.origin['x'], self.origin['y'] - axisStretch)
        yAxisBottom = (self.origin['x'], self.origin['y'] + axisStretch)

        # Axis Lines
        self.drawLine(self.colors['main'], (xAxisLeft, xAxisRight), self.line_thickness)
        self.drawLine(self.colors['main'], (yAxisTop, yAxisBottom), self.line_thickness)

        if arrows:
            arrowWidth  = self.radius // 12
            arrowLength = self.radius // 10

            # Arrow Points
            LeftArrow  = ((xAxisLeft[0], self.origin['y'] - arrowWidth//2),
                        (xAxisLeft[0], self.origin['y'] + arrowWidth//2),
                        (xAxisLeft[0] - arrowLength, self.origin['y']))
            RightArrow = ((xAxisRight[0], self.origin['y'] - arrowWidth//2),
                        (xAxisRight[0], self.origin['y'] + arrowWidth//2),
                        (xAxisRight[0] + arrowLength, self.origin['y']))
            TopArrow    = ((self.origin['x'] - arrowWidth//2, yAxisTop[1]),
                        (self.origin['x'] + arrowWidth//2, yAxisTop[1]),
                        (self.origin['x'], yAxisTop[1] - arrowLength))
            BottomArrow = ((self.origin['x'] - arrowWidth//2, yAxisBottom[1]),
                        (self.origin['x'] + arrowWidth//2, yAxisBottom[1]),
                        (self.origin['x'], yAxisBottom[1] + arrowLength))

            # Arrow Triangles
            pg.draw.polygon(self.surface, self.colors['main'], LeftArrow)
            pg.draw.polygon(self.surface, self.colors['main'], RightArrow)
            pg.draw.polygon(self.surface, self.colors['main'], TopArrow)
            pg.draw.polygon(self.surface, self.colors['main'], BottomArrow)


    def calculateTrigs(self) -> None:

        # Mouse position to unit circle plane position
        mapCoors = pg.mouse.get_pos()
        mapOrigin = (self.origin['x'], self.origin['y'])
        mapScales = (self.radius, self.radius)
        mappedX, mappedY = linearMapXY(mapCoors, mapOrigin, mapScales)

        # Calculate angle
        radAngle = math.atan2(mappedY, mappedX)
        degAngle = math.degrees(radAngle)

        cos = math.cos(radAngle)
        sin = math.sin(radAngle)
        tan = sin/cos if rounded(cos) != 0 else math.nan
        cot = cos/sin if rounded(sin) != 0 else math.nan
        sec = 1/cos if rounded(cos) != 0  else math.nan
        csc = 1/sin if rounded(sin) != 0 else math.nan

        self.sin = linearMapY(sin, self.origin['y'], self.radius, inverse=True)
        self.csc = linearMapY(csc, self.origin['y'], self.radius, inverse=True)
        self.cos = linearMapX(cos, self.origin['x'], self.radius, inverse=True)
        self.sec = linearMapX(sec, self.origin['x'], self.radius, inverse=True)

        # numberLabel = lambda text, value, n: f"{text.rjust(5)}: {round(value, n):< }"

        # texts = ('sin', 'cos', 'tan', 'cot', 'sec', 'csc')
        # values = (sin, cos, tan, cot, sec, csc)
        # trigLabels = []
        # for text, value in zip(texts, values):
        #     content = numberLabel(text, value, 4)
        #     trigLabels.append(self.font.render(content, True, self.colors[text]))

        # angleLabel = self.font.render(numberLabel('Angle', degAngle, 2), True, self.colors['main'])
        # xLabel = self.font.render(numberLabel('X', mappedX, 2), True, self.colors['main'])
        # yLabel = self.font.render(numberLabel('Y', mappedY, 2), True, self.colors['main'])

        # return {'trigLabels': trigLabels, 'angleLabel': angleLabel, 'xLabel': xLabel, 'yLabel': yLabel}


def colorMode(mode='CMY') -> None:
    pg.mouse.set_visible(False)
    UnitCircle.show_circle = False
    UnitCircle.show_origin = False
    UnitCircle.show_axes = False
    UnitCircle.show_tan_cot_sec_csc = False
    UnitCircle.radius_on_top = True
    if mode.lower() == 'rgb':
        UnitCircle.colors.update({
            'sin':    (255, 0, 0),
            'cos':    (0, 255, 0),
            'radius': (0, 0, 255),
            })
    elif mode.lower() == 'cmy':
        UnitCircle.colors.update({
            'radius': (0, 255, 255),
            'cos':    (255, 0, 255),
            'sin':    (255, 255, 0),
            })


def setWindow(title, size, icon_file) -> pg.surface.Surface:
    pg.display.set_caption(title)
    icon = pg.image.load(icon_file)
    pg.display.set_icon(icon)
    return pg.display.set_mode(size)

def main() -> None:
    FPS = 30
    # (720, 480)
    WIDTH, HEIGHT = 720, 720
    TITLE = "Unit Circle"
    ICON = "img/trig_circle.png"
    FONT1 = "fonts/AzeretMono-Regular.ttf"
    FONT2 = "fonts/AzeretMono-Bold.ttf"
    FONTSIZE = HEIGHT//24
    LINEHEIGHT = FONTSIZE
    INDENT = FONTSIZE

    pg.init()
    clock = pg.time.Clock()
    window = setWindow(TITLE, (WIDTH, HEIGHT), ICON)
    font1 = pg.font.Font(FONT1, FONTSIZE)
    font2 = pg.font.Font(FONT2, FONTSIZE)

    def generateCircleMatrix(n, divs, sep) -> list[UnitCircle]:
        radius = WIDTH//divs
        circles = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                origin = (((sep*i - 1)*WIDTH)//divs, ((sep*j - 1)*HEIGHT)//divs)
                circles.append(UnitCircle(window, origin, radius, font1))
        return circles


    # Contiguous
    # 1 -> .. -> 2          -> 1*2
    # 2 -> .. .. -> 4       -> 2*2
    # 3 -> .. .. .. -> 6    -> 2*3
    # 4 -> .. .. .. .. -> 8 -> 2*4
    # n = 1
    # divs = (2*n)
    # circles = generateCircleMatrix(n, divs=(2*n), sep=2)
    # colorMode('RGB')


    # # Equally separated by radius
    # # 1 -> . .. . -> 4                 -> 3*1 + 1
    # # 2 -> . .. . .. . -> 7            -> 3*2 + 1
    # # 3 -> . .. . .. . .. . -> 10      -> 3*3 + 1
    # # 4 -> . .. . .. . .. . .. . -> 13 -> 3*4 + 1
    n = 1
    circles = generateCircleMatrix(n, divs=(3*n + 1), sep=3)


    def update() -> None:
        pg.display.update()
        for circle in circles:
            circle.calculateTrigs()
        window.fill('black')

    def draw() -> None:
        for circle in circles:
            circle.draw()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        update()
        draw()
        clock.tick(FPS)
    pg.quit()


if __name__ == '__main__':
    main()

