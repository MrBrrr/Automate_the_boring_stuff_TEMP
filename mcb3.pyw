#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
"""
Python scripts (files with the extension .py) will be executed by python.exe by default.
This executable opens a terminal, which stays open even if the program uses a GUI.
-----------------------------------------------------------------------------------------
If you do not want this to happen, use the extension .pyw
which will cause the script to be executed by pythonw.exe by default
(both executables are located in the top-level of your Python installation directory).
This suppresses the terminal window on startup.
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
# with shelve.open('mcb') as mcbShelf: #AttributeError: DbfilenameShelf instance has no attribute '__exit__'

try:
    if 'save' == sys.argv[1].lower():
        try:
            clipboardContent = pyperclip.paste()
            mcbShelf[sys.argv[2]] = clipboardContent
        except IndexError:
            print("Pass one more argument to save clipboard content under it's name")
            
    elif 'list' == sys.argv[1].lower():
        for k, v in zip(list(mcbShelf.keys()), list(mcbShelf.values())):
            print(k + ' - ' + v)

    elif 'all' == sys.argv[1].lower():
        putToClipboard = ''
        print('---- keys ----')
        for k, v in zip(list(mcbShelf.keys()), list(mcbShelf.values())):
            print(k)
            putToClipboard = putToClipboard + v + '\n'
        print('---- values ----')
        print()

    elif 'del' == sys.argv[1].lower():
        try:
            if sys.argv[2] in mcbShelf.keys():
                del mcbShelf[sys.argv[2]]
            else:
                print('No list to delete avialable')
        except IndexError:
            print("Pass one more argument to delete it from the multiclipboard shelf")

    elif 'delall' == sys.argv[1].lower():
        for k in list(mcbShelf.keys()):
            del mcbShelf[k]
    
    elif sys.argv[1] in mcbShelf.keys():
        putToClipboard = list(mcbShelf.values())[list(mcbShelf.keys()).index(sys.argv[1])]
        print(putToClipboard)
        pyperclip.copy(putToClipboard)

    else:
        print('No list to copy available')

except IndexError:
    print('Pass some argument')

mcbShelf.close()
