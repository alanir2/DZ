import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

def get_crypto_data():
    driver = webdriver.Chrome()
    driver.get('https://coinmarketcap.com/all/views/all/')
    driver.maximize_window()
    px = 0
    for i in range(10):
        px += 1000
        driver.execute_script(f'window.scrollTo(0, {px})')
        sleep(0.1)

    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, 'html.parser')
    all_coins = soup.find_all(class_="cmc-table__column-name--name cmc-link")
    all_market_cap = soup.find_all(class_="sc-11478e5d-1 hwOFkt")

    total_value = sum([int(value.text.replace('$', '').replace(',', '')) for value in all_market_cap])
    current_time = datetime.now().strftime('%H.%M %d.%m.%Y')

    count = 1  # Счетчик для отслеживания количества выведенных значений

    with open(f'data2/{current_time}.csv', 'a', newline='', encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerow(['№', 'Name', 'Market Cap', 'Percentage'])

        for name, value in zip(all_coins, all_market_cap):
            if count == 101:  # Ограничение на вывод только первых 100 значений
                break

            name_coin = name.text
            market_cap = value.text
            num = int(value.text.replace('$', '').replace(',', ''))
            num = float(num / total_value * 100)
            percent = str(round(num, 2)) + '%'
            writer.writerow([count, name_coin, market_cap, percent])
            count += 1

crypto_data = get_crypto_data()
