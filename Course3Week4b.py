import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
position = input('Enter position: ')
position = int(position)-1

for i in range(int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position].get('href',None)

name = re.findall('by_(.*).html',url)
print(name[0])

# Retrieve all of the anchor tags
#tags = soup('a')
#print(tags[2].get('href',None))
#for tag in tags:
#    print(tag.get('href', None))