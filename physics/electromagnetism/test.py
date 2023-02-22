import numpy as np



A = np.array([[-8000,  1000,  3000]
            , [-1000,  3000, -2000]
            , [-3000, -2000,  5000]])

b = np.array([0, 15, 10])


print('x: ', np.linalg.solve(A, b))


