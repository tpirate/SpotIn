
# Imports
import requests
import json
import spotipy
# Headers
headers={
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'Authorization': 'Bearer !!! paste your auth token here !!!' 
}
# Url
url="https://api.spotify.com/v1/me/player/currently-playing"
try:
	response = requests.get(url, headers=headers)
	response.raise_for_status()
	jsonResponse = response.json()
	for key, value in jsonResponse.items():
		if key == 'item':
			jsonResponse2 = value
		for key, value in jsonResponse2.items():
			if key == 'name':
				songname = value
			elif key == 'artists':
				jsonResponse3 = value[0]
		for key, value in jsonResponse3.items():
			if key == 'name':
				artistname = value
	print(f"{artistname} {songname}")
	file = open("searcharg.txt", "w")
	file.write(f"{artistname} {songname} lyrics genius")
# Error Handling

except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)
