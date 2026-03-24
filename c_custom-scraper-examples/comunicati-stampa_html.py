# this file shows an example of how to parse html and save the response to a file 
import json
import requests
from bs4 import BeautifulSoup

URL = "https://www4.ti.ch/tich/area-media/comunicati"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

comunicati = []

for item in soup.find_all("li", class_="no-list"):
    info = item.find("p", class_="dipartimento")
    parts = [s.strip() for s in info.stripped_strings]

    comunicati.append({
        "tag": item.find("span", class_="etichettaHome").get_text(strip=True),
        "department": parts[0],
        "date": " ".join(parts[1].split()) if len(parts) > 1 else "",
        "title": " ".join(item.find("h1").get_text().split()),
        "link": "https://www4.ti.ch" + item.find("a")["href"],
    })

with open("comunicati.json", "w") as f:
    json.dump(comunicati, f, indent=2, ensure_ascii=False)

