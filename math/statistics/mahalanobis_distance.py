import numpy as np
import pandas as pd
import random
import matplotlib as plt


def calculateMahalanobis(y=None, data=None, cov=None):  
    y_mu = y - np.mean(data)
    if not cov:
        cov = np.cov(data.values.T)
    inv_covmat = np.linalg.inv(cov)
    left = np.dot(y_mu, inv_covmat)
    mahal = np.dot(left, y_mu.T)
    return mahal.diagonal()
  

# data
n = 20  # Where n is the number of elements in the dictionary
data = {}  # Create an empty dictionary
data['x'] ,data['y'] = [random.randint(150, 200) for i in range(1, n)], [random.randint(55, 90) for i in range(1, n)]

data = {'x': [159, 172, 150, 162, 170, 153, 170, 170, 162, 170, 182, 185, 171, 176, 154, 180, 170, 170, 174, 181],
        'y': [75, 69, 46, 59, 60, 58, 60, 65, 62, 59, 85, 87, 83, 80, 59, 82, 61, 73, 70, 85]
        }
print(data)

# Creating dataset
df = pd.DataFrame(data,columns=['x', 'y'])
# Creating a new column in the dataframe that holds the Mahalanobis distance for each row
df['calculateMahalanobis'] = calculateMahalanobis(y=df, data=df[['x', 'y']])
# Display the dataframe
print(df)



data = {'peso': [ 85,  67,  67,  75,  79,  70,  73,  60,  75,  85,  60,  54,  70,  67,  49,  59,  57,  78,  58,  70,  95,  65,  78,  62,  79,  80,  75,  76,  65,  90,  67,  80,  52,  58,  63,  56,  62,  60,  69,  57],
       'talla': [179, 165, 168, 177, 175, 175, 178, 168, 176, 180, 165, 161, 170, 174, 166, 162, 179, 187, 197, 178, 187, 158, 165, 161, 170, 174, 166, 170, 162, 180, 163, 182, 153, 172, 169, 153, 165, 163, 171, 150]}
print(f'\nThe dataset counts with 40 elements')
df = pd.DataFrame(data,columns=['peso', 'talla'])
df['calculateMahalanobis'] = calculateMahalanobis(y=df, data=df[['peso', 'talla']])
print(df)



input_data = {'peso_aleatorio': [10, -12, -21,  16],
             'talla_aleatoria': [17,  16,  -8, -10]}
df = pd.DataFrame(input_data,columns=['peso_aleatorio', 'talla_aleatoria'])
df['calculateMahalanobis'] = calculateMahalanobis(y=df, data=df[['peso_aleatorio', 'talla_aleatoria']])
print(df)

