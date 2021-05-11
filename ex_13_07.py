# In this assignment you will write a Python program that will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function

import json, urllib.request, urllib.parse

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'


while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    params = dict()
    params['address'] = address
    params['key'] = api_key
    
    url = serviceurl + urllib.parse.urlencode(params)
    req = urllib.request.urlopen(url)
    data = req.read().decode()

    try:
        jsonData = json.loads(data)
    except:
        jsonData = None

    if not jsonData or 'status' not in jsonData or jsonData['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        continue
    
    print(jsonData["results"][0]["place_id"])