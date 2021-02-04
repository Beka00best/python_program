import requests
import json
from bs4 import BeautifulSoup as BS

url = 'https://bai.kz/kursy/'
r = requests.get(url)
html = BS(r.content, 'html.parser')
#items = html.find('td', class_='bank_dir_table')
title = html.select('.bank_dir_table')
#exchange__rates_content
#title = html.select('.currency___columns')

#val = []
#for item in title:
#	val.append({
#		'valuta': item.find('td', class_='bank_dir_td').get_text(),
#		'usd_price': item.find('td').get_text(),
#		})
#print(val)

print(title[0].get_text().replace('наличные',' '))

