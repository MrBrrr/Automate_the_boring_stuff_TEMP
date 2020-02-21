#! python

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # from command line
    url_address = "+".join(sys.argv[1:])
else:
    # from clipboard
    url_address = "+".join(pyperclip.paste().split(" "))

url = "".join(["https://www.google.com/maps/place/", url_address])
webbrowser.open(url)
