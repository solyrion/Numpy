import numpy as np

# 넘파이 자료형
"""
integer                 i
unsigned integer        u
single precision float  f
double precision float  d
bool                    b
complex                 D
string                  S
unicode                 U
"""

'''
- DATA를 다루는 모듈이기에 자료형 종류가 많음.
- 각각의 자료형에느느 해당 자료형으로 변환하는 함수가 있음 (복소수 -> 정수,실수 X)
- 배열 생성시 대부분의 넘파이 함수는 자료형을 선택할 수 있음
- 넘파이 배열의 각 요소들은 모두 동일한 자료형으로 구성됨.

EX - uint8 -> 0 ~ 255
'''

ar1 = np.array([1, 2, 3.5, 4, 5])
print(type(ar1))    # <class 'numpy.ndarray'>
print(ar1.dtype)    # float64 - 3.5에 맞춰서 float으로 설정.

ar = np.array([1,2,3,4,5])
print(ar.dtype) # int64

ar = np.array([1,2,3,4,5], dtype=np.int64) # 강제로 자료형 지정 가능.
ar3 = np.arange(10, dtype = np.int64)

ar2 = np.array([1,2,3,4,-1], dtype=np.uint8)
print(ar2) # [  1   2   3   4 255]  -> -1은 uint8의 범위에 벗어나지만 출력은 대충 맞춰서 됨.

ar1 = np.array([1,2,3,4,5])
ar2 = ar1.astype(np.float64) # astype -> 새로운 타입으로 변환. as type
print(ar2) # [1. 2. 3. 4. 5.]
print(ar2.dtype) # float64

ar1 = np.array([True, False])
print(ar1.dtype) # bool



















