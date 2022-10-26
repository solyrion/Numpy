import numpy as np

# Broadcasting 비교연산

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,3],[1,5,2]])
c = np.array([7,8,9])
d = np.array([7,8])
e = np.array([1,2,3,4])

print(a == b)
print(a == c)
"""
[[False False  True]
 [False  True False]]
 
 [[False False False]
 [False False False]]
"""
# 각각의 요소에 대해 비교를 함  shape이 다를 경우 broadcasting을 함. (==, !=, <, >)

print(a != d)
print(a == d)
# 그래서 연산 + < > 비교는 broadcasting이 안되면 에러 발생 근데 == / != 는 출력은 됨.
# 추후에 오류를 야기할 수 있다고 오류만 뜨고 True/False출력
