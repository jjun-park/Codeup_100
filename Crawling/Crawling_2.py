import requests
from bs4 import BeautifulSoup
import pyautogui

# keyword = pyautogui.prompt("검색어를 입력하세요>>>")    # 입력창을 물리적으로 띄움
# res = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
# # f 스트링을 통해 중괄호 안에 변수 입력 받음
# html = res.text
# soup = BeautifulSoup(html, 'html.parser')
# links = soup.select(".news_tit")
# for link in links:
#     title = link.text
#     url = link.attrs['href']
#     print(title, url)

#############################

keyword = pyautogui.prompt("검색어를 입력하세요>>>")
page_num = 1    # 페이지 구분을 위해 변수 설정
last_page = int(pyautogui.prompt("마지막  페이지 번호를 입력해 주세요"))    # 마지막 페이지 번호를 입력 받음
for i in range(1, last_page * 10, 10):    # 하기 링크 내 start를 반복문으로 돌려 입력하고, 그에 따라 페이지별로 정보를 출력함
    print(f"=========={page_num} 페이지 입니다.==========")
    # 몇 페이지에 어떤 내용이 있는지 표시
    res = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    # f 스트링을 통해 중괄호 안에 변수 입력 받음 / i가 10씩 증가할 때마다 페이지 수가 1씩 증가
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")
    for link in links:
        title = link.text    # .text: 텍스트를 출력함
        url = link.attrs['href']    # .attrs: 주소를 출력함
        print(title, url)
    page_num += 1
