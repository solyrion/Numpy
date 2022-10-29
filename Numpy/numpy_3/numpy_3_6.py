import numpy as np

# append 매서드
# axis = 0은 행 추가 / axis = 1은 열 추가

a = np.array([])
a = np.append(a, 1) # 이러한 방식으로 append / a에 다시 대입해줘야 append처리됨
a = np.append(a, np.array([3, 4]))
# 특이한 점은 [3, 4]를 추가해도 list append와는 다르게 3, 4가 추가됨([3, 4]가 아닌)

b = np.empty((3, 3), dtype=int) # 의미없는 숫자로 채운 배열 생성 (dtype 설정가능)
print(b)

u = np.empty((5, 5))
print(u.dtype) # float64가 default 값

z = np.empty_like(a, dtype=int)
print(z) # 그냥 empty만 쓰면 오류 _like하면 인자의 크기와 같게 empty형성
# empty는 초기화하지 않는다는 점에서 살짝 빠른 장점이 있음

ar = np.ones((5, 5), dtype=int)
ar = np.append(ar, np.array([[3,4,5,6,7]]), axis = 0) # 행에 추가해줌 (열 개수 맞춰주어야 함)
print(ar)


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
addcol = np.zeros((2, 1), int) # 추가할 배열을 미리 설정
arr = np.append(arr, addcol, axis = 1)
print(arr)

arr = np.append(arr, np.array([[100], [200]]), axis=1)
print(arr)
"""
[[  1   2   3   4   5   0 100]
 [  6   7   8   9  10   0 200]]
"""