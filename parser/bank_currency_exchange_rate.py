import requests
import json
from bs4 import BeautifulSoup as BS

url = 'https://prodengi.kz/currency/'
r = requests.get(url)
html = BS(r.content, 'html.parser')

items1 = html.find_all('li', class_='odd EUR Евро')
items2 = html.find_all('li', class_='odd USD Доллар США')
items3 = html.find_all('li', class_='odd RUB Российский рубль')

eur = []
for item in items1:
	eur.append({
		'valuta': item.find('div', class_='short_name befor').get_text(),
		'price':  item.find('div', class_='price_buy befor').get_text(),
		})
eur = eur[0]

usd = []
for item in items2:
	usd.append({
		'valuta': item.find('div', class_='short_name befor').get_text(),
		'price':  item.find('div', class_='price_buy befor').get_text(),
		})
usd = usd[0]

rub = []
for item in items3:
	rub.append({
		'valuta': item.find('div', class_='short_name befor').get_text(),
		'price':  item.find('div', class_='price_buy befor').get_text(),
		})
rub = rub[0]

myObj = {
	"rub":"rub[0]",
	"eur":{'valuta':'valuta', 'price':'price'},
	"usd":{'valuta':'valuta', 'price':'price'},
}
x = rub['valuta'] + ' = ' + rub['price']
print(x)












