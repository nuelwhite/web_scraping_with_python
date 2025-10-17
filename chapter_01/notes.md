## Chapter 1 - My First Web Scrapper

In this Chapter we'll cover how to format and interpret data without a browser. In this chapter, we start with the basics of sending a ```GET request``` to a web server for a specific page, reading the HTML output from that page, and doing some simple data extraction in order to isolate the content that we are looking for.

Browsers provide a great way to make webpages more human readable, from images to videos, and even CSS styling. At the core of webpages, the HTML markup languages only provides a skeleton. Browsers help render these for useability. You can access a web page from a browser, but likewise can you access the same page with just 3 lines of python code. The only difference between the two is how human readable it is.

Example lines of code to view a webpage:
```python

    from urllib.request import urlopen

    html = urlopen('http://pythonscraping.com/pages/page1.html')

    print(html.read())
```

It returns the content of the HTML file. 

We will be using the ```urllib``` module extensively. It is a standard python library that that contains functions for accessing data across the web, handling cookies, and even changing metadata such as headers and my user agent. The python documentation for urllib provides detailed information.



###  Introduction to BeautifulSoup

The BeautifulSoup library was named after a Lewis Carroll poem of the same name in *Alice's Adventures in Wonderland*. BeautifulSoup makes sense of the nonsensical, it helps format and organize messy web data. It is designed for parsing HTML and XML documents. It has loads of functionalities:
- **Parsing HTML/XML**: It can take raw HTML or XML content and convert it into navigable tree of python objects.
- **Handling Malformed Markup**: It is robust and can handle poorly structured HTML. 
- **Navigation and Searching**: Provides methods for navigating the parse tree and searching for specific elements based on tags, attributes, CSS selectors etc using find() or findall(). 
- **Data Extraction**: Once elements are located, data extraction is easy.

### Installing BeautifulSoup

BeautifulSoup is not a standard python library, so we'd have to install it to be able to use it. Just like every other python packages, it is easy to install, whether on Linux, Mac or Windows.

- On **Linux** systems, we can install it using ```sudo apt-get install python-bs4```
- On **Mac** systems, we can install the *pip* package manager using the command ```sudo easy_install pip``` and then run ```pip install beautifulsoup4```.
- On **Windows** systems, we can download the recent release on the website, unzip the downloaded file, navigate to the folder where the file was extracted, and run ```python setup.py install```. Or you can use the *pip* package manager by using the following command ```pip install beautifulsoup4```

### Running BeautifulSoup

The most common onject used in the ```bs4``` module is ```BeautifulSoup```. 

Example:
```python
    from urllib.requests import urlopen
    from bs4 import BeautifulSoup

    html = urlopen('http://pythonscraping.com/pages/page1.html')
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)
```

The output is as follows:
```html
    <h1>An Interesting Title</h1>
```

Note that this returns only the first h1 tag on the page. By convention, there should be only one h1 tag on a page, but conventions are broken all the time, so this returns only the first h1 tag everytime, and not necessarily what we might be looking for.

When you create a BeautifulSoup object, two arguments are passed: 
- The first is the HTML text
- The second is the *parser* you want beautiful soup to use to create the object.

In the majority of the cases, it makes no difference which parser you use, but there are more than one parser available with their unique characteristics.
- **lmxl**: unlike html parser, this requires installation so **pip install lmxl** will install it. It's advantage is, it is better at parsing malformed pr messy HTML code. It can ignore issues like unclosed tags, missing head or body tags, improperly nested structures. The disadvantage it has is that it is dependent on external C libraries, and has to be installed separately as this can cause unease of use, and portability as compared to ```html.parser```.

- **html5lib**: Just like lmxl parser, it is extremely forgiving and ignores messy and malformed structures. It even goes the extra length to correct the missing or malformed tags. It is also externally dependent, and slower than lmxl and html.parser. You can install it using pip and pass it as an argument.


### Connecting Reliably and Handling Exceptions

The web is messy, data are poorly formatted, websites go down and many other challenges. A frustrating experience is scheduling a script to scrape data from a website and only to find out that the script broke down because it hit an error.
It is best practice and very important to anticipate circumstances like these; error 404, error 500, etc. This makes your scraping script robust and allows it to bounce back after failure.

In the context of scraping from this site ```'http://pythonscraping.com/pages/page1.html'``` there are a few errors we can encounter but to get started, we can anticipate these two:
- Page not found 
- Server not found.

We can handle these exceptions in the following way:

```python

    from urllib.request import urlopen
    from urllib.error import HTTPError, URLError

    try:
        html = urlopen('http://pythonscraping.com/pages/page1.html')
    except HTTPError as e:
        print(e)
        # you can return something or do a plan B
    except URLError as e:
        print("The server could not be found")
    else:
        # program continues
        # if you break or return in the except statement, you do not need an else statement
```

There is the issue of content not being what we expected on the page when the page is retrived successfully. Everytime you access a tag in a BeautifulSoup, it is smart to check and make sure the tag actually exists. If you attempt to access a tag that does not exist, BeautifulSoup returns a **None** value. For example, ```bs.some_non_existent_tag```. This returns an Exceptiopn: **AttributeError**. 

So how can we guard our script against something like this?

```python
    try:
        badContent = bs.nonExistingTag.AnotherTag
    except AttributeError as e:
        print("Tag was not found")
    else:
        if badContent == None:
            print("Tag was not found")
        else:
            print(badContent)
```




