import turtle
nav=turtle.Turtle()
nav.speed(20)
a=120
for i in range(10000):
    nav.forward(i*2)
    nav.right(a-0.4)