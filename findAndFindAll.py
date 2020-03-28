from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

# html안에 있는 class=green 값을 가진 span을 모두 가져온다
nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    # 텍스트안의 등장인물들을 모두 출력
    # get_text()는 태그를 지우고 태그안의 문자열만 반환
    # 최종 데이터를 출력, 저장, 조작하기 직전에만 사용
    print(name.get_text())

# 문서의 모든 헤더태그 반환
bs.findAll({'h1', 'h2', 'h3', 'h4', 'h5', 'h6'})

# class=red or class=green인 모든 span태그 반환
bs.findAll('span', {'class': {'red', 'green'}})
