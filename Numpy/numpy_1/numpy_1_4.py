import numpy as np

# 단위 행렬
# 좌측에서 우측 아래로 대각선 방향으로 요소가 1
# 다른 요소들은 0 / 정사각형 행렬

# 1차 단위행렬
arr = np.eye(1)
print(arr) # [[1.]]

# 2차 단위행렬
arr = np.eye(2)
print(arr)
'''
[[1. 0.]
 [0. 1.]]
'''

# 행렬의 곱셈
arr1 = np.eye(2)
arr2 = np.array([[3,4], [5,6]])
test = arr1*arr2
print(test) # 각 index에 맞게 단순히 곱하기만 함 -> 행렬의 곱셈 X
"""
[[3. 0.]
 [0. 6.]]
"""

test = np.dot(arr1, arr2)
print(test) # 이래야 제대로 된 행렬의 곱셈.
"""
[[3. 4.]
 [5. 6.]]
"""