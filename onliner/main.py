from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import lxml
import random
import csv
import datetime

user = UserAgent().random
headers = {'user-agent': user}

product_titles = []
cur_data = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

with open(f'baraholka.onliner_{cur_data}.csv', 'w') as file:
    writer = csv.writer(file)

    writer.writerow(
        (
            'название',
            'цена',
            'ссылка'
        )
    )
url = f'https://baraholka.onliner.by/search.php?q=%D1%81%D0%BC%D0%B0%D1%80%D1%82+%D1%87%D0%B0%D1%81%D1%8B&start=0'
# print(url)
r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
pages = soup.find_all(class_='pages-fastnav')[-1].text
pages = int(pages[-1]) * 25
# print(str)
# pages = (0, pages, 25)
# print(pages)

for i in range(0, pages , 25):
    url = f'https://baraholka.onliner.by/search.php?q=%D1%81%D0%BC%D0%B0%D1%80%D1%82+%D1%87%D0%B0%D1%81%D1%8B&start={i}'
    # print(url)
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    data_products = soup.find('div', class_='ba-tbl-list').find_all('tr')

    for product in data_products:


        try:
            product_title = product.find('h2', class_='wraptxt').find('a').text.strip()

        except:
            product_title = 'нет названия'

        # product_titles.append(product_title)

        try:
            price =product.find('td', class_='cost').find('div', class_='price-primary').text.strip()
            # print(price)
        except:
            price = 'нет цены'

        try:
            url = 'https://baraholka.onliner.by' + product.find('h2', class_='wraptxt').find('a').get('href')

        except:
            img_url = 'нет картинки'

        product_titles.append(
            {
                'product_title': product_title,
                'price': price,
                'url': url
            }
        )


product_titles1 = product_titles[5::3]
# test = product_titles1[2]

# print(test)
# print(product_titles[2::3])
for keys in product_titles1:
    product = keys['product_title']
    price = keys['price']
    url = keys['url']

    with open(f'baraholka.onliner_{cur_data}.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                product,
                price,
                url
            )
        )

    # for key in keys:
    # print(keys, product_titles1.values("product_title"))
        # product = key.get(product_title)
        # print(product)



    # print(product_title)
        # print(url)



# print(product_titles1)
# print(product_titles[1])
