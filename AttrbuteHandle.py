from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    # h1 태그가 없을 경우 None을 반환하게 함
    except AttributeError as e:
        return None
    # h1 태그가 존재하면 h1의 컨텐츠 반환
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
# 제목이 없는 태그일 떄
if title == None:
    print('Title could not be found')
# 제목이 있는 태그일 때
else:
    print(title)
