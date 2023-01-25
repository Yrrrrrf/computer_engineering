# Reza Campos Fernando Bryan
# 2120019
import numpy as np
import matplotlib.pyplot as plt


# counts the number of iterations until the function diverges or returns the iteration threshold that we check until
def count_iterations_until_divergent(c, threshold):
    global iterations
    z = complex(0, 0)
    for iterations in range(threshold):
        z = (z * z) + c
        if abs(z) > 4:
            break
            pass
        pass
    return iterations


# takes the iteration limit before declaring function as convergent and takes the density of the atlas
# create atlas, plot mandelbrot set, display set
def mandelbrot(threshold, density, width, height):
    # location and size of the Atlas rectangle
    # real_axis = np.linspace(-2.25, 0.75, width)
    # imaginary_axis = np.linspace(-1.5, 1.5, height)
    real_axis = np.linspace(-0.22, -0.219, width)
    imaginary_axis = np.linspace(-0.70, -0.699, height)
    real_axis_len = len(real_axis)
    imaginary_axis_len = len(imaginary_axis)
    # 2-D array to represent mandelbrot atlas
    atlas = np.empty((real_axis_len, imaginary_axis_len))
    # color each point in the atlas depending on the iteration count
    for ix in range(real_axis_len):
        for iy in range(imaginary_axis_len):
            cx = real_axis[ix]
            cy = imaginary_axis[iy]
            c = complex(cx, cy)
            atlas[ix, iy] = count_iterations_until_divergent(c, threshold)
            pass
        pass
    # plot and display mandelbrot set
    plt.imshow(atlas.T, interpolation="nearest")
    plt.show()


# mandelbrot(threshold, density,  width, height)
mandelbrot(120, 4096, 1920, 1080)
