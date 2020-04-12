from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

context = ssl._create_unverified_context()

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl),
                   context=context)
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새 페이지를 발견
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)  # 새로운 페이지는 세트에 추가
                getLinks(newPage)  # 새로운 페이지 탐색을 위해 재귀호출


getLinks('')
