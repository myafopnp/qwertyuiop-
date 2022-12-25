import requests
import sqlite3
from bs4 import BeautifulSoup as BS

pages_cnt = 1

links = []

while True:
    page = requests.get(f"https://apteka.ru/category/basic_care/makiyazh/?page={pages_cnt}")

    soup = BS(page.text, "html.parser")
    products = soup.findAll('a', class_='catalog-card__link', href=True)
    link = []

    for product in products:
        link.append(f"https://apteka.ru/{product['href']}")
        links.append(f"https://apteka.ru/{product['href']}")

    if link == []:
        break

    pages_cnt += 1

dess = []
for i in range(len(links)):
    page = requests.get(links[i])

    soup = BS(page.text, "html.parser")
    descriptions = soup.findAll('div', class_= "ProdDescList")

    dess.append({soup.find('div', class_="ViewProductPage__title").text: []})

    for tag in descriptions:
        dess[i][soup.find('div', class_="ViewProductPage__title").text].append({tag.h3.text: tag.text[len(tag.h3.text):]})
print(dess)
