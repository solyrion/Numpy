import numpy as np
import pandas as pd

"""
series
    - 판다스의 고유 타입이자 자료구조
    - 라벨로 이루어진 자료구조, 1차원 배열
    - dict/numpy_arr 등 여러 방식으로 생성가능
    - index / value 둘다 확인이 가능.능
    - Dataframe return값은 Series로
"""

# 대소문자 조심

ar = pd.Series([1,2,3,-4,5])
ar2 = pd.Series(np.arange(5))
print(ar)
print(type(ar))
print(ar.index) # RangeIndex(start=0, stop=5, step=1) (0 ~ 4까지 1씩)
print(ar.values) # [ 1  2  3 -4  5]

ar = pd.Series([1,2,3,-4,5], index = ['a','b','c','d','e'])
print(ar) # index지정 가능

a = {'a':1, 'b':2, 'c':3}
ar = pd.Series(a)
ar.name = "abc 숫자" # series name도 지정가능
ar.index = ['k','z','j'] # 기존 series의 index크기와 같아야됨 아니면 오류
print(ar) # 딕셔너리도 index/value 설정가능.
print(ar[0])
print(ar['k'])
print(ar[1:3])