#!python

""" Cos nie dziala z tymi CSS-selectors-ami """

import requests, sys, bs4, webbrowser

if len(sys.argv) > 1:
    keywords = "+".join(sys.arv[1:])
    print(" ".join(["You are searching for:", keywords]))
else:
    print("Pass the keywords you are searching for:")
    keywords = "+".join(input().split(" "))

url = "".join(["https://www.ecosia.org/search?q=", keywords])

""" Opening the web page content """
res = requests.get(url)
#webbrowser.open(url)
try:
    res.raise_for_status()
except Exception as exc:
    print("Something went wrong: %s" % exc)
    exit()

""" Downloading the web page"""
EcosiaFile = open("ecosia_searching_results.html", "wb")
for chunk in res.iter_content(100000):
    EcosiaFile.write(chunk)
EcosiaFile.close()
# do close it and then open to read

""" Searching for some more URLs to open them"""
EcosiaFile = open("ecosia_searching_results.html", "r")
EcosiaBS = bs4.BeautifulSoup(EcosiaFile.read())
list_of_EcosiaTags = EcosiaBS.select('meta')
print(len(list_of_EcosiaTags))

for TagObject in list_of_EcosiaTags[0:5]:
    print(str(TagObject))
    print(TagObject.getText() + ":)")
    # webbrowser.open(TagObject.getText())
