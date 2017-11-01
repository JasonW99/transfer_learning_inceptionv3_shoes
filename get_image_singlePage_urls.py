#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import getopt
import requests
from bs4 import BeautifulSoup
import json

# fileDir = "output5.txt"
# maxPage = 1
# url = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228542&page="
# url = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228542#searchProductResult"
# url2 = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228542&page=2#searchProductResult"
# url3 = "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228547#searchProductResult"
# url4 = "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228548#searchProductResult"


def main(url, max_page, file_dir):
    file = open(file_dir, "a")
    for i in range(1, max_page + 1):
        curr_url = url + "&page=" + str(i) + "#searchProductResult"
        r = requests.get(curr_url)
        shoes = BeautifulSoup(r.content, "html.parser")
        temp = shoes.find_all("script")
        temp = temp[10].text.replace("window.__WML_REDUX_INITIAL_STATE__ = ", "", 1)
        temp = temp.replace(";", " ")
        shoe_data = json.loads(temp)
        for key in shoe_data['preso']['items']:
            try:
                sub_key = key['variants']['variantData']
                for currKey in sub_key:
                    file.write(currKey['productImageUrl'] + '\n')
            except:
                pass
    file.close()

if __name__ == "__main__":
    url = ""
    max_page = 25
    file_dir = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:m:f:", ["help", "url=", "maxPage=", "fileDir"])
    except getopt.GetoptError:
        print('get_image_singlePage_urls.py -u <url of the web page> -m <max number of the search result page> -f '
              '<directory of the out put file>')
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('get_image_singlePage_urls.py -u <url of the web page> -m <max number of the search result page> -f '
                  '<directory of the out put file>')
            sys.exit()
        elif opt in ("-u", "--url"):
            url = arg
        elif opt in ("-m", "--maxPage"):
            max_page = int(arg)
        elif opt in ("-f", "--fileDir"):
            file_dir = arg
    main(url, max_page, file_dir)