# 네이버 뉴스 수집하기

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8"
                   , headers={'User-Agent':'Mozilla/5.0'}) #안티 크롤링 피해가기
html = BeautifulSoup(raw.text, "html.parser")

