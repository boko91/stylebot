#!/usr/bin/python3
#This script finds style errors and sends feedback to the command line

import sys


myFile = sys.argv[1]

data =  open(myFile, 'r', encoding = None, errors = 'ignore')
myPage = "<!doctype html> "
#myPage = []
lineCount = 0

#cut lines containing unwanted text string
for line in data:
     lineCount = lineCount + 1
     if isinstance(line, str) == True:
        if 'aint' in line:
            print("line ", lineCount, ": Warning: Aint is an improper usage. Try 'am not' or 'are not' or something else.")
        if ' -- ' in line:
            print("line ", lineCount, ": Warning: Two consecutive hyphens. Try replacing with an em-dash. You can use alt+0151 on the PC or Command + hyphen on the Mac.")
        else:
           continue
     else:
        print("not string")




print("Review completed.")
