#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import urllib.request
import sys
import getopt

'''
the script may read the url lists from the directory ./imageUrl .
and download the images to corresponding folders within the directory ./imageDownload . 
'''


def main(image_number, size):
    url_dir = "./imageUrl/"
    image_dir = "./imageDownload/"
    file_names = os.listdir(url_dir)

    for curr_file in file_names:
        with open(os.path.join(url_dir, curr_file), "r") as f:
            curr_list = f.read().split("\n")
            currClass = curr_file.replace(".txt", "", 1)
            download_dir = os.path.join(image_dir, currClass)
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
            for i in range(0, image_number):
                curr_url = curr_list[i].split("?")[0] + "?odnHeight=" + size + "&odnWidth=" + size + "&odnBg=ffffff"
                # print(curr_url)
                curr_file = os.path.join(download_dir, curr_list[i].split("?")[0].split("/")[-1])
                if not os.path.exists(curr_file):
                	try:
                		urllib.request.urlretrieve(curr_url, curr_file)
                	except:
                		print(arg)
                print("downloading image" + str(i) + "for" + currClass)

if __name__ == "__main__":
    n = 10
    size = "180" # try 450 or 180, not all values are valid
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:s:", ["number=", "size="])
    except getopt.GetoptError:
        pass
    for opt, arg in opts:
        if opt in ("-n", "--number"):
            n = int(arg)
        elif opt in ("-s", "--size"):
            size = arg
    main(n, size)



