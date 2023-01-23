import requests
url = "https://t139754.tistory.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.87 Whale/3.16.138.22 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("tistory.html", "w", encoding="utf8") as f:
    f.write(res.text)