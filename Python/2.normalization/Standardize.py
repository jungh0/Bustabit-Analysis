import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

BUSTED_AT = 5
BUSTED_5 = 60.0
BUSTED_3 = 30.0

df = pd.read_csv('data_output.csv')
df = df.to_numpy()
df_x = df.copy()

numbers_A = list()
numbers_B = list()

set_a = list()

for flex in df_x:
    ba = flex[1]
    set_a.append(flex)

set_a = np.array(set_a)

for i in range(0, 12):
    my1 = set_a[:, i]
    numbers_A.append((my1.max(), my1.min()))

for (i, flex) in enumerate(set_a):
    set_a[i][0] = 1 if flex[0] >= BUSTED_AT else 0
    for k in range(1, 12):
        set_a[i][k] = (flex[k] - numbers_A[k][1]) / (numbers_A[k][0]-numbers_A[k][1])


train_setA, test_setA = train_test_split(pd.DataFrame(set_a), test_size= 0.3,random_state=0)


test_setA_result = test_setA[:][0]
test_setA_ = test_setA.drop(test_setA.columns[0], axis=1)

train_setA_result = train_setA[:][0]
train_setA_ = train_setA.drop(train_setA.columns[0], axis=1)

ra = list()
ra_ = list()

for flex in train_setA_result:
    ra.append((1-flex, flex))
for flex in test_setA_result:
    ra_.append((1-flex, flex))

ra = np.array(ra)
ra_ = np.array(ra_)

test_setA_.to_csv("test_setA.csv", mode='w', header=False, index=False)
pd.DataFrame(ra_).to_csv("test_setA_result.csv", mode='w', header=False, index=False)
train_setA_.to_csv("train_setA.csv", mode='w', header=False, index=False)
pd.DataFrame(ra).to_csv("train_setA_result.csv", mode='w', header=False, index=False)
