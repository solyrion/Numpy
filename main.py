import numpy as np
import pandas as pd

raw_data = {
    'food': ['apple', 'pear', 'peach', 'banana', 'orange', 'watermelon'],
    'month': [1,2,3,4,5,6],
    'quantity': [55,32,59,87,24,49]
}

df = pd.DataFrame(raw_data)
print(df)
# df = pd.read_csv("상가(상권)정보_의료기관_201909.csv", low_memory=False)
a = {'a' : [1,2,3], 'b' : [4,5,6], 'c':[7,8,9]}
df = pd.DataFrame(a, index = list('xyz'))
print(df)
print(df['a'])
print(df[['a', 'b']])
print(df.loc[['x']])
