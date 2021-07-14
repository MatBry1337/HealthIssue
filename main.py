import requests
import re

from bs4 import BeautifulSoup

link = input()
links = []

r = requests.get(link)

soup = BeautifulSoup(r.content, "html.parser")

tag1 = soup.find_all('a', href=re.compile('topics'))
tag2 = soup.find_all('a', href=re.compile('entity'))

for i in tag1:
    if len(i.text) > 1:
        if i.text.lower().startswith('l'):
            links.append(i.text)

for i in tag2:
    if len(i.text) > 1:
        if i.text.lower().startswith('l'):
            links.append(i.text)

print(links)
