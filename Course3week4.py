import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

sum = 0

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_67905.html').read()
soup = BeautifulSoup(html,'html.parser')

#retrieve all span tags
tags = soup('span')
for tag in tags:
    sum = sum + int(tag.contents[0])
    
print(sum)
