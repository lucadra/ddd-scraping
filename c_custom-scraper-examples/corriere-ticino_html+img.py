# this file shows an example of how to parse html and download images 
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.cdt.ch/search?qs=frontalieri"

response = requests.get(URL)

page = BeautifulSoup(response.text, "html.parser")

articles = page.find_all("article", class_="horizontal")

for article in articles: 
    img_url = article.find("img")["src"]
    title = article.find("div", class_="title").get_text()
    subtitle = article.find("div", class_="subtitle").get_text()
    slug = article.find("a")["href"]
    date = article.find("div", class_="date-pubblication").get_text()

with open("articles.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["img_url", "title", "subtitle", "slug", "date"])
    for i, article in enumerate(articles):
        img_url = article.find("img")["src"]
        title = article.find("div", class_="title").get_text()
        subtitle = article.find("div", class_="subtitle").get_text()
        slug = article.find("a")["href"]
        date = article.find("div", class_="date-pubblication").get_text()
        writer.writerow([img_url, title, subtitle, slug, date])
        
        r = requests.get(img_url)
        with open(f"images/{i}.jpg", "wb") as img_file:
            img_file.write(r.content)