import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET



url = input ("Enter url: ")
response = urllib.request.urlopen(urllib.request.Request(url)).read() 

tree = ET.fromstring(response)
data = tree.findall('.//count')

print (sum( [ int(i.text) for i in data ] ))