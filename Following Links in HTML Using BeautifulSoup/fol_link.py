# # To run this, you can install BeautifulSoup
# # https://pypi.python.org/pypi/beautifulsoup4

# # Or download the file
# # http://www.py4e.com/code3/bs4.zip
# # and unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')

# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url -')
position = int(input('Enter position -'))-1
count = int (input('Enter count -'))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
href = soup('a')

while count >= 0:
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tags = soup('a')
   print(url)
   url = tags[position].get("href", None)
   count = count - 1
    
    
    


