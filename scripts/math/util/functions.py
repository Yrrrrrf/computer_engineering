from typing import Callable

from sympy import Symbol, lambdify, sympify, solve


def get_derivative(f: Callable[[float], float]) -> Callable[[float], float]:
    """
    Return the derivative of a function (lambda function) using SymPy
    :param f: lambda function
    :return: lambda function
    """
    from inspect import getsource  # to get the source code of a function
    function_str = getsource(f).split("return ")[1]  # get the "return" part of the function (the function itself) and convert it to a string
    derivative = sympify(function_str).diff(Symbol('x'))  # get the derivative of f
    diff = lambdify(Symbol('x'), derivative, 'numpy')  # convert the derivative to a lambda function (to make it faster
    print(f"f(x) = {function_str}", end='')  # print the function
    print(f"f'(x) = {derivative}")  # print the derivative of f
    return diff  # return the derivative of f (lambda function)


# ! This function is not working properly
def get_g_function(f: Callable[[float], float]) -> Callable[[float], float]:
    """
    Return the g function of a function (lambda function) using SymPy
    :param f: lambda function
    :return: lambda function
    """
    from inspect import getsource  # to get the source code of a function
    function_str = getsource(f).split("return ")[1]  # get the "return" part of the function (the function itself) and convert it to a string
    g = solve(sympify(function_str), Symbol('x'))  # get the g function of f
    print(f"g(x) = {g}")  # print the g function of f
    return lambdify(Symbol('x'), g, 'numpy')  # convert the g function to a lambda function (to make it faster)


def _gaussian_substitution(f: Callable[[float], float]) -> Callable[[float], float]:
    """
    Is a function that takes a function f(x) and returns a function f(t) that is the result of substituting x with t
    This function is used in the gaussian quadrature method
    :param f: function
    :return: function
    """
    f = sympify(f).subs(Symbol('x'), Symbol('t'))
    return lambdify(Symbol('t'), f, 'numpy')
