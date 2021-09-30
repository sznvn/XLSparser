#import wget
import requests
from bs4 import BeautifulSoup

URL = 'https://www.muiv.ru/studentu/fakultety-i-kafedry/fakultet-it/raspisaniya/'
page = requests.get(URL).text
soup = BeautifulSoup(page, "html.parser").find_all('p', 'm-doc__name')
docs = []
i = 0
# asoup = soup.find_all('p', 'm-doc__name')

for a in soup:
    docs.append('https://www.muiv.ru' + a.find('a').get('href'))


#govno peredelat'
#for doc in docs:
#    name = doc.split('/')[6]
#    print(name)
#    dir = '/output' + name[0]
#    file = open(dir, 'w')
#    file.write(requests.get(doc).text)
#print(page)