import numpy as np
import pandas as pd

# 특정한 행과  열의 값을 출력
# 먼저 행 -> loc

raw_data = {
    'food': ['melon', 'melon', 'apple', 'apple', 'apple', 'peach'],
    'year': [2018,2019,2018,2019,2020,2018],
    'quantity': [490,512,478,325,290,800]
}

df = pd.DataFrame(raw_data, columns = ['quantity', 'year', 'rank', 'food'])

print(df.loc[3]) # 3행의 값을 출력
print(df.year) # 이런식으로 열 값 출력

print(df.loc[[1, 5], ['year', 'rank','food']])
# 이런 식으로 원하는 여러 행값만 혹은 원하는 행의 열값만 출력 가능 loc[ [] ] 이중 배열느낌으로 해야됨.
# df.loc[[1, 5],] == df.loc[[1, 5], :] // df.loc[[1, 5], []]  == empty data 출력

# iloc -> 열출력
print(df.iloc[:, [1]]) # 모든 행에 대하여 1열만 출력.
print(df.iloc[:, [3]])
print(df.iloc[:, [0, 3, 1]]) # 지정한 순서에 맞춰서 열값 출력 quan - food - year

# NaN 값 초기화 시키기.
df = df.fillna(0)
print(df) # 이런식으로 NaN값 0으로 초기화. df = 해줘야 df가 변경됨. fillna('a') 문자도 가능.