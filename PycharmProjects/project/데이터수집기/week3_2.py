# 네이버 뉴스 수집하기

import requests
from bs4 import BeautifulSoup

for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8&start="+str(n)
                       , headers={'User-Agent':'Mozilla/5.0'}) #안티 크롤링 피해가기
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.list_news > li")

    for ar in articles:
        title = ar.select_one("a.news_tit").text
        source = ar.select_one("a.info.press").text
        print(title, source)

#기사 컨테이너 선택자 ul.list_news > li
#기사 제목 선택자 a.news.tit
#언론사 선택자 a.info press

