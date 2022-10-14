import numpy as np

ar1 = np.arange(10, dtype = '<u1') # 리틀엔디언 방식 - default 값
ar2 = np.arange(10, dtype = '>u1') # 빅엔디언 방식

"""
보여지는 것에는 차이가 없으나 내부적인 차이가 존재한다.
빅엔디언 = 가장 중요한 byte 먼저 저장.
리틀엔디언 = 가장 중요한 byte 나중에 저장
"""

# 자료형 확인 - np.issubdtype

ar = np.arange(10, dtype = np.uint32)
arr1 = ar.astype('float64')

print(np.issubdtype(ar.dtype, np.integer)) # True
print(np.issubdtype(ar.dtype, np.float)) # False -> 경고발생 np.floating or np.float64로 직적 써야됨
print(np.issubdtype(ar.dtype, np.floating)) # False

ar3 = ar.astype(int)
ar4 = ar.astype(float)

print(ar3.dtype) #int64
print(ar4.dtype) #float64
                 # 그냥 int / float 써도 됨