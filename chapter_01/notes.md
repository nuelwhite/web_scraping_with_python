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

