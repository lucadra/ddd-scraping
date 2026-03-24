import json 
import requests
from bs4 import BeautifulSoup
import csv 

URL = "https://api.ticino.ch/fileadmin/api/events"

response = requests.get(URL)

content = response.json()

items = content["content"][0]["data"]["items"]

# Extract the dictionary part from each item (since it's a list containing a dict)
events = [item[0] for item in items]

keys = events[0].keys()

for event in events: 
    image_url = event["imageName"]
    r = requests.get(image_url)
    with open(f"images/{event['itemId']}.jpg", "wb") as img_file:
        img_file.write(r.content)

with open("events.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=keys) 
    writer.writeheader()      # Write the column names
    writer.writerows(events)  # Write all the event dictionaries