import numpy as np

arr = [1,2,3,4]
print(type(arr)) # list

arr1 = np.array(arr)
print(type(arr1)) # <class 'numpy.ndarray'>

# Size
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1.size) # 6 size 몇차원인지 아는데는 도움X

#ndim
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1.ndim) # 차원