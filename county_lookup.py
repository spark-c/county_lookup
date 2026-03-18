# Given an address (street, city, st, zip), returns hyperlink(s) to
# relevant county's public records website, if available.
# Collin Sparks 3/18/2026

import pyperclip
from urllib import 
from .google_geocode_api_key import key as geocode_api_key

# (fake addr for testing)
#street, addr_line2 = "28 Eckard's Way\nCooper's Hawk, NM 87532-12345".split("\n")

street, addr_line2 = pyperclip.paste().split("\n")
city, state_and_zip = addr_line2.split(",")
state = state_and_zip.strip()[0:2]
zipcode = state_and_zip[3:].strip()

print(f"street: {street}")
print(f"city: {city}")
print(f"state: {state}")
print(f"zipcode: {zipcode}")

# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
#url = f"https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key={geocode_api_key}"

