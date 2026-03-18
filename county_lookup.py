# Given an address (street, city, st, zip), returns hyperlink(s) to
# relevant county's public records website, if available.
# Collin Sparks 3/18/2026

import json
import pyperclip
import urllib.error
import urllib.parse
import urllib.request
from google_geocode_api_key import key as geocode_api_key

GEOCODE_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

# parse address from clipboard
street, addr_line2 = pyperclip.paste().split("\n")
city, state_and_zip = addr_line2.split(",")
state = state_and_zip.strip()[0:2]
zipcode = state_and_zip[3:].strip()

''' debug parsing
print(f"street: {street}")
print(f"city: {city}")
print(f"state: {state}")
print(f"zipcode: {zipcode}")
'''

# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
#url = f"https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key={geocode_api_key}"

# build request URL
params = urllib.parse.urlencode(
	{
		"address": "+".join((street, city, state)),
		"key": f"{geocode_api_key}"
	}
)
url = f"{GEOCODE_BASE_URL}?{params}"

try:
	print(f"URL: {url}")
	print(f"URL: {url}")
	print(f"URL: {url}")
	response = urllib.request.urlopen(url)

except urllib.error.URLError as err:
	print("There was an error with the request.")
	print(f'{err}')
	raise err
	pass

else:
	result = json.load(response)
	if result["status"] == "OK":
		print(result)
	elif result["status"] != "UNKNOWN_ERROR":
		raise Exception(result["error_message"])
	else:
		print("Something went wrong... Unkown error.\n\n")
		raise Exception



# handle success response
for i in result["results"][0]["address_components"]:
	if "administrative_area_level_2" not in i["types"]:
		print(f"SKIP {i['types']}")
		continue
	else:
		print(f"FOUND {i['types']}")
		county = i["short_name"]
		break
print(county)