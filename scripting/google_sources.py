"""
semi-automation of google search for information
"""

import webbrowser as wb
from time import sleep
from bs4 import BeautifulSoup
import requests


foods = [
    'egg',
    'avocado',
    'spinach',
    'peanut',
    'cheese',
    'brocoli',
    'chicken',
    'mayonnaise',
    'salmon',
    'tuna',
    'tomato',
    'onion',
    'lemon',
    'chorizo',
    'pickle',
    'meat',
    'pork',
    'lettuce'
]

stats = ['carbs', 'proteins', 'fat', 'calories']

url = 'https://www.google.com/search?q={}+in+{}&ie=utf-8&oe=utf-8'

with open('food.csv', 'w') as storage:
    for f in foods:
        storage.write('{}\n'.format(f))

sleep(5)

for f in foods:
    for s in stats:
        wb.open_new_tab(url.format(s, f))
        # TODO: try with requests - BeautifulSoup
        # response = requests.get(url.format(s, f))
        # soup = BeautifulSoup(response, 'html.parser')
        # answer = soup.find_all('div', '_XWk an_fna')
        # print(answer)
        # print('{} contains {} of {}'.format(f, answer, s))
        sleep(12)
