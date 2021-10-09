import os
import wget
import requests
from bs4 import BeautifulSoup

os.system("./clean.sh")

docs = []
faculties = ['fakultet-it/raspisaniya/',
             'fakultet-upravleniya/raspisaniya-zanyatiy-fakulteta-upravlekniya.php',
             'fakultet-ekonomiki-i-finansov/raspisaniya-zanyatiy-fakulteta-ekonomiki-i-finansov.php',
             'yuridicheskiy-fakultet/raspisaniya-zanyatiy-yuridicheskogo-fakulteta.php']

for faculty in faculties:
    url = 'https://www.muiv.ru/studentu/fakultety-i-kafedry/' + faculty
    page = requests.get(url).text
    tags = BeautifulSoup(page, "html.parser").find_all('p', 'm-doc__name')
    for tag in tags:
        gateway = 'https://www.muiv.ru' + tag.find('a').get('href')
        if gateway.endswith('xls'):
            docs.append(gateway)

i = 0
for doc in docs:
    i += 1
    wget.download(doc, './files/' + str(i) + '.xls')
