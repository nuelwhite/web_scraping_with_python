from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

# create a function to get the title

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.h1
    except AttributeError as e:
        return None

    return title

title = getTitle('http://pythonscraping.com/pages/page1.html')

if title == None:
    print("Title could not be found")
else:
    print(title)
