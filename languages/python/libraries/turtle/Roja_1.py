import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(100)
cl=["red"]

def drawArt(d, angle, x, y):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()
    for i in range(1, 1000):
        my_turtle.pencolor(cl[0])
        my_turtle.forward(d)
        my_turtle.left(angle)
        d = d - 1
drawArt(150, 98, 0, 0)