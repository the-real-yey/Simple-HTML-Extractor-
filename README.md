# Simple-HTML-Extractor(Python BeautifulSoup)
A simple extractor based on BeautifulSoup, you can use it to iterate through all the HTML files in the website root directory and get the text, placeholders and other text.
## 1. Required Packages
-Python 3 (version 3.8.0)
-BeautifulSoup 4 (version 4.4.0)
-CSV tool
## 2. Basic Logic
### 2.1 Input:
-`path`: the url of the website root directory. (eg. 'CurrentRoot/src' ,'C:/User/Wbesite/src' ) 
Please modify this var before running this script.

### 2.2 Find HTML files:
The function `findHTML` will be called to iterate the whole folder and store a list of urls(`htmls`) of all .html files in this root directory.

### 2.3 Extract terms:
-The function `extract` needs one reference named path, which should be the url of targer .html which you want to deal with(generally one of the url from htmls list)  <br><br>
-This script is going to aim 3 types of text: `Text`, `Placeholder`,`Mattooltip`. (Detailed script description on BeautifulSoup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
```Python  
    text = soup.find_all(text=True)
    placeholders = soup.find_all(placeholder=True)
    mattooltips = soup.find_all(mattooltip=True)
```
-Filters: there is a list called `blacklist` which contains all the tag names we want to ignore(e.g header, meta,style). For any specific tags, you can just add the tag name into this list to block them.<br><br>
```Python
if s.name not in blacklist
```
-Rules: Generally, we need to block some meaningless texts like digits and interpolation expressions(Angular):<br>
`digit`:
```Python  
if not t.strip().encode('UTF-8').isdigit(): 
```
`Interpolation expressions`:
```Python 
if not isInterpolationExpressions(t):
### following 


def isInterpolationExpressions(t):  
        return '{{' in t.strip() and '}}' in t.strip()
```

### 2.4 Generate output
In this script, this expected output is .csv spreadsheet file. Python 3.8.0 combined with the csv tool:
```Python
with open("names.csv", 'a+',newline="",encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile,dialect='excel')
        writer.writerow(['Term','Url'])
        for p in htmls:
            print('Current File' + p)
            extract(p)
            
            
extract(path):
  ### 
  code
  ###
  
  def addTextToOutput():
    ###
    code
    ###
    writer.writerow([t.strip(),path])
    
    
  def PlaceholderTextToOutput():
    ###
    code
    ###
    writer.writerow([t.strip(),path])
    
  def addMatTooltipTextToOutput():
    ###
    code
    ###
    writer.writerow([t.strip(),path])
```

CSV tool is openning file `name.csv` with encoding in `utf-8`, then `extract` function will add new rows including required `Texts`, `Placeholders` and `Mattooltips`.

## 3. Output
The ideal output includes two Column `Term` and `Url` <br>

| Term            | Url                                                                 |
|-----------------|---------------------------------------------------------------------|
| Forgot password | src/app/view/account/forgot-password/forgot-password.component.html |
| close           | src/app/view/account/forgot-password/forgot-password.component.html |
| Cancel          | src/app/view/account/forgot-password/forgot-password.component.html |
| Send            | src/app/view/account/forgot-password/forgot-password.component.html |
| Client Code     | src/app/view/account/forgot-password/forgot-password.component.html |
| User Name       | src/app/view/account/forgot-password/forgot-password.component.html |
| ...             | ...                                                                 |
