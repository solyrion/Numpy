import numpy as np

# 기본 인덱싱 - 행기준

ar = np.arange(10)
print(ar[4:7]) # [4 5 6] -> list와 같음

ar[4:7] = 0
print(ar) # [0 1 2 3 0 0 0 7 8 9] -> 한번에 변경가능
print(ar[:]) # ar 출력

# 2차원 배열
# 1차원 배열과는 달리 ,좌우로 행, 열 분리
ar = np.arange(1, 26).reshape(5,5)
print(ar[3, :]) # [16 17 18 19 20] -> 3행의 모든 요소 ar[3,]도 같음

print(ar[4,3]) # 24 -> 4행 3열
print(ar[2,2]) # 13

print(ar[3, 1:4]) # [17 18 19]
print(ar[4, 1:3]) # [22 23]

print(ar[2:4]) # 2, 3행 두행을 출력한다.

k = ar[2:3] # 이것은 ar[2]와 내용물은 비슷하지만 배열의 차원이 다름.  ndim diff
x = ar[4] # ar[-1]과 같음 len(ar) == 5라는 기준하에