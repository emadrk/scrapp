import requests
from bs4 import BeautifulSoup
import re

def make_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup
# put urls in a list
def get_xml_urls(soup):
    urls = [loc.string for loc in soup.find_all('loc')]
    return urls
if __name__ == '__main__':
    file1 = open('brainly10.txt', 'r')
    file2 = open("brainly_cleaned.txt","a")
    Lines = file1.readlines()
    for line in Lines:
        xml = f"{line}"
        soup = make_soup(xml)
        urls = get_xml_urls(soup)
        # loop through the urls
        for url in urls:
            file2.write(url)
            file2.write("\n")
            print(url)
    file1.close()   
    file2.close()       