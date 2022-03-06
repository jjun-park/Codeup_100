import requests
from bs4 import BeautifulSoup

# res = requests.get("https://www.naver.com")    # 요청 보냄
# html = res.text    # 응답 받음
# print(html)    # html 스크립트를 가져옴

#############################

# res = requests.get("https://www.naver.com")
# html = res.text
# soup = BeautifulSoup(html, 'html.parser')    # html 번역 요청
# word = soup.select_one("#NM_set_home_btn")    # "네이버를 시작페이지로" 버튼의 속성값 / #  # 표시는 id 속성을 의미 (한 개 데이터)
# print(word.text)    # 텍스트 값만 가져옴

#############################

# res = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
# html = res.text
# soup = BeautifulSoup(html, 'html.parser')
# links = soup.select(".news_tit")    # . 표시는 class 속성을 의미 (여러 개 데이터)
# for link in links:    # class 속성은 여러 개의 데이터이므로, 반복문으로 가져와야 함
#     title = link.text    # 태그 안에 텍스트 요소(문자)를 가져옴
#     url = link.attrs['href']    # href의 속성 값(주소)을 가져옴
#     print(title, url)

#############################

keyword = input("검색어를 입력하세요>>>")
res = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + keyword)
# 반드시 상기 링크의 query 값을 비워두고, 거기에 keyword 값이 입력될 수 있도록 작성해야 함
html = res.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)
