from bs4 import BeautifulSoup as BS
import requests as req

req = req.get('https://www.mk.ru/anekdoti/')
soup = BS(req.text, 'lxml')

for item in soup.find_all('p', {'text'}):
    print(item.text+'\n')