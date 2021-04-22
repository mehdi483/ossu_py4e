# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
# file address: http://py4e-data.dr-chuck.net/comments_1210182.html
# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers

import urllib.request
from bs4 import BeautifulSoup as bs
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1210182.html', context=ctx).read()

soup = bs(html, 'html.parser')
tags = soup('span')

total = 0
for tag in tags:
    total += int(tag.contents[0])

print(total)