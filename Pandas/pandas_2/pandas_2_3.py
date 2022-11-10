import numpy as np
import pandas as pd

raw_data = {
    'food': ['melon', 'melon', 'apple', 'apple', 'apple', 'peach'],
    'year': [2018,2019,2018,2019,2020,2018],
    'quantity': [490,512,478,325,290,800]
}

df = pd.DataFrame(raw_data, columns = ['quantity', 'year', 'rank','food'])

df['rank'] = df.food == 'peach'
print(df) # rank에 조건의 결과값을 대입.
df['addcol'] = df.food == 'peach'
print(df) # 새로운 column 추가도 가능.

del df['addcol'] # 삭제도 가능

# transpose -- 행과 열 바꾸기

data = {
    'Seoul' : {2018:1, 2019:2, 2020:1},
    'Busan' : {2018:3, 2019:1, 2020:4}
}
df2 = pd.DataFrame(data)
"""
      Seoul  Busan
2018      1      3
2019      2      1
2020      1      4
"""
df2 = df2.T # index <-> columns 바뀜
df3 = pd.DataFrame(data, index = [2019, 2020]) # index값 지정 가능 원하는 값만 / index값이 data에 없으면 NaN

df4 = pd.DataFrame(data)
x = {
    'Seoul': df4['Seoul'][:-1]
}
k = pd.DataFrame(x)
print(k) # 새로운 DF에 이런식으로 범위 지정해서 생성가능

x = {
    'Busan': df4['Busan'][1:-1],
    'Seoul': df4['Seoul'][:-1]
}
k = pd.DataFrame(x)
print(k) # 부산의 경우 2018의 값이 x에 지정이 되지 않았기 때문에 'NaN' (범위는 내부에서 맞춤)
"""
      Busan  Seoul
2018    NaN      1
2019    1.0      2
NaN값에 의해 2019 - Busan 값이 float으로 변경됨.
"""