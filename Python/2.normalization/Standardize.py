import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

BUSTED_AT = 2.0
BUSTED_5 = 60.0
BUSTED_3 = 30.0

df = pd.read_csv('data_output.csv')
df = df.to_numpy()
df_x = df.copy()

numbers_A = list()
numbers_B = list()

set_a = list()
set_b = list()

for flex in df_x:
    ba = flex[1]
    if ba>=10000 and ba<100000:
        set_a.append(flex)
    elif ba>=100000 and ba <500000:
        set_b.append(flex)

set_a = np.array(set_a)
set_b = np.array(set_b)

for i in range(0, 9):
    my1 = set_a[:, i]
    my2 = set_b[:, i]
    numbers_A.append((my1.max(), my1.min()))
    numbers_B.append((my2.max(), my2.min()))

for (i, flex) in enumerate(set_a):
    set_a[i][0] = 1 if flex[0] >= BUSTED_AT else 0
    for k in range(1, 9):
        if k == 3 or k == 4:
            continue
        set_a[i][k] = (flex[k] - numbers_A[k][1]) / (numbers_A[k][0]-numbers_A[k][1])
    
    if numbers_A[3][0] >= BUSTED_5:
        set_a[i][3] = 1 if flex[3] >= BUSTED_5 else (flex[3] - numbers_A[3][1]) / (BUSTED_5-numbers_A[3][1])
    else:
        set_a[i][3] = (flex[3] - numbers_A[3][1]) / (numbers_A[3][0]-numbers_A[3][1])

    if numbers_A[4][0] >= BUSTED_3:
        set_a[i][4] = 1 if flex[4] >= BUSTED_3 else (flex[4] - numbers_A[4][1]) / (BUSTED_3-numbers_A[4][1])
    else:
        set_a[i][4] = (flex[4] - numbers_A[4][1]) / (numbers_A[4][0]-numbers_A[4][1])

for (i, flex) in enumerate(set_b):
    set_b[i][0] = 1 if flex[0] >= BUSTED_AT else 0
    for k in range(1, 9):
        if k == 3 or k == 4:
            continue
        set_b[i][k] = (flex[k] - numbers_B[k][1]) / (numbers_B[k][0]-numbers_B[k][1])
    
    if numbers_B[3][0] >= BUSTED_5:
        set_b[i][3] = 1 if flex[3] >= BUSTED_5 else (flex[3] - numbers_B[3][1]) / (BUSTED_5-numbers_B[3][1])
    else:
        set_b[i][3] = (flex[3] - numbers_B[3][1]) / (numbers_B[3][0]-numbers_B[3][1])

    if numbers_B[4][0] >= BUSTED_3:
        set_b[i][4] = 1 if flex[4] >= BUSTED_3 else (flex[4] - numbers_B[4][1]) / (BUSTED_3-numbers_B[4][1])
    else:
        set_b[i][4] = (flex[4] - numbers_B[4][1]) / (numbers_B[4][0]-numbers_B[4][1])

train_setA, test_setA = train_test_split(pd.DataFrame(set_a), test_size= 0.3)
train_setB, test_setB = train_test_split(pd.DataFrame(set_b), test_size= 0.3)

test_setA_result = test_setA[:][0]
test_setA_ = test_setA.drop(test_setA.columns[0], axis=1)

train_setA_result = train_setA[:][0]
train_setA_ = train_setA.drop(train_setA.columns[0], axis=1)

test_setB_result = test_setB[:][0]
test_setB_ = test_setB.drop(test_setB.columns[0], axis=1)

train_setB_result = train_setB[:][0]
train_setB_ = train_setB.drop(train_setB.columns[0], axis=1)

ra = list()
ra_ = list()
rb = list()
rb_ = list()

for flex in train_setA_result:
    ra.append((1-flex, flex))
for flex in train_setB_result:
    rb.append((1-flex, flex))

for flex in test_setA_result:
    ra_.append((1-flex, flex))
for flex in test_setB_result:
    rb_.append((1-flex, flex))

ra = np.array(ra)
rb = np.array(rb)
ra_ = np.array(ra_)
rb_ = np.array(rb_)

test_setA_.to_csv("test_setA.csv", mode='w', header=False, index=False)
pd.DataFrame(ra_).to_csv("test_setA_result.csv", mode='w', header=False, index=False)
train_setA_.to_csv("train_setA.csv", mode='w', header=False, index=False)
pd.DataFrame(ra).to_csv("train_setA_result.csv", mode='w', header=False, index=False)

test_setB_.to_csv("test_setB.csv", mode='w', header=False, index=False)
pd.DataFrame(rb_).to_csv("test_setB_result.csv", mode='w', header=False, index=False)
train_setB_.to_csv("train_setB.csv", mode='w', header=False, index=False)
pd.DataFrame(rb).to_csv("train_setB_result.csv", mode='w', header=False, index=False)