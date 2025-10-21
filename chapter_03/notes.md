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

From the output we can see all links on the webpage, notably wikipedia pages have sidebars so all those links have been extracted, but we only need relevant links. Wikipedia pages with internal links have these in common:
- They reside in a div container with id bodyContent
- URLs do not contain colons
- The URLs begin with /wiki/.

Based on these, we can revise our code to filter the irrelevant links out

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
```
The result of this shows only relevant links to Kevin Bacon. 
