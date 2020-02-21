#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()
'''
list_of_lines = text.split('\n')
for line in range(len(list_of_lines)):
    print 'enter'
    list_of_lines[line] = '*  ' + list_of_lines[line]

text = '\n'.join(list_of_lines)


'''

newtext = ''
line = ''
for sign in text+'\n':
    if sign == '\n':
        print 'enter'
        print '*  ' + line
        newtext = newtext + '*  ' + line + '\n'
        line = ''
    else:
        line = line + sign

print newtext
print ':)'
pyperclip.copy(newtext)
