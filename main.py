import numpy as np

arr = np.array([1,2,3,4,5])
print(arr.shape) # (5,) -> 모양 형태, 몸매, 체형

arr2 = np.array((['a','b','c']))
print(arr2.shape) #  3,)

arr3 = np.array([1,2,3,'a','b','c'])
print(arr3.shape) # (6,)

arr4 = np.array([[1,2,3],[4,5,6]])
print(arr4.shape) # (2, 3) -> 2행 3

arr5 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr5.shape) # (3, 4)
# shape -> 다차원으로 갈 수록 유용해짐
