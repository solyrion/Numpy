import numpy as np
import pandas as pd

ar = pd.Series(['b','a','c','d','e'])
ar1 = pd.Series([1,2,3,4,5])

print(ar[ar>'b']) # 이런식으로 **[value]** 를 기준으로 출력가능
print(ar[ar != 'b']) # T/F비교도 가능
print(ar1[ar1 > 3])

ar1 = ar1 * 2
print(ar1) #곱셈가능

a = {'강감찬':180, '이순신':185, '을지문덕':190}
ar2 = pd.Series(a)
ind = ['홍길동','강감찬','이순신','을지문덕']
ar1 = pd.Series(a, index = ind) # index 추가 가능.
print(ar1) # '홍길동'은 a에 없기 때문에 value = NaN

# Series는 2차원 배열 안됨. 애당초 1차원 배열 자료구조임.
# a = pd.Series(np.arange(1, 31).reshape(5, 6) -> 오류