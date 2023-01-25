import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Callable, Any

def printArray(array) -> None:
    elemType = str(type(array[0])).strip('<class >')
    print(f"Array of {len(array)} {elemType} elements")
    print('[')
    for elem in array:
        if type(array[0]) == type(1):
            print(f"  {elem: < 8,}")
        else:
            print(f"  {float(elem): < 8,.6f}")
    print(']')

def printAngleArray(array) -> None:
    # Dismiss '<class ' at the beginning and '>' at the end
    elemType = str(type(array[0]))[7:-1]
    print(f"Array of {len(array)} {elemType} elements")
    print('[')
    print(f"  {'Radians': >9}  ->  {'Degrees': <8}")
    for elem in array:
        print(f"  {float(elem): < 8,.6f}", end="  ->")
        print(f"  {math.degrees(float(elem)): < 6,.2f}")
    print(']')

def zipPrint(array1, array2) -> None:
    print('[')
    for elem1, elem2 in zip(array1, array2):
        print(f"{str(round(elem1, 8)).rjust(12)} {str(round(elem2, 0)).rjust(8)}")
    print(']')

def trigPrint(trigMatrix) -> None:
    decimals = 4
    colWidth = 10
    formatTrigs = []
    for trig in trigMatrix[0:6]:
        formatTrigs.append(str(round(x, decimals)).rjust(colWidth) for x in trig)
    for sin, cos, tan, cot, sec, csc, angle in zip(*formatTrigs, trigMatrix[6]):
        print(f"{sin}{cos}{tan}{cot}{sec}{csc}{str(round(angle, 0)).rjust(colWidth)}")

def rounder(func: Callable, n=8) -> Callable:
    def wrapper(*args, **kwargs) -> float:
        return round(func(*args, **kwargs), n)
    return wrapper

# rounder = lambda func, n=8: lambda *args, **kwargs: round(func(*args, **kwargs), n)

def sinCosDeg(radians: list|np.array.Array) -> list[list[float]]:
    sin = rounder(math.sin)
    cos = rounder(math.cos)
    degrees = [math.degrees(x) for x in radians]
    sine   = [sin(x) for x in radians]
    cosine = [cos(x) for x in radians]
    return [sine, cosine, degrees]

def trigMatrix(radians: list|np.array.Array) -> list[list[float]]:
    rounded = lambda x: round(x, 8)
    [sine, cosine, degrees] = sinCosDeg(radians)
    tangent   = [sin/cos if rounded(cos) != 0 else math.nan for sin, cos in zip(sine, cosine)]
    cotangent = [cos/sin if rounded(sin) != 0 else math.nan for cos, sin in zip(cosine, sine)]
    secant    = [1/cos if rounded(cos) != 0 else math.nan for cos in cosine]
    cosecant  = [1/sin if rounded(sin) != 0 else math.nan for sin in sine]
    return [sine, cosine, tangent, cotangent, secant, cosecant, degrees]

trigs = trigMatrix(np.linspace(math.tau/2, -math.tau/2, num=73))
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)
# pd.set_option('display.colheader_justify', 'center')
# pd.set_option('display.precision', 6)
trigsDf = pd.DataFrame(np.transpose(trigs))
trigsDf.columns = ['sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'deg']
roundDf = trigsDf.round(8)
# print(trigsDf.round(6))
print(roundDf)
with pd.option_context(
    'display.max_rows', None,
    'display.max_columns', None,
    'display.width', 1000,
    'display.colheader_justify', 'center',
    'display.precision', 6):
    print(trigsDf.round(6))

# plt.plot(trigs[6], trigs[0])
# fontdict = {'fontname': 'Times New Roman', 'fontsize': 20}
# plt.title('Trigonometric Functions', fontdict=fontdict)
# plt.xlabel('Angle (Degrees)')
# plt.ylabel('Value')
# plt.show()

# trigPrint(trigs)
# for trig in trigs:
#     for elem in trig:
#         if round(elem, 8) == 0:
#             print(round(elem, 8))
#             print(elem)


# https://docs.python.org/3/library/math.html#trigonometric-functions
# math.atan(x)      Return value range: [-tau/4, tau/4]
# math.atan2(y, x)  Return value range: [-tau/2, tau/2]
#                   The sign of both inputs are known to it, so it can
#                   compute the correct quadrant for the angle.

[sine, cosine, degrees] = sinCosDeg(np.linspace(math.tau/2, -math.tau/2, num=73))
angles = [math.degrees(math.atan2(sin, cos)) for sin, cos in zip(sine, cosine)]
zipPrint(angles, degrees)

degs = rounder(math.degrees, 6)

[sine, cosine, degrees] = sinCosDeg(np.linspace(0, math.tau, num=73))
angles = [degs(math.atan2(sin, cos)) for sin, cos in zip(sine, cosine)]
zipPrint(angles, degrees)

[sine, cosine, degrees] = sinCosDeg(np.linspace(0, math.tau, num=73))
# angles = []
# for sin, cos in zip(sine, cosine):
#     candidate = math.atan(sin/cos)
#     if cos > 0:
#         angle = math.degrees((candidate + math.tau) % math.tau)
#         angles.append(angle)
#     elif cos <= 0:
#         angle = math.degrees(candidate + math.tau/2)
#         angles.append(angle)
# zipPrint(angles, degrees)


# A = math.atan(sin/cos)
# I:    A
# II:   180 + A   (A is negative)
# III:  180 + A   (A is positive)
# IV:   360 + A   (A is negative)


# printArray(np.arange(5)) # [0 1 2 3 4] <np.int32>
# printArray(np.arange(2, 13, 2)) # [2 4 6 8 10 12] <np.int32>
# printArray(np.ones(5))




