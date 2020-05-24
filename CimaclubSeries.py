from bs4 import BeautifulSoup
import requests
import re
from os import path

'''
This Script takes the first watch link and returns all season download links
'''


dct = path.dirname(path.abspath(__file__))


out_file = f"{dct}" + "\Links.txt"


def next_epo(link):
    if link:
        page = link.get('href')
        req = requests.get(page)
        soup = BeautifulSoup(req.text, "lxml")
        page = soup.find('a', attrs={'href': re.compile(".*download=.*govid.*")}).get('href')
        mid_links.append(page)
        print('....')
        nxt = soup.find('a', attrs={'class': 'NextEpisode'})
        next_epo(nxt)


def last_links(mid):
    x = 0
    for i in mid:
        req = requests.get(i).text
        soup = BeautifulSoup(req, "lxml")
        # Quality Change -->(5)<--   [6 for 720]  [5 for 480]  [4 for 360]
        page = soup.find('a', attrs={'onclick': re.compile(".*( 5.* ).*")}).get('href')
        x += 1
        print(f'Ep {x}')
        ep.append(page)


ep = []
mid_links = []
first_link = input("Enter First Ep watch link: ")
first_req = requests.get(first_link)
first_soup = BeautifulSoup(first_req.text, "lxml")
first_page = first_soup.find('a', attrs={'href': re.compile(".*download=.*govid.*")}).get('href')
mid_links.append(first_page)

first_nxt = first_soup.find('a', attrs={'class': 'NextEpisode'})
next_epo(first_nxt)
last_links(mid_links)

print(ep)
