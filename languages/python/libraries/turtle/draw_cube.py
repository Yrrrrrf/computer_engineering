import turtle


def draw_cube(size: int) -> None:
    '''
    Draws a cube with sides of size size
    '''
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)


if __name__ == '__main__':
    turtle.speed(0)  # Set the speed of the turtle to the fastest
    for i in range(1, 100):  # Draw 100 cubes
        draw_cube(i * 3)  # Draw a cube with sides of size i * 5
        turtle.right(20)  # Turn the turtle by 11.25 degrees
    turtle.done()
