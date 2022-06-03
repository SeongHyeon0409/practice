#-*- coding: utf-8 -*-
# 네이버 뉴스 수집하기

import requests, openpyxl
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
wb.save('test.xlsx')

sheet = wb.active

# 시트선택/데이터 쓰기
sheet['A1'] = 'hello world!'

# 숫자로 데이터 입력
sheet.cell(row=3, column=3).value = "BYE!!"

# 가장 마지막 줄에 데이터 입력
subject = ["Python", "Java", "HTML", "JavaScript"]
sheet.append(subject)

# sheet의 시트이름 변경
sheet.title = "1st sheet"
# 새로운 시트 만들고 sheet2에 저장
sheet2 = wb.create_sheet("2nd sheet")

# sheet1과 sheet2에 동시에 데이터 쓰기
for i in range(1, 10):
    sheet.cell(row=i, column=1).value = i
    sheet2.cell(row=1, column=i).value = i

wb.save('test.xlsx')

