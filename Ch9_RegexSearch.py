#! python
# {rogram that opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression.
# The results should be printed to the screen.

import re, os, pprint

cwdList = os.listdir(os.getcwd())

txtReg = re.compile(r'.*\.txt')
txtList = txtReg.findall('\n'.join(cwdList))
#print txtList

print "User's regular expression:"
userReg = re.compile(str(input()))
dictionary = {}

for txtFile in txtList:
    f = open(txtFile,'r')
    file_content = f.read()
    userRegList = userReg.findall(file_content)
    dictionary[txtFile] = userRegList

for item in dictionary.items():
    pprint.pprint (item)
