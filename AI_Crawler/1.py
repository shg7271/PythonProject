import requests
from bs4 import BeautifulSoup

# 특정 URL에 접속하는 요청(Request) 객체를 생성합니다.
request = requests.get('https://www.mofa.go.jp/region/asia-paci/takeshima/index.html')
# https://www.kr.emb-japan.go.jp/territory/takeshima/g_ninchi.html
# https://www.kr.emb-japan.go.jp/territory/takeshima/index.html
# 접속한 이후의 웹 사이트 소스코드를 추출합니다.
html = request.text

# HTML 소스코드를 파이썬 객체로 변환합니다.
soup = BeautifulSoup(html, 'lxml')
#print(soup)
# <a> 태그 포합하는 요소를 추출합니다.
links = soup.select('div > a')

# 모든 링크에 하나씩 접근합니다.
for link in links:
    # 링크가 href 속성을 가지고 있다면
    #if link.has_attr('href'):
        # href 속성의 값으로 notice라는 문자열이 포함되어 있다면
    #   if link.get('href').find('notice') != -1:
    print(link.text)
#print(html)