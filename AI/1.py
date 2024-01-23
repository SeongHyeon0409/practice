import numpy as np

# A 행렬 선언
A = np.array([[1, 3], [4, 2]])

# A 행렬의 역행렬 계산
A_inv = np.linalg.inv(A)

# 결과 출력
print(A_inv)