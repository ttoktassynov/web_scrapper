import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
html = response.content
scraped = BeautifulSoup(html, 'html.parser')
articles = scraped.select(".product_pod")
title_prices = {}
for article in articles:
    title = article.h3.a["title"]
    price = float(article.find("p", class_ = "price_color").text.lstrip("£"))
    title_prices[title] = price
for title, price in title_prices.items():
    print('A book {} is worth £{}'.format(title, price))
