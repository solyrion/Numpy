import numpy as np

# reshape(-1, n) / reshape(n, -1) n은 정수

ar = np.arange(12).reshape(3, 4)
ar1 = ar.reshape(-1, 2)
print(ar1) # (-1, n)일때 n에 맞게 알아서 배열을 함.
           # size=12 기준 (-1, 2) -> (6, 2) / (-1, 3) -> (4, 3)

ar2 = ar.reshape(3, -1)
print(ar2) # (n, -1)이여도 n에 맞춰서 배열을 함. (3, -1) -> (3, 4)
           # size에 맞게 n을 기준으로 맞출 수 없다면 오류발생.
           # EX) size = 12 -> (-1, 5) -> 오류

ar1 = ar.reshape(-1)
print(ar1) # [ 0  1  2  3  4  5  6  7  8  9 10 11]
           # ar.reshape(-1) == ar.reshape(1, -1) != ar.reshape(-1, 1)

ar1 = ar.reshape(-1, -1) # 맞춰줄 기준이 없기 떄문에 오류발생

ar2 = ar.reshape(6, -45)
print(ar2) # 구지 -1이 아니더리도 - 라면 똑같이 작동함.





















