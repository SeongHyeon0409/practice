# 네이버tv 인기 영상 1~3 수집하기

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")
#print(raw.text)

html = BeautifulSoup(raw.text, "html.parser")
#print(html)

clips = html.select("div.inner")
#print(clips[0])

# 데이터 수집부분
title = clips[0].select_one("dt.title")
chn = clips[0].select_one("dd.chn")
hit = clips[0].select_one("span.hit")
like = clips[0].select_one("span.like")

# 수집결과 출력부분
for cl in clips:
    title = cl.select_one("dt.title")
    chn = cl.select_one("dd.chn")
    hit = cl.select_one("span.hit")
    like = cl.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())