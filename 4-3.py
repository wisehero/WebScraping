import requests
from bs4 import BeautifulSoup


class Content:
    """
    글/페이지 전체에 사용할 기반 클래스
    """

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print('New article found for topic: {}'.format(self.topic))
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('Body:\n{}'.format(self.body))


class Website:
    """
    웹사이트 구조에 관한 정보를 저장할 클래스
    """

    def __init__(self, name, url, searchUrl, resultListing,
                 resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl  # url에 검색어를 추가한 경우 검색 결과를 어디에서 얻는 지 정의
        self.resultListing = resultListing  # 각 결과에 관한 정보를 담고있는 박스
        self.resultUrl = resultUrl  # 결과에서 정확한 url을 추출할 때 사용할 태그 정보
        self.absoluteUrl = absoluteUrl  # 검색 결과가 절대url인지 상대url인지를 알려주는 불리언 값
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''

    def search(self, topic, site):
        """
        주어진 검색어로 주어진 웹사이트를 검색헤 결과 페이지를 모두 기록
        """
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs['href']
            # 상대 URL인지 절대 URL인지 확인
            if(site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print('Something was wrong with that page or URL. Skipping!')
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, url, title, body)
                content.print()


crawler = Crawler()

siteDate = [
    ['O\'Reilly Media',  # Website.name
     'http://oreilly.com',  # Website.url
     'https://ssearch.oreilly.com/?q=',  # Website.searchUrl
     'article.product-result',  # Website.resultListing
     'p.title a',  # Website resultUrl
     True,  # Website.absoluteUrl
     'h1',  # Website.titleTag
     'section#product-description'  # Website.bodyTag
     ],
    ['Reuters', 'http://reuters.com',
     'http://www.reuters.com/search/news?blob=',
     'div.search-result-content',
     'h3.search-result-title a',
     False,
     'h1',
     'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu',
     'https://www.brookings.edu/search/?s=',
     'div.list-content article',
     'h4.title a',
     True,
     'h1',
     'div.post-body']
]

sites = []
for row in siteDate:
    sites.append(Website(row[0], row[1], row[2],
                         row[3], row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']
for topic in topics:
    print('GETTING INFO ABOUT: ' + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)
