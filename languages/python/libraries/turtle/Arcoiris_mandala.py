import turtle

myScreen = turtle.Screen()
myScreen.bgcolor('black')

Lucy = turtle.Turtle()

def drawCircles(t, size, numInnerCircles, adjSize):
    for i in range(numInnerCircles):
        t.circle(size)
        size=size-adjSize

def drawPattern(t, size, numCircles, numInnerCircles, adjSize, speed, color):
    t.speed(speed)
    t.color(color)
    for i in range(numCircles):
        drawCircles(t,size, numInnerCircles, adjSize)
        t.right(360/numCircles)

Lucy.penup()
Lucy.goto(0,170)
Lucy.color("white")
Lucy.write("Let's draw some spirals", align="center", font=("Arial", 6, "normal"))
Lucy.goto(0,-180)
Lucy.color("lightblue")
Lucy.write("Make your own changes and have some fun !!", align="center", font=("Arial", 6, "normal"))
Lucy.home()
Lucy.pendown()

drawPattern(Lucy, 76, 10, 10, 4, 0, 'white')
drawPattern(Lucy, 68, 5, 4, 10, 0, 'yellow')
drawPattern(Lucy, 60, 6, 4, 5, 0, 'pink')
drawPattern(Lucy, 30, 4, 8, 8, 0, 'orange')
drawPattern(Lucy, 70, 6, 4, 6, 0, 'blue')