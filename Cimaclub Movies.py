from bs4 import BeautifulSoup
from requests import get
from re import compile

from os import path
'''
This Script takes the text file with movie links and returns direct download links
'''

# Replace {Path} with Movies file Path
in_file = r"Path"

dct = path.dirname(path.abspath(__file__))


out_file = f"{dct}" + "\MLinks.txt"


links = []
with open(in_file)as file:
    for line in file:
        if len(line) > 1:
            req = get(line)
            soup = BeautifulSoup(req.text, "lxml")
            print("Done")
            page = soup.find('a', attrs={'href': compile(".*download=.*govid.*")}).get('href')

            req = get(page)
            soup = BeautifulSoup(req.text, "lxml")
            # Quality Change -->(5)<--   [6 for 720]  [5 for 480]  [4 for 360]
            page = soup.find('a', attrs={'onclick': compile(".*( 5.* ).*")}).get('href')
            links.append(page)
with open(out_file, "a") as f:
    for i in links:
        f.write(i)
