## Chapter 2 - Advanced HTML Parsing

In this chapter, we look at how to parse complicated HTML pages, to extract the data we only need.

Every webpage contains stylesheets. To think that CSS is only there to make webpages human readable and for browsers only is not accurately true. CSS relies on the differentiation of HTML elements that otherwise might have the same markup in order to style them separately. Some tags might look like this:
```html
    <span class="red"></span>
```

or 

```html
    <span class="green"></span>
```

Web scrapers can easily distinguish these two tags based on their classes. for example, we can use BeautifulSoup to grab all the "red" classes, but not the "green" clasess. 

Let's create a scraper that scrapes this site: http://www.pythonscraping.com/pages/warandpeace.html. On this page, words spoken by the characters in the story are in red, and the names of the characters are in green. You can grab the entire page and create a BeautifulSoup.

```python
    
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    soup = BeautifulSoup(html, 'html.parser')

    nameList = soup.findAll('span', {'class': 'green'})

    for name in nameList:
        print(name.get_text())

```

When executed, it will return a list of all proper nouns in the text, in the order as they appear on the page. In the previous chapter we directly called or used bs.tagName to access a tag's content, but in this chapter we've seen findAll. It returns a list of tags on a webpage.

The **get_text()** here returns only text content, it separates the tags from the content. It is recommended to only use it when you want specific content extracted. 

### find and find_all() with BeautifulSoup

The *find* and *find_all()* are the two most likely used methods in the beautiful soup module. You can easily filter HTML files to find desired tags or a single tag, based on their various attributes. Both functions share similar properties

```python

    find_all(tag, attributes, recursive, text, limit, keywords)
    find(tag, attributes, recursive, text, keywords)
```

In most cases, the first two arguments are the only ones you will need in your script. Let's take a look at the various arguments and what they are for:
- **tag**: you can pass a string name of list of string tag names. eg: find_all(['h1', 'h2', 'h3'])
- **attributes**: this argument takes a python dictionary of attributes and matches tags that contains any of those attributes. eg: find_all('span', {'class': 'green', 'red'})
- **recursive**: this argument is a boolean which is set to *True* by default. It looks into children, and grandchildren tags for tags that match your parameters.
- **text**: this argument matches based on the text content on the page. eg: find_all(text="the prince") returns all items with the text the prince.
- **limit**: this argument is only used in find_all function. It is used to retrieve only the first n elements.
- **keywords**: this argument allows you to select tags that contain a particular attribute or set of attributes. 

### Navigating Trees

The find_all function is responsible for finding tags based on their name and attributes. But what if you need to find a tag based on its location in a document. In chapter we could access tags like this bs.tag.subTag.anotherSubTag. 


#### Dealing with Children and Descendants

In the BeautifulSoup library, there is a distinction between children and descendants. Just like in a human family tree, children are one level level below and descendants are more than one level. It is the same here. All children are descendants, but not all descendants are children. 

Generally, BeautifulSoup functions always deal with the descendants of the current tag selected. For instance, bs.body.h1 selects the first h1 tag in the descendant of the body tag. It will not find tags located outside the body tag. 

Similarly, bs.div.find_all('img') will find the first div tag in the document and retrieve all 'img' tags that are descendants of the div. 

To find only descendants, you can use the .children() attribute in BeautifulSoup:
```python

    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen('http://www.pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html, 'html.parser')

    for child in bs.find('table', {'id':'giftList'}).children:
        print(child)

```

This code prints the list of product rows in the giftList table, including the initial row of column labels. If you use *descendants()* instead, you will get all descendant tags.













