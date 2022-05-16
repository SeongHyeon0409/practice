#-*- coding: utf-8 -*-
# 네이버 뉴스 수집하기

import requests, openpyxl
from bs4 import BeautifulSoup

# 파일 불러오기를 시도합니다.
try:
    # 워크북 불러오기, 현재 활성화된 시트 선택하기
    wb = openpyxl.load_workbook("navernews.xlsx")
    sheet = wb.active
    print("불러오기 완료")
# 파일 불러오기에 실패하면, 새로운 워크북(엑셀파일)을 만듭니다.
except:
    # 워크북 새로 만들기, 현재 활성화된 시트 선택하기
    # 헤더 행 추가하기
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["검색어", "제목", "언론사"])
    print("새로운 파일을 만들었습니다.")

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

        sheet.append([keyword, title, source])

wb.save("navernews.xlsx")