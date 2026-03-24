# this file shows an example to call a json api and save the response to a file 
import requests
import json

URL = "https://api.divoora.ch/web/restaurants"

PAYLOAD = {
    "areaID":4,
    "destination":{
        "_id":102865,
        "addressLine":"Via Flora Ruchat-Roncati 15, 6850 Mendrisio",
        "lat":45.8696601,
        "lng":8.9781707,
        "version":337
    },
    "testing":None,
    "target":None,
    "registered":None
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
}

response = requests.post(URL, json=PAYLOAD, headers=HEADERS)
data = response.json()

with open("restaurants.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)