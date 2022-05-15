#-*- coding: utf-8 -*-
# 네이버 뉴스 수집하기

import requests, openpyxl
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "언론사"])


keyword = input("검색어를 입력해주세요: ")

# 반복1: 기사번호를 변경시키면서 데이터 수집을 반복하기
# 1 ~ 100까지 10단위로 반복(1, 11, ..., 91)
for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query="+keyword+"&start=" + str(n),
                       headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.list_news > li")

    # 반복2: 기사에 대해서 반복하면 세부 정보 수집하기
    # 리스트를 사용한 반복문으로 모든 기사에 대해서 제목/언론사 출력
    for ar in articles:
        title = ar.select_one("a.news_tit").text
        source = ar.select_one("a.info.press").text
        source = source.replace("언론사 선정", "")
        print(title, source)

        sheet.append([title, source])

wb.save("navernews.xlsx")