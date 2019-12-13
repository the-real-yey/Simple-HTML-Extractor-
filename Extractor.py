import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import csv
import os

def extract(path) :
    try:
        soup = BeautifulSoup(open(path), 'html.parser')
    
    except:
        print("error happend when parser html file:"+path)
        return
    

    for element in soup(text=lambda text:isinstance(text, Comment)): #discard comments
        element.extract()
    text = soup.find_all(text=True)
    placeholders = soup.find_all(placeholder=True)
    mattooltips = soup.find_all(mattooltip=True)
    

    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'script',
        'style',
        # there may be more elements you don't want, such as "style", etc.
    ]

    def addTextToOutput():
        global output
        for t in text:
            if not t.strip().encode('UTF-8').isdigit():
                if not isInterpolationExpressions(t):
                    if t.parent.name not in blacklist:
                        if not t.strip() in output:
                            output.append(t.strip())
                            writer.writerow([t.strip(),path])
                            


    

    def addPlaceholderTextToOutput():
        global output
        for s in placeholders:
            t=s['placeholder']
            if not t.strip().encode('UTF-8').isdigit():
                if not isInterpolationExpressions(t):
                    if s.name not in blacklist:
                        if not t.strip() in output:
                            output.append(t.strip())
                            writer.writerow([t.strip(),path])

    def addMatTooltipTextToOutput():
        global output
        for s in mattooltips:
            t=s['mattooltip']
            if not t.strip().encode('UTF-8').isdigit():
                if not isInterpolationExpressions(t):
                    if s.name not in blacklist:
                        if not t.strip() in output:
                            output.append(t.strip())
                            writer.writerow([t.strip(),path])


    def isInterpolationExpressions(t):  
        return '{{' in t.strip() and '}}' in t.strip()

    addMatTooltipTextToOutput()
    addTextToOutput()
    addPlaceholderTextToOutput()


def findHTML(path):
    global htmls
    currentPath=path
    for f in os.listdir(currentPath):
        if(os.path.isdir(currentPath +'/' +f)):
            findHTML(currentPath +'/' + f)
        else:
            if(f.split('.')[-1]=='html'):
                htmls.append(currentPath +'/' + f)

    


if __name__ == "__main__":
    output=[]
    htmls=[]
    path='src'
    findHTML(path)

    with open("names.csv", 'a+',newline="") as csvfile:
        writer = csv.writer(csvfile,dialect='excel')
        writer.writerow(['Term','Url'])
        for p in htmls:
            print('Current File' + p)
            extract(p)

    for te in output:
        print(te)