# In this assignment you will write a Python program that will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
# http://py4e-data.dr-chuck.net/known_by_Alba.html

import urllib.request
from bs4 import BeautifulSoup as bs
import ssl

url = input('Enter initial address: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tries = 0
while tries <= count:
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    
    soup = bs(html, 'html.parser')
    tag = soup('a')[pos - 1]
    url = tag.get('href')
    tries += 1