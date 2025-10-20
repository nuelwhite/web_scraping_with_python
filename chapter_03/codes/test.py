from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs= BeautifulSoup(html, 'html.parser')

for link in bs.findall('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

