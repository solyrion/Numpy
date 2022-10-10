import numpy as np

# np.arange(n)

arr = np.arange(10)
print(arr) # [0 1 2 3 4 5 6 7 8 9] 0~n-1까지 자동으로 numpy배열 생성

arr = np.arange(0, 10, 3)
print(arr) # [0 3 6 9] 기본적으로 for문과 비슷.

arr = np.arange(1, 5, 0.5)
print(arr) # [1.  1.5 2.  2.5 3.  3.5 4.  4.5] 증가량이 소수도 가능.
           # 특이한것은 4.5? (1, 5) = 1 ~ 4인데? -> 이것은 (x,y,z)중 z가 없다면 디폴트가 1임
           # 즉 z가 있다면 y-z까지임.

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

arr = np.arange(1, 10)
arr = arr.reshape((3, 3))
print(arr) # 위의 방식보다 arange + reshape를 통해 일일이 쓸 필요없이 간단히 가능함.

arr = np.arange(1, 37)
arr = arr.reshape((6, 6))
print(arr) # 데이터가 많아질수록 편해짐. (arr.reshape() 해도 arr이 reshape 되지 않음
           # arr = arr.reshape() 해야됨

arr = np.arange(1, 37).reshape(6, 6) # 한번에도 가능
print(arr)















