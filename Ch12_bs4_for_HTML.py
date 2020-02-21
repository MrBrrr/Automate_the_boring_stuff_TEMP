import bs4
import requests
"""
res = requests.get('http://nostarch.com')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text)
# passing the file object to change it to BeautifulSoup Object

print(str(type(noStarchSoup)))
"""
exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)
