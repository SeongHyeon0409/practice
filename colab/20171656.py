# -*- coding: utf-8 -*-
"""비전-과제_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WBaLKvU0xeKFjnt0iiE0mDiUxn1eASpR

컴퓨터 비전 1차 과제
- 과제 기한: 10월 18일 자정

- 과제명: 주어진 영상을 일고 4연결성/8연결성을 이용하여 영상을 라벨링하여 색칠하기

- 제출방법: colab에서 프로그램을 작성한 후 " .py" 확장자로 다운로드하여 가상대학에 제출하시기 바람

- 파일명: 학번.py

- 과제 제출 기한을 반드시 지키고, 이후에 제출시 감정

Python 버전 확인
"""

#python --version

import numpy as np
import cv2
import matplotlib.pyplot as plt
cv2.__version__

"""이미지 다운로드"""

#wget https://i.imgur.com/iWGMlJR.png
#mv iWGMlJR.png sample.png

img = cv2.imread('sample.png')

# image 출력
plt.imshow(img)
plt.show()

"""# 4연결성과 8연결성 라벨링 출력 예시
## 숫자로 표시
![alt text](https://i.imgur.com/lQ9nXox.png)
## 색상으로 표시
![alt text](https://i.imgur.com/91M3MwP.png)

# 과제1: 4연결성 라벨링

- 위의 4연결성(4-neighbors) 라벨링과 같이 숫자 또는 색을 이용하여 라벨링하시오.
- cf. 색의 종류에는 제한이 없고, 연결된 픽셀은 같은 숫자 또는 같은 색을 가져야함.
"""

def four_connect(img):
    # 함수 작성
    height, width, a = img.shape
    mask_img = []
    l = [[0]*width for i in range(height)]
    for i in range(0, height-1):
      for j in range(0, width-1):
        img_c = img[i][j]
        if img_c[0] == 255 and img_c[1] == 255 and img_c[2] ==255:
          l[i][j] = -1


    label = 1
    for i in range(0, height-1):
      for j in range(0, width-1):
          if l[i][j] == -1:
            flood_fill4(l, i, j, label)
            label += 1


    label = 1
    t_img = [100,100,100]
    for k in range(len(l)):
      for i in range(0, height-1):
        for j in range(0, width-1):
          if l[i][j] == label:
            img[i][j] = t_img

      label += 1
      t_img = re_color(t_img, 10, 15, 20)

    return  img

def re_color(img, a, b, c):
  img[0] = img[0] + a if img[0] + a <= 255 else img[0] + a - 255
  img[1] = img[1] + b if img[1] + b <= 255 else img[1] + b - 255
  img[2] = img[2] + c if img[2] + c <= 255 else img[2] + c - 255

  return img

def flood_fill4(l,i,j,label):
    if l[i][j] == -1:
      l[i][j] = label
      flood_fill4(l,i,j+1,label)
      flood_fill4(l,i-1,j,label)
      flood_fill4(l,i,j-1,label)
      flood_fill4(l,i+1,j,label)

img = cv2.imread('sample.png')

labeled_img = four_connect(img)

# image 출력
plt.imshow(labeled_img)
plt.grid(None)   
plt.xticks([])
plt.yticks([])
plt.show()

"""과제2: 8연결성 라벨링
- 위의 8연결성(8-neighbors) 라벨링과 같이 숫자 또는 색을 이용하여 라벨링하시오.
- cf. 색의 종류에는 제한이 없고, 연결된 픽셀은 같은 숫자 또는 같은 색을 가져야함.-
"""

def eight_connect(img):
    # 함수 작성
    height, width, a = img.shape
    mask_img = []
    l = [[0]*width for i in range(height)]
    for i in range(0, height-1):
      for j in range(0, width-1):
        img_c = img[i][j]
        if img_c[0] == 255 and img_c[1] == 255 and img_c[2] ==255:
          l[i][j] = -1


    label = 1
    for i in range(0, height-1):
      for j in range(0, width-1):
          if l[i][j] == -1:
            flood_fill8(l, i, j, label)
            label += 1


    label = 1
    t_img = [100,100,100]
    for k in range(len(l)):
      for i in range(0, height-1):
        for j in range(0, width-1):
          if l[i][j] == label:
            img[i][j] = t_img

      label += 1
      t_img = re_color(t_img, 50, 100, 150)

    return  img

def re_color(img, a, b, c):
  img[0] = img[0] + a if img[0] + a <= 255 else img[0] + a - 255
  img[1] = img[1] + b if img[1] + b <= 255 else img[1] + b - 255
  img[2] = img[2] + c if img[2] + c <= 255 else img[2] + c - 255

  return img

def flood_fill8(l,i,j,label):
    if l[i][j] == -1:
      l[i][j] = label
      flood_fill8(l,i,j+1,label)
      flood_fill8(l,i-1,j+1,label)
      flood_fill8(l,i-1,j,label)
      flood_fill8(l,i-1,j-1,label)
      flood_fill8(l,i,j-1,label)
      flood_fill8(l,i+1,j-1,label)
      flood_fill8(l,i+1,j,label)
      flood_fill8(l,i+1,j+1,label)

img = cv2.imread('sample.png')

labeled_img = eight_connect(img)

# image 출력
plt.imshow(labeled_img)
plt.grid(None)   
plt.xticks([])
plt.yticks([])
plt.show()