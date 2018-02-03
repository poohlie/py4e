import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

counts=0
sum=0

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    
    results = tree.findall('.//count')
    counts = len(results)
    for result in results:
        #print(result.text)
        sum = sum + int(result.text)
    break

print('Count: '+str(counts))
print('Sum: '+str(sum))

    #results = tree.findall('result')
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text
