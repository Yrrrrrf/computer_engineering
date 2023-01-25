# 2120019
# Reza Campos Fernando Bryan

# Código utilizado para el cálculo de los estados
import numpy as np
import pandas as pd


data_set = {'1': [ 0.5,  0.5,    0,    0,    0,    0],  # sum = 1
            '2': [0.25, 0.25, 0.25,    0, 0.25,    0],  # sum = 1
            '3': [   0,  0.5,  0.5,    0,    0,    0],  # sum = 1
            '4': [   0,    0,    0,  0.5,  0.5,    0],  # sum = 1
            '5': [   0, 0.25,    0, 0.25, 0.25, 0.25],  # sum = 1
            '6': [   0,    0,    0,    0,  0.5,  0.5]}  # sum = 1

markov_chain = pd.DataFrame(data=data_set, index=['1', '2', '3', '4', '5', '6'])
print(markov_chain)

# We have 500 people, so we can calculate the probability of each state
p_vector = [1, 0, 0, 0, 0, 0]
p_vector = [0, 1, 0, 0, 0, 0]
p_vector = [0, 0, 1, 0, 0, 0]
p_vector = [0, 0, 0, 1, 0, 0]
p_vector = [0, 0, 0, 0, 1, 0]
p_vector = [0, 0, 0, 0, 0, 1]
# print(f'\n{p_vector}' )

# We can calculate the probability of the next state
def calculate_state(n):
    current_state = np.dot(markov_chain, p_vector)
    print(f'n1  = {current_state}')
    for i in range(2, n+1):
        current_state = np.dot(markov_chain, current_state)
        print(f'n{i:<3}= {current_state}')


calculate_state(50)
