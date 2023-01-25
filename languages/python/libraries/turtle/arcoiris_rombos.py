import turtle

sc= turtle.Screen()

sc.bgcolor('black')


my_pencil = turtle.Turtle()

my_pencil.speed(0) # adjust speed with 0 being the highest

my_pencil.pensize(2) #pensize is the thickness


colors_list = ['Cyan','HotPink','Lime','Red','Yellow','White','Orange']

for i in range(5): # in one iteration we are creating different squares of above mentioned colors

    for colour in colors_list:

        my_pencil.color(colour)

        my_pencil.left(12) #turn 12deg

        for j in range(4): # 1 square created

            my_pencil.forward(200)

            my_pencil.left(90)