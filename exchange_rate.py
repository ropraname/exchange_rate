import requests as re
from bs4 import BeautifulSoup

def get_best_exchange_rate(currency_code, num_branches):
	url = 'https://www.banki.ru/products/currency/cash/{}/sankt-peterburg/#sort=sale&order=asc'.format(currency_code)
	content = re.get(url)
	soup = BeautifulSoup(content.text, "html.parser")

	all_values = soup.find_all('div', class_="table-flex__row item calculator-hover-icon__container")
	data = []
	
	for value in range(len(all_values)):
		name = str(all_values[value].find("a", class_='font-size-default color-gray-gray').text)
		name_ard = str(all_values[value].find("a", class_='font-bold').text)
		if value == 0:

			price = str(all_values[value].find_all('div')[6]["data-currencies-rate-sell"])

		else:
			divs = all_values[value].find_all('div')
			for tags in divs:
				try:
					price = str(tags["data-currencies-rate-sell"])
					if len(price) > 3:
						price = price[:5]
				except:
					continue
		container = (name, name_ard, price)
		data.append(container)
		
	return data[:num_branches]


