# LAMBDA FUNCTIONS = Useful when we need a function for a short period of time
# lambda arguments: expression

import random

double = lambda x: x * 2
print(double(5))
pow_n = lambda x, n: x ** n
print(pow_n(2, 3))
square = lambda x: pow_n(x, 2)
print(square(5))
square_root = lambda x: pow_n(x, 0.5)
print(square_root(25))

age_check = lambda age: True if age >= 18 else False
print(age_check(18))
print(age_check(12))

# Example: Factorial of a number
# n! = n * (n-1) * (n-2) * ... * 1
factorial = lambda x: 1 if x==0 else x * factorial(x-1)
print(factorial(7))


# Lambda functions with filter()
# If
# expression if condition else expression
print("Heads") if random.randint(1,10) > 5 else print("Tails")
# if condition: expression
if random.randint(1,10) > 5: print("Heads")


# map(function, iterable)
# Applies the function to every element of the iterable
pow_list = map(lambda x: x**2, list(range(10)))
print([x for x in pow_list])  # This isn't a list, it's a map object

# filter(function, iterable)
# Returns an iterator that passed the function check for each element in the iterable
# If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
print([i for i in range(1, 10) if i % 2 != 0])  # List with odd numbers from 1 to 9
print(list(filter(lambda x: x%2 != 0, range(0, 19))))  # Same as above

# reduce
# Applies a rolling computation to sequential pairs of values in a list
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))  # 15
print(reduce(lambda x, y: x*y, [1, 2, 3, 4, 5]))  # 120

# Examples
n_filter = ['']*10  # Empty list of 10 elements
print(['Odd' if i%2==1 else i for i in range(n_filter.__len__())])

# round(number, n_digits)
x1 = [round(i/(5/3), 2) for i in range(-5, 6)]  # same as np.linspace(-3, 3, 11)
print(x1)
x2 = [i**2 for i in x1]  # same as np.linspace(-3, 3, 11)^2
print(x2)

text = ['Superb', 'Omnipotent', 'Fine', 'Intrisnsic', 'Alluring']
[print(name[0]) for name in text]  # See this ;3
