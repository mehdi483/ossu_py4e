import xml.etree.ElementTree as et, urllib.request

xmlUrl = input("Please enter URL of the xml file: ")

try:
    req = urllib.request.urlopen(xmlUrl)
except:
    print("Entered URL is not valid")
    quit()

data = req.read().decode()

try:
    xmlData = et.fromstring(data)
except:
    print("Entered URL does not contain a valid xml")
    quit()

countElements = xmlData.findall('./comments/comment/count')

totalCount = 0
for countElement in countElements:
    totalCount += int(countElement.text)

print("Total comments count: ", str(totalCount))
