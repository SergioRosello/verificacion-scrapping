import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("guardian.xml"))

#page = urllib2.urlopen('https://www.theguardian.com/international/rss').read()
#soup = BeautifulSoup(page)

guardar = []

for link in soup.find_all('item'):
    for title in link.find_all('title'):
        print(title.string)
        guardar.append(title.string)

with open("Output.txt", "r+") as text_file:
    for x in guardar:
        text_file.write(x.encode("utf-8"))
        text_file.write('\n')


