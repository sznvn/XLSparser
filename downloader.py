import wget
import requests
#import urllib.request
from bs4 import BeautifulSoup

URL = 'https://www.muiv.ru/studentu/fakultety-i-kafedry/fakultet-it/raspisaniya/'
page = requests.get(URL).text
soup = BeautifulSoup(page, "html.parser").find_all('p', 'm-doc__name')
docs = []
names = []
i = 0
# asoup = soup.find_all('p', 'm-doc__name')

for a in soup:
    names.append(a)
    url = 'https://www.muiv.ru' + a.find('a').get('href')
    if(url.endswith('xls')):
        docs.append(url)

print(docs)

#wget.download('https://pythonworld.ru/m/img/python-3.png', 'C:/Users/sznvn/PycharmProjects/XLSparser/files/cat.png')
for doc in docs:
    i += 1
    print(doc)
    wget.download(doc, 'C:/Users/sznvn/PycharmProjects/XLSparser/files/' + str(i) + '.xls')

#urllib.request.urlretrieve('https://pythonworld.ru/m/img/python-3.png', 'C:/Users/sznvn/PycharmProjects/XLSparser/files/cat.png')


#govno peredelat'
#for doc in docs:
#    name = doc.split('/')[6]
#    print(name)
#    dir = '/output' + name[0]
#    file = open(dir, 'w')
#    file.write(requests.get(doc).text)
#print(page)