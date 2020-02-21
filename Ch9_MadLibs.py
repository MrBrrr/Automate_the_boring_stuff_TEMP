#! python
# Program that reads in text files and lets the user add their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB,or VERB appears in the text file.

import re, os

sentence = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

for char_ind in range(len(sentence)):

    for sth in ['NOUN','ADJECTIVE','VERB']:
        index = sentence.find(sth,char_ind,char_ind+len(sth))
        if index != -1 :
            print ' Enter an ' + sth.lower() +':'
            word = str(input())
            sentence = sentence[:index] + word + sentence[char_ind+len(sth):]

print sentence

with open('NewText.txt','w') as newFile:
    newFile.write(sentence)
    





