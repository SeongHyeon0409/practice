import torch

# 1) x의 shape을 구하기
x = torch.rand(5, 4)
print("1) x의 shape:", x.shape)

# 2) 33열을 indexing을 사용하여 출력하기
element_33 = x[:, 2]  # 33열은 인덱스 2입니다 (0부터 시작)
print("2) x의 33열:", element_33)

# 3) 크기를 바꾸는 함수를 사용하여 크기 변경 후 출력
x_reshape_1 = x.view(4, 5)  # 크기를 4x5로 변경
x_reshape_2 = x.view(1, 20)  # 크기를 1x20으로 변경
print("3) 크기 변경 1:", x_reshape_1)
print("3) 크기 변경 2:", x_reshape_2)

# 4) x를 CUDA 장치 객체로 변경
x_cuda = x.to('cuda')
print("4) CUDA 장치 객체로 변경:", x_cuda)
