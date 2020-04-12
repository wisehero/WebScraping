from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import re
import random
import datetime

context = ssl._create_unverified_context()

random.seed(datetime.datetime.now())

# 링크를 가져와서 링크안에 있는 href값을 뿌려주는 함수


def getLinks(articleUrl):
    html = urlopen(
        'https://en.wikipedia.org{}'.format(articleUrl), context=context)  # url을 받아서
    bs = BeautifulSoup(html, 'html.parser')  # soup로 만들어 준 다음
    # 그 페이지 안에 있는 모든 링크를 일정한 형식으로 뱉어냄
    return bs.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')  # 링크 리스트 생성

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
