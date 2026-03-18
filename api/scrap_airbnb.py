import requests
from bs4 import BeautifulSoup
import json

url = "https://www.airbnb.com.br/rooms/1581264694372549727/reviews"

html = requests.get(url).text
soup = BeautifulSoup(html,"html.parser")

reviews = []

for r in soup.select(".review"):
    reviews.append({
        "author": r.select_one(".author").text,
        "text": r.select_one(".text").text
    })

data = {
 "rating":4.9,
 "total":len(reviews),
 "reviews":reviews
}

with open("airbnb-reviews.json","w") as f:
    json.dump(data,f)