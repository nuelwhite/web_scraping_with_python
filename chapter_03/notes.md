## Chapter 3 - Writing Web Crawlers

### Traversing a Single Domain

The **Six Degrees of Wikipedia** just like the Six Degrees of Kevin Bacon is a concept that helps to link two unlikely subjects by a chain containing no more than six total (chains). In this lesson we will use this concept to find and link websites on wikipedia. Wikipedia provides a stable HTML structure.

A python script that retrieves a webpage and produces a link of lists on the page:

```python 

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs= BeautifulSoup(html, 'html.parser')

for link in bs.findall('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
```
