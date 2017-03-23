import urllib2
from bs4 import BeautifulSoup
from mock import Mock


class Scrapper:

    # soup = BeautifulSoup(open("guardian.xml"))
    def __init__(self, url):
        page = urllib2.urlopen(url).read()
        self.soup = BeautifulSoup(page, "html.parser")

    def parse_xml(self):
        guardar = []
        for link in self.soup.find_all('item'):
            for title in link.find_all('title'):
                guardar.append(title.string)
        return guardar

    @staticmethod
    def save_to_file(guardar):
        with open("Output.txt", "r+") as text_file:
            for x in guardar:
                text_file.write(x.encode("utf-8"))
                text_file.write('\n')


if __name__ == '__main__':
    url = 'https://www.theguardian.com/international/rss'
    scrapper = Scrapper(url)
    output = scrapper.parse_xml()
    scrapper.save_to_file(output)