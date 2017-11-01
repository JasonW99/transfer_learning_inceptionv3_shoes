import requests
from bs4 import BeautifulSoup
import json

fileDir = "output5.txt"
maxPage = 1

url = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228542&page="
# url = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228542#searchProductResult"
# url2 = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228542&page=2#searchProductResult"
# url3 = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228547#searchProductResult"
# url4 = "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228548#searchProductResult"
url5 = "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228550"

def main(url = url5, maxPage = maxPage, fileDir = fileDir):
    file = open(fileDir, "a")

    for i in range(1, maxPage + 1):
        currUrl = url + "&page=" + str(i) + "#searchProductResult"

        r = requests.get(currUrl)

        shoes = BeautifulSoup(r.content, "html.parser")

        temp = shoes.find_all("script")
        temp = (temp[10].text).replace("window.__WML_REDUX_INITIAL_STATE__ = ", "", 1)
        temp = (temp).replace(";", " ")

        shoeData = json.loads(temp)
        for key in shoeData['preso']['items']:
            try:
                subKey = key['variants']['variantData']
                for currKey in subKey:
                    file.write(currKey['productImageUrl'] + '\n')
            except:
                pass
    file.close()

if __name__ == "__main__":
    main()
