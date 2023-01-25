import sys
import time


# ? Time Tests----------------------------------------------------------------------------------------------------------------
# Then we create a decorator to time the execution of the functions
def performance(func):
    '''
    Decorator to time the execution of a function
    Print the time it took to execute the function
    '''
    def wrap_func(*args, **kwargs):
        t1 = time.time()  # Get the time before the function is executed
        result = func(*args, **kwargs)  # Execute the function
        t2 = time.time()  # Get the time after the function is executed
        print(f'Took {t2 - t1} seconds')  # Print the time it took to execute the function
        return result
    return wrap_func

# ? Functions-----------------------------------------------------------------------------------------------------------------

# In large numbers, iteration is the best option
@performance
def factorial(n: int) -> int:
    '''
    Calculates the factorial of the given number
    :param n: The number to calculate the factorial of
    Complexity: O(n)
    '''
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


# Optimized Fibonacci using recursion
# With small numbers, recursion is the best option
@performance
def factorial_recursive(number: int) -> int:
    '''
    Calculates the factorial of the given number
    :param number: The number to calculate the factorial of
    Complexity: O(n)
    '''
    return 1 if number == 0 else number * factorial(number - 1)


@performance
def fibonacci(number: int) -> int:
    '''
    Calculates the Fibonacci number of the given number
    :param number: The number to calculate the Fibonacci number of
    '''
    if number == 0: return 0
    elif number == 1: return 1
    else:  # If the number is greater than 1, calculate the Fibonacci number recursively
        return fibonacci(number - 1) + fibonacci(number - 2)


# Optimized Fibonacci using memoization
@performance
def fibonacci_optimized(n: int, memo: dict={}) -> int:
    '''
    Calculates the Fibonacci number of the given number. Uses memoization to speed up the calculation.
    :param n: The number to calculate the Fibonacci number of
    :param memo: The memoization dictionary
    '''
    try:  # Try to get the value from the memoization dictionary
        if n in memo: return memo[n]
        if n <= 2: return 1
        return memo[n]
    except KeyError:  # If the value is not in the memoization dictionary, calculate it and add it to the dictionary
        memo[n] = fibonacci_optimized(n - 1, memo) + fibonacci_optimized(n - 2, memo)
        return memo[n]  # Return the value


# ? MAIN-----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    sys.setrecursionlimit(1000000) # Set the recursion limit to 10002, so that we can calculate the 10000th Fibonacci number
    n = 1000000

    # Now test the performance of the functions
    factorial(n)
    factorial_recursive(n)
    # fibonacci(n)
    # fibonacci_optimized(n)

    # print([fibonacci_optimized(i) for i in range(1, 100)])  # Print the first 100 Fibonacci numbers

