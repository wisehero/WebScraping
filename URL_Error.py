'''서버를 전혀 찾을 수 없을때, 예를 들어 페이지가 다운되었거나 URL에 오타가 있을 때 
urlopen은 URLError 예외를 일으킨다. 이러한 예외는 다음과 같이 캐치'''


from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError

try:
    html = urlopen('http://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')
