#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt

def main(argv):
   inputfile = 'xxx'
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   print(opts)
   print(args)
   for opt, arg in opts:
      if opt == '-h':
         print('wahaaa')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('input message:', inputfile)
   print('output message:', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])