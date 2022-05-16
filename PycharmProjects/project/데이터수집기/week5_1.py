#-*- coding: utf-8 -*-
# 네이버 영화 수집하기

import requests, openpyxl
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.naver", headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, 'html.parser')

movie = html.select("dl.lst_dsc")

for m in movie:
    title = m.select_one("dt.tit a")
    score = m.select_one("div.star_t1 span.num")

    # 방법 1
    info = m.select("dl.info_txt1 dd")

    # genre = info[0].select("a")
    # directors = info[1].select("a")
    # actors = info[2].select("a")

    # 방법 2
    # nth-of-type을 활용해서 데이터를 선택합니다.
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    directors = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    actors = m.select("dl.info_txt1 dd:nth-of-type(3) a")

    if float(score.text) < 8.5:
        continue

    genre_all = m.select_one("dl.info_txt1 dd:nth-of-type(1) span.link_txt")
    if "액션" not in genre_all.text:
        continue

    print("=" * 50)
    print("제목:", title.text)

    print("-" * 50)
    print("평점:", score.text)

    print("-" * 50)
    print("장르:")
    for g in genre:
        print(g.text)

    print("-" * 50)
    print("감독:")
    for d in directors:
        print(d.text)

    print("-" * 50)
    print("출연:")
    for d in actors:
        print(d.text)