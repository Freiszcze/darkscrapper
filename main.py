import requests
import yaml
from bs4 import BeautifulSoup

page_number = 1
links = {}

while True:
    print(page_number)
    r = requests.get("http://hikarinoakariost.info/page/" + str(page_number))
    payload = r.text
    soup = BeautifulSoup(payload, 'html.parser')

    titles = soup.find_all("h3", class_="entry-title")
    if not titles:
        break

    for link in titles:
        a = link.a
        title = a.get('title')
        if " OP" in title or " ED" in title:
            links[title] = a.get('href')
    page_number += 1

stream = open('OPy&EDy.yaml', 'w')
yaml.dump(links, stream)
print(links)

