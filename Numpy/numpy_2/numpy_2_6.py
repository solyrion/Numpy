import numpy as np

# view - numpy의 고유한 방식 알아보기

ar = np.arange(1, 31).reshape(5, 6)
print(ar[1][1:]) # [ 8  9 10 11 12] -> 이러한 방식은 numpy의 고유방식이 아님 (느림)

a = ar[-1][2:5] # a[-1, 2:5]
a[-1] = 0 # 원본인 ar도 변경이 됨. list의 포인터개념
          # 즉 a를 통해 원본인 ar을 참조하고 있음 -> 메모리 사용에 장점이 있음
          # 이런것을 view라고 함.
print(ar)
"""
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]
 [19 20 21 22 23 24]
 [25 26 27 28  0 30]]
"""

# numpy 고유의 방식
ar = np.arange(1, 31).reshape(5, 6)
print(ar[1, 1:])

"""
지금까지 써온 이러한 방식이 numpy 고유의 인덱싱이다.
2중 list에서는 이러한 방식을 쓰지 못함.
즉 numpy는 list의 방식과 고유의 방식 2가지 모두 사용가능하다.
그러나 고유의 방식이 빠르기 때문에 어지간 하면 이 방식 사용.
"""