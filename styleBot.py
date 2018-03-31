#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3




#Get filename from command line input
import sys
myFile = sys.argv[1]
print("styleBot is checking ", myFile)

# open file and initiate line counter
data =  open(myFile, 'r', encoding = None, errors = 'ignore')
paragraphCount = 0
lineCount = 0

# Check each line against checklist of potential errors
for line in data:
    myLines = line.split(".")
    paragraphCount = paragraphCount + 1
    lineCount = 0
    for sentence in myLines:
        lineCount = lineCount + 1
        if isinstance(line, str) == True:
           if 'aint' in sentence:
              print("Par",paragraphCount,", Sen",lineCount, ": Warning! Aint is an improper usage. Try 'am not' or 'are not' or something else.")
           if '--' in sentence:
              print("Par",paragraphCount,", Sen",lineCount, ": Warning! Two consecutive hyphens. Try replacing with an em-dash. You can use alt+0151 on the PC or Command + hyphen on the Mac.")
           if ' -- ' in sentence:
              print("Par",paragraphCount,", Sen",lineCount, ": Warning! Two consecutive hyphens. Try replacing with an em-dash. You can use alt+0151 on the PC or Command + hyphen on the Mac.")

           else:
              continue
        else:
           print("not string data")
# Indicate the end of the process in the command line
print("Review completed.")
