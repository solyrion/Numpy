import numpy as np

# int != int_ -> int32 or int64 -> 일반적인 정수형 배열은 int_ / int는 오류

a = np.int_([1,2,3,4,5])
print(a.dtype) # int64

c = np.int(190)
print(type(c)) # <class 'int'> / dtype은 오류발생

a = np.float_(4) # float_ == float64
print(a) # 4.0
print(a.dtype) # float64 / float_으로 생성했기에 dtype사용가능

# 타입지정

ar1 = np.arange(10, dtype = np.uint8)
print(ar1) # [0 1 2 3 4 5 6 7 8 9]
print(ar1.dtype) # uint8

ar1 = np.arange(10, dtype = 'uint8')
print(ar1) # [0 1 2 3 4 5 6 7 8 9]
print(ar1.dtype) # uint8

ar1 = np.arange(10, dtype = 'u8') # 코드사용
print(ar1.dtype) # uint64 / ??? u8 == uint8 ? -> X
                 # 'u8'처럼 코드(문자열)로 썻을때 뒤의 숫자는 byte임. 8byte = 64 bit

x = np.dtype('float64')
print(x.type) # <class 'numpy.float64'>
print(x.str) # <f8 -> float64에 대해 문자코드로 출력을 해달라. + 리틀엔디언