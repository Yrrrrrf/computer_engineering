import math

print('Enter an equation in the form ax^2 + bx + c = 0')
a = float(input('Enter a value:\n'))

if a==0:
    print("That's not a quadratic equation!")
else:
    b = float(input("Enter b value:\n"))
    c = float(input("Enter c value:\n"))

    root = ((b*b)-(4*a*c))
    if (4*a*c)>(b*b):
        print(f'There\'s no real solution!\nThe imaginary root\'ll be: {math.sqrt(-root)} i')
    else:
        x1 = ((-b+math.sqrt(root))/(2*a))
        print(f'x_1 value is {x1}')
        x2 = ((-b-math.sqrt(root))/(2*a))
        print(f'x_2 value is {x2}')
        print(f'{a}*({x1})^2 + {b}*({x1}) + {c} = 0')
        print(f'{a}*({x2})^2 + {b}*({x2}) + {c} = 0')
