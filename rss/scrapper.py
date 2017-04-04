import os
import urllib2
from bs4 import BeautifulSoup


class Scrapper:

    def __init__(self, url):
        self.url = url
        self.list_of_titles = []
        self.xml = self.get_rss()

    def parse_xml(self):
        soup = BeautifulSoup(self.xml,'html.parser')
        for link in soup.find_all('item'):
            for title in link.find_all('title'):
                self.list_of_titles.append(title.string.strip().encode("utf-8"))

    def save_to_file(self, output_file):
        with open(output_file, "w+") as text_file:
            for x in self.list_of_titles:
                text_file.write(x)
                text_file.write('\n')

    def get_rss(self):
        return urllib2.urlopen(self.url).read()

if __name__ == '__main__':
    url = 'https://www.theguardian.com/international/rss'
    print 'Scrapping ' + url
    scrapper = Scrapper(url)
    print 'Parsing XML'
    scrapper.parse_xml()
    print 'Generating output: result.txt'
    scrapper.save_to_file("result.txt")