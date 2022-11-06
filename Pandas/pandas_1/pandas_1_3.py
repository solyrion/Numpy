import numpy as np
import pandas as pd

"""
- DataFrame
    - 엑셀, 관계형 DB(RDBMS)의 테이블은 행-열 2차원 배열구조. 이를 위한 pandas 자료구조
    - Series = 1차원 / DataFrame = 2차원
    - Series = 행단위 처리 / DataFrame = 열단위 처리
"""

df = pd.DataFrame([[1,2,3,4,5], [6,7,8,9,10]])
print(df)
"""
   0  1  2  3   4
0  1  2  3  4   5
1  6  7  8  9  10
가장 기본적인 형태.
"""
df = pd.DataFrame([[1,2,3,4,5], [6,7,8,9,10]], index = ['a', 'b'])
print(df) # index(행) 지정가능 / index 코드 자체는 안 써도 되긴함. list('ab')도 가능

df = pd.DataFrame([[1,2,3,4,5], [6,7,8,9,10]], index = ['a', 'b'], columns = ['a','b','c','d','e'])
print(df) # 당연하게 열 레이블 지정가능 단, frame의 행,열 크기와 맞아야 함.

print(df.values)
print(type(df))
print(type(df.values)) # numpy - array
print(df.index)
print(df.columns)  # 행-열 정보 확인 가능.
# df. ndim / size / shape도 가능

df = pd.DataFrame(np.arange(1, 10).reshape(3,3))
print(df)