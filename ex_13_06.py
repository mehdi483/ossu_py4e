# In this assignment you will write a Python program that will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import json, urllib.request

jsonUrl = input("Please enter URL of the JSON file: ")

try:
    req = urllib.request.urlopen(jsonUrl)
except:
    print("Entered URL is not valid")
    quit()

stringData = req.read().decode()

try:
    jsonData = json.loads(stringData)
except:
    print("Entered URL does not contain a valid json")
    quit()

comments = jsonData["comments"]

totalCount = 0
for comment in comments:
    totalCount += comment["count"]

print(totalCount)