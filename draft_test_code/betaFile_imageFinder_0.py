import requests
from bs4 import BeautifulSoup
import json

r = requests.get("https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228542#searchProductResult")
url5 = "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228550"
r = requests.get(url5)
# print(r.content)
shoes = BeautifulSoup(r.content, "html.parser")
print(shoes.prettify())

for link in shoes.find_all("a"):
    print(link)

for link in shoes.find_all("a"):
    if "https" in link.get("href"):
        print(link.text, link.get("href"))

for link in shoes.find_all("div", {"class": "search-product-result"}):
    # print(link.text, link.get("src"))
    print(link)

shoes.find("body").\
    find("div", {"class" : "page-full-wrapper"}).\
    find("div", {"class" : "page-content-wrapper Container"})
shoes.find_all("div")


for link in shoes.find_all("script"):
    print(link)
    if "window.__WML_REDUX_INITIAL_STATE__" in link.text:
        print(link.text)

temp = shoes.find_all("script")
temp = (temp[10].text).replace("window.__WML_REDUX_INITIAL_STATE__ = ", "", 1)
temp = (temp).replace(";", " ")
temp
type(temp)
x = json.loads(temp)
x["recommendationMap"]["addToCartStatus"]
x["ads"]



with open('data.txt', 'w') as outfile:
    json.dump(x, outfile)

for key in x:
    print(key)
x['preso']

for key in x['preso']:
    print(key)

x['preso']['items']

for key in x['preso']['items']:
    print(key)
    type(key)
    y = json.loads(key)
    for subKey in y:
        print(subKey)

for key in x['preso']['items']:
    for subKey in key['variants']['variantData']:
        print(subKey['productImageUrl'])


for key in x['preso']['items']:
    try:
        subKey = key['variants']['variantData']
        for currKey in subKey:
            print(currKey['productImageUrl'])
    except:
        pass


    for subKey in key['variants']['variantData']:
        print(subKey['productImageUrl'])
