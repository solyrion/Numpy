import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(1, 31).reshape(5, 6))
# df[4, 4]와 같은 참조는 오류발생, 별도의 method필요

print(df[0]) # 오류 x df는 열기준 색인이기 떄문에 0열의 해당하는 data 출력
print(df[0][0]) # 이런 식의 참조는 가능 다만 기존 배열과 다르게 [열][행]임..
print(df[4][5]) # 에러 (index오류) -> keyerror : 5 -> [5]가 잘못됨.