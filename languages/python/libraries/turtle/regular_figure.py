import turtle


def draw_figure(n_sides: int) -> None:
    '''
    Draws a figure with n sides
    '''
    angle = 360 / n_sides  # Calculate the angle of each turn
    for _ in range(n_sides):
        turtle.forward(100)  # Advance the turtle by 100 units
        turtle.right(angle)  # Turn the turtle by angle degrees


if __name__ == '__main__':
    
    for i in range(3, 11):
        draw_figure(i)
    
