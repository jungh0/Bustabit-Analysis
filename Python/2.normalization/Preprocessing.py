import csv
import pandas as pd
import numpy as np
import argparse
import sys

BUSTED_5 = 60.0
BUSTED_3 = 30.0

numbers_A = [(99997.0, 11083.0), (920113.0, -99829.0), (8388.45, 5.53), (8377.18, 3.08),
             (25391344.0, -11652565.0), (12591347.0, -10021862.0), (12700949.0, -9618877.0), (12799142.0, -9431350.0)]
numbers_B = [(499885.0, 100004.0), (11832202.0, -499158.0), (3073.41, 5.33), (3068.08, 3.03),
             (12656758.0, -10792929.0), (24731064.0, -10468750.0), (25121624.0, -10086032.0), (25650876.0, -9569315.0)]

# 46637,154569,61.92,23.01,93915,168498,172921,363688 이런 형태로 들어옴
arg = sys.argv[1].split(',')

df = list()

for k in arg:
    df.append(float(k))

df = np.array(df)

ba = df[0]

numbers = []

if ba >= 10000 and ba < 100000:
    numbers = numbers_A
elif ba >= 100000 and ba < 500000:
    numbers = numbers_B
else :
    print('invalid value')
    exit()

for k in range(0, 8):
    if k == 2 or k == 3:
        continue
    df[k] = (df[k] - numbers[k][1]) / (numbers[k][0]-numbers[k][1])

if numbers[2][0] >= BUSTED_5:
    df[2] = 1 if df[2] >= BUSTED_5 else (
        df[2] - numbers[2][1]) / (BUSTED_5-numbers[2][1])
else:
    df[2] = (df[2] - numbers[2][1]) / (numbers[2][0]-numbers[2][1])

if numbers[3][0] >= BUSTED_3:
    df[3] = 1 if df[3] >= BUSTED_3 else (
        df[3] - numbers[3][1]) / (BUSTED_3-numbers[3][1])
else:
    df[3] = (df[3] - numbers[3][1]) / (numbers[3][0]-numbers[3][1])

print(df)

