import requests
from bs4 import BeautifulSoup
import json

fileDir = "output.txt"
url = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228542#searchProductResult"
url2 = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228542&page=2#searchProductResult"
url3 = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228547#searchProductResult"
url4 = "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228548#searchProductResult"

r = requests.get(url2)

shoes = BeautifulSoup(r.content, "html.parser")

temp = shoes.find_all("script")
temp = (temp[10].text).replace("window.__WML_REDUX_INITIAL_STATE__ = ", "", 1)
temp = (temp).replace(";", " ")

shoeData = json.loads(temp)

file = open(fileDir, "a")
for key in shoeData['preso']['items']:
    for subKey in key['variants']['variantData']:
        # print(subKey['productImageUrl'])
        file.write(subKey['productImageUrl'] + '\n')
file.close()