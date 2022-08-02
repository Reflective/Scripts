import requests
import selenium
from bs4 import BeautifulSoup


# Webscraper Template
# This basic webscraper uses request and beautiful soup to collect and processes data from a given URL
# Be sure to check the terms of service of the scrape target

# Hardcode URL of Scrape target
URL = "https://www.amazon.com/APC-Back-UPS-Battery-Protector-BR700G/dp/B002RCNX8K/ref=sr_1_14?crid=2T8T73O61ZL4G&keywords=backup+battery&qid=1659406301&sprefix=backup+batter%2Caps%2C108&sr=8-14"

# search "my user agent" on any browser to find your user agent
headers = {"User-Agent": "my user agent"}
# returns results of request.get to page using the defined input
page = requests.get(URL, headers=headers)

# assigns entire contents of soup
soup1 = BeautifulSoup(page.content, "lxml")
# searches saved soup instead of live site to prevent flagging
soup2 = BeautifulSoup(soup1.prettify(), "lxml")

title = (soup2.find("span", attrs={"id": "productTitle"}),)
price = (soup2.find("span", attrs={"id": "price-whole"}),)

productprice = {title, ": ", price}
# print out title and price
print(productprice)
