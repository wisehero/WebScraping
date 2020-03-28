from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(
    'https://sports.news.naver.com/wfootball/news/index.nhn?date=20200328&isphoto=N')
bs = BeautifulSoup(html, 'html.parser')
newsTitle = bs.findAll('div', {'class': 'text'})

print(newsTitle)
