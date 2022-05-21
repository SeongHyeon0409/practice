#-*- coding: utf-8 -*-
# 네이버 영화 이미지 데이터 수집하기

from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

urlretrieve("https://movie-phinf.pstatic.net/20220504_33/165164173504831gKe_JPEG/movie_image.jpg?type=m77_110_2",
            "닥스2.png")

