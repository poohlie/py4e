import urllib.request, urllib.parse, urllib.error
import json

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    counts=0
    sum=0
    
    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    #print(info)

    counts = len(info)
    #print(counts)

    for item in info['comments']:
        sum = sum + item['count']
    print('Count: ',counts)
    print('Sum: ',sum)



