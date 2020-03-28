from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# table태그 중 id가 giftList인 것의 자식들을 전부 반환
# for child in bs.find('table', {'id': 'giftList'}).children:
#    print(child)

# table태그의 첫번째 tr을 건너뛴 나머지만 출력 (제목을 안뽑을 때 유용)
# for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
#    print(sibling)

print(bs.find('img', {'src': '../img/gifts/img1.jpg'
                      }).parent.previous_sibling.get_text())
