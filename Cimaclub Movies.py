from bs4 import BeautifulSoup
import requests
import re

in_file = r"C:\Users\Ahmed Mostafa\Desktop\CimaClub\movies.txt"
out_file = r"C:\Users\Ahmed Mostafa\Desktop\CimaClub\MLinks.txt"
links = []
with open(in_file)as file:
    for line in file:
        if len(line) > 1:
            req = requests.get(line)
            soup = BeautifulSoup(req.text, "lxml")
            page = soup.find('a', attrs={'href': re.compile(".*download=.*govid.*")}).get('href')

            req = requests.get(page).text
            soup = BeautifulSoup(req, "lxml")
            # Quality Change -->(5)<--   [6 for 720]  [5 for 480]  [4 for 360]
            page = soup.find('a', attrs={'onclick': re.compile(".*( 5.* ).*")}).get('href')
            links.append(page)
with open(out_file, "a") as f:
    for i in links:
        f.write(i)

# req = requests.get(input("Enter Url: "))
# soup = BeautifulSoup(req.text, "lxml")
# pages = soup.find('a', attrs={'href': re.compile(".*download=.*govid.*")}).get('href')
#
# req = requests.get(pages).text
# soup = BeautifulSoup(req,"lxml")
# # Quality Change -->(5)<--   [6 for 720]  [5 for 480]  [4 for 360]
# pages = soup.find('a',attrs={'onclick': re.compile(".*( 5.* ).*")}).get('href')
# print(pages)
