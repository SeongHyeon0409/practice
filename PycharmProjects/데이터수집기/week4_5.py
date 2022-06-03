#-*- coding: utf-8 -*-
# 네이버 뉴스 수집하기

import requests, openpyxl
from bs4 import BeautifulSoup

import requests, openpyxl
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "채널", "재생 수", "좋아요 수"])

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

# 1위 - 100위 컨테이너 선택자: dl.cds_info
clips = html.select("dl.cds_info")

for cl in clips:
    # 수정된 부분
    title = cl.select_one("dt.title").text.strip()
    chn = cl.select_one("dd.chn").text.strip()
    hit = cl.select_one("span.hit").text.strip()
    like = cl.select_one("span.like").text.strip()

    hit = hit.replace("재생 수", "")
    like = like.replace("좋아요 수", "")

    print("제목", title)
    print("채널명", chn)
    print(hit)
    print(like)
    print("=" * 50)

    sheet.append([title, chn, hit, like])

wb.save("navertv.xlsx")