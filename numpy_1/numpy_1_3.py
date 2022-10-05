import numpy as np

# size vs len

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.size) # 9
print(len(arr1)) # 3
# size = 총 요소의 개수, len = list len이랑 같은 느낌.

#identical
# 넘파이 요소는 모두 동일한 타입. -> 그래서 리스트보다 빠르다.
arr = np.array([1,2,3,'a','b','c'])
print(arr[0]) # 1 -> numpy.str 1임 숫자 X
print(arr) # ['1' '2' '3' 'a' 'b' 'c']

#중첩배열

a = np.array([[1,2,3],[4,5,6]])
print(a[1, 0]) # 4
print(a[1, 2]) # 6
print(a[0, 2]) # 3   a[행:열] = list에서 a[행][열]이랑 같음.

# a.shape == np.shape(a)
x = a.shape # (2, 3)
y = a.shape[0] # 2
z = a.shape[1] # 3

# 구조 변경

a = np.array([[1,2,3,4,5,6], [1,2,3,4,5,6]])
a = a.reshape(3, 4) # 3행 4열로 재배열 -> a = 에 넣어줘야 a가 변경되는 거임. a.reshape만한다고 a변경 X
print(a) #[[1 2 3 4]
          #[5 6 1 2]
          #[3 4 5 6]]

arr = np.zeros((2, 2)) # (x, y) - x행y열 행렬을 0으로 초기화
print(arr)
arr = np.ones((2, 2)) # (x, y) - x행y열 행렬을 1로 초기화
print(arr)

# np.zeros((x,y)) -> O np.zeros(0, 0) -> X