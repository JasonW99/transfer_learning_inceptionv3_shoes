#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import requests
from bs4 import BeautifulSoup
import json

'''
the script may record the image urls from walmart search result pages.
the results will be saved into the directory ./imageUrl .
'''

files = ["Women's Boots", "Women's Sandals", "Women's Dress Shoes", "Women's Casual Shoes", "Women's Athletic Shoes",
         "Women's Slippers", "Men's Athletic Shoes", "Men's Boots", "Men's Casual Shoes", "Men's Sandals",
         "Men's Slippers", "Men's Dress Shoes"]
pages = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
urls = ["https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228542",
        "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228547",
        "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228546",
        "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228545",
        "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228540",
        "https://www.walmart.com/browse/shoes/women-s-shoes/5438_1045804_1045806?cat_id=5438_1045804_1045806_1228543",
        "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228548",
        "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228549",
        "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228552",
        "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228554",
        "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228550",
        "https://www.walmart.com/browse/shoes/men-s-shoes/5438_1045804_1045807?cat_id=5438_1045804_1045807_1228553"]


def single_page_url_download(url, max_page, file_dir):
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


def main():
    n = len(files)
    for i in range(0, n):
        curr_file = "./imageUrl/" + files[i] + ".txt"
        curr_page = pages[i]
        curr_url = urls[i]
        if not os.path.exists(os.path.dirname(curr_file)):
            os.mkdir(os.path.dirname(curr_file))
        single_page_url_download(curr_url, curr_page, curr_file)

if __name__ == "__main__":
    main()









