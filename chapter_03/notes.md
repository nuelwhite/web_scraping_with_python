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

### Crawling an Entire Site
Building scrapers that scrape entire sites can be memory intensive, and it is best suited for websites for which a readily available database to store the crawled data. 
You can use scrapers to traverse entire site for some reasons like:
- Generate the sitemap
- Gather specific data 

The general approach to scrape an entire site is to start by checking the landing page (homepage) and then checking all other internal links available. Everyone of those links is then crossed, and additional links are found on each of them, which are further crawled. 

Some internal links might be duplicated, so in order to avoid duplicates and avoid crawling the same twice or more, put constraints or checks in place to make sure if a site is crawled already, it should not be crawled again. Example

```python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
            #We have encountered a new page
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)

getLinks('')
```





