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


def main(total_number, size):
    url_dir = "./imageUrl/"
    image_dir = "./imageDownload/"
    file_names = os.listdir(url_dir)

    for curr_file in file_names:
        with open(os.path.join(url_dir, curr_file), "r") as f:
            curr_list = f.read().split("\n")
            currClass = curr_file.replace(".txt", "", 1)
            download_dir = os.path.join(image_dir, currClass)

            image_number = 0
            if os.path.exists(download_dir):
            	image_number = len(os.listdir(download_dir))
            	print(str(image_number) + " images have already been downloaded.")
            else:
                os.makedirs(download_dir)            

            i = 0
            while image_number < total_number and i < len(curr_list):
                curr_url = curr_list[i].split("?")[0] + "?odnHeight=" + size + "&odnWidth=" + size + "&odnBg=ffffff"
                # print(curr_url)
                curr_file = os.path.join(download_dir, curr_list[i].split("?")[0].split("/")[-1])
                if os.path.exists(curr_file):
                	print("processing record " + str(i) + ": a duplicate image -- " + curr_file)              	
                else:
                	try:
                		urllib.request.urlretrieve(curr_url, curr_file)
                		image_number += 1
                		print("processing record " + str(i) + ": download image" + str(image_number) + " for " + currClass)
                	except:
                		print(arg)
                i += 1

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



