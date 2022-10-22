import numpy as np

# 짝수행만 출력
ar = np.arange(1, 31).reshape(5, 6)

for i in range(len(ar)):
    if i%2 == 0:
        print(ar[i])
"""
len(ar) 대신 ar.shape[0]도 가능
이런식으로 가능은 하지만 데이터 양이 커질 수록 너무 시간이 오래걸림.
짝수 열만 출력하는 것도 반복문으로 가능하지만 마찬가지의 문제가 생김
"""

# numpy 고유방식 사용
print(ar[::2]) # 짝수 행만 출력

"""
::2 -> ???
for문에서 for i in range(1, 10, 2)랑 비슷한 거임
::2 -> 첫번째 : 앞뒤에 없다는 것은  처음부터 끝까지라는 뜻. [ ar[:] == ar ]

즉 크게 X : Y : Z로 보면 됨.
"""

print(ar[:3:3])
"""
앞 :3 -> 0~2까지
뒤 :3 -> 3칸씩
"""

print(ar[1::2]) # 홀수 행만 출력
print(ar[:, ::2]) # 짝수 열만 출력
print(ar[:, 1::2]) # 홀수 열만 출력
print(ar[:, 1:4:2])