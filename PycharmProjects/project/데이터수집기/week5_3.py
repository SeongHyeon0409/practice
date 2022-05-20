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

    url = "https://movie.naver.com" + title.attrs["href"]
    print(url)

    raw_each = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text, 'html.parser')

    # 컨테이너(댓글) 수집
    reply = html_each.select("div.score_result li")
    print("-" * 50)
    print("평점과 댓글:")
    for r in reply:
        # 평점, 댓글 수집/출력
        score = r.select_one("div.star_score em").text
        reply = r.select_one("div.score_reple p").text
        print(score, reply)