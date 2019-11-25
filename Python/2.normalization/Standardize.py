import csv
import pandas as pd
import numpy as np
from sklearn import preprocessing

df = pd.read_csv('data.csv')
df = df.to_numpy()
df_x = df.copy()

numbers = list()

for i in range(0, 10):
    my = df_x[:, i]
    numbers.append((my.max(), my.min()))

for (i, flex) in enumerate(df_x):
    df[i][0] = 1 if flex[0] >= 3 else 0
    for k in range(1, 10):
        if k == 3 or k == 4:
            continue
        df[i][k] = (flex[k] - numbers[k][1]) / (numbers[k][0]-numbers[k][1])
    
    if numbers[3][0] >= 100:
        df[i][3] = 1 if flex[3] >= 100 else (flex[3] - numbers[3][1]) / (100-numbers[3][1])
    else:
        df[i][3] = (flex[3] - numbers[3][1]) / (numbers[3][0]-numbers[3][1])

    if numbers[4][0] >= 60:
        df[i][4] = 1 if flex[4] >= 100 else (flex[4] - numbers[4][1]) / (100-numbers[4][1])
    else:
        df[i][4] = (flex[4] - numbers[4][1]) / (numbers[4][0]-numbers[4][1])

pd.DataFrame(df).to_csv("data_output.csv", mode='w', header=False, index=False)
