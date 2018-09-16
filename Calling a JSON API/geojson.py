
import urllib.request as ur

import urllib.parse as up

import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address_input = input("Enter location: ")

params = {"sensor": "false", "address": address_input}

url = serviceurl + up.urlencode(params)

print("Retrieving ", url)

data = ur.urlopen(url).read().decode('utf-8')

print('Retrieved', len(data), 'characters')

json_obj = json.loads(data)



place_id = json_obj["results"][0]["place_id"]

print("Place id", place_id)