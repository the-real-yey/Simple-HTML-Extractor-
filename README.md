# Simple-HTML-Extractor(Python BeautifulSoup)
A simple extractor based on BeautifulSoup, You can use it to iterate through all the HTML files in the website root directory and get the text, placeholders and other text.
## 1. Required Packages
-Python 3 (version 3.8.0)
-BeautifulSoup 4 (version 4.4.0)
## 2. Basic Logic
### 2.1 Input:
    path: the url of the website root directory. (eg. 'CurrentRoot/src' ,'C:/User/Wbesite/src' ) Please modify this var before running this script.

### 2.2 find HTML files:
    the function 'findHTML' will be called to iterate the whole folder and store a list of urls(htmls) of all .html files in this root directory.

### 2.3 extract
    the function extract needs one reference nameed path, which should be the url of targer .html which you want to deal with(generally one of the url from htmls list)