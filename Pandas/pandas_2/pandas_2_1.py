import numpy as np
import pandas as pd

# raw_data 생성
raw_data = {
    'food': ['apple', 'pear', 'peach', 'banana', 'orange', 'watermelon'],
    'month': [1,2,3,4,5,6],
    'quantity': [55,32,59,87,24,49]
}

df = pd.DataFrame(raw_data)
print(df)
df1 = pd.DataFrame(raw_data, columns=['month', 'food', 'quantity'])
print(df1) # 원하는 배치로 columns 변경 가능.
df1 = pd.DataFrame(raw_data, index = list('abcdef'))
print(df1) # index도 당연히 설정 가능

df1 = pd.DataFrame(raw_data, columns=['quantity', 'food', 'month', 'rank'])
print(df1) # 변경하면서 새로운 column추가 가능. raw_data에 해당 column없으면 NaN값으로.

print(df1.index)
print(df1.columns)
