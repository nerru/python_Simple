# 해당 URL 접속해서 기사 [제목, 본문, 날짜] 수집하는 함수
import requests
from bs4 import BeautifulSoup


def get_news(url: str):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")


    reg_date = doc.select("span.num_date")[0].get_text()
    print(f"날짜: {reg_date}")

    title = doc.select("h3.tit_view")[0].get_text()
    print(f"제목: {title}")


    content_list = doc.select("div.article_view p")


    content = ""

    for p in content_list:

        content += p.get_text()
    print(f"본문: {content}")