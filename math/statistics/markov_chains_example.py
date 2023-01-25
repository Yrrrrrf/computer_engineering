# 2120019
# Reza Campos Fernando Bryan

# Código utilizado para el cálculo de los estados

import numpy as np
import pandas as pd


data_set = {'A': [0.8, 0.1, 0.1],  # 200
            'B': [0.2, 0.7, 0.1],  # 120
            'C': [0.1, 0.3, 0.6]   # 180
           } # So we have a total of 500 people

markov_chain = pd.DataFrame(data=data_set, index=['A', 'B', 'C'])
print(markov_chain)

# We have 500 people, so we can calculate the probability of each state
p_vector = [200/500, 120/500, 180/500]  # [0.4, 0.24, 0.36]
print(f'\n{p_vector}' )

# We can calculate the probability of the next state
def calculate_state(n):
    current_state = np.dot(markov_chain, p_vector)
    print(f'n1  = {current_state}')
    for i in range(2, n+1):
        current_state = np.dot(markov_chain, current_state)
        print(f'n{i:<3}= {current_state}')


calculate_state(50)
