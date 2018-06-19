from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

request = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
resp = urlopen(request)
html = resp.read().decode("cp949")
# print(html)

bs = BeautifulSoup(html, 'html.parser')
# print(bs.prettify())

tags = bs.findAll('div', attrs={'class': 'tit3'})
# print(tags)
for index, tag in enumerate(tags):
    print(index+1, tag.a.text, tag.a['href'], sep=' : ')