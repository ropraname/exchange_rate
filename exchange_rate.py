import requests as re
from bs4 import BeautifulSoup

def get_best_exchange_rate(currency_code, num_branches):
	url = 'https://www.banki.ru/products/currency/cash/{}/sankt-peterburg/#sort=sale&order=asc'.format(currency_code)
	content = re.get(url)
	content = content.text
	soup = BeautifulSoup(content, 'html.parser')
	#prettify()
	all_bank_values = soup.find_all("div", class_='exchange-calculator-rates table-flex__row-group ')
	data = []
	for banks in all_bank_values:
		name = str(banks.find("a", class_='font-size-default color-gray-gray').text)
		name_ard = str(banks.find("a", class_='font-bold').text)
		value = banks.find("div", class_='table-flex__cell table-flex__rate font-size-large color-pumpkin-orange  text-nowrap')
		value = str(value['data-currencies-rate-sell'])
		container = (name, name_ard, value)
		data.append(container)
		
	print(data[:num_branches])
