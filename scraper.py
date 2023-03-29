import requests
from bs4 import BeautifulSoup


# product_code=input("Podaj kod produktu: ")
product_code="105809880"

url=f"https://www.ceneo.pl/{product_code}#tab=reviews"
response=requests.get(url)
page = BeautifulSoup(response.text, "html.parser")
opinions = page.select("div.js_produc-review")

for opinion in opinions:
    pass

# print(page.prettify())
print(len(opinions))
print(type(opinions))