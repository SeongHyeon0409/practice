#-*- coding: utf-8 -*-
# 네이버 영화 수집하기

import requests
from bs4 import BeautifulSoup

# 웹페이지에서 소스코드를 가져와 BeautifulSoup으로 파싱
raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 수집하기
movie = html.select("dl.lst_dsc")
for m in movie:
    # 영화별 데이터 수집하기
    title = m.select_one("dt.tit a")
    print("="*50)
    print(title.text)

