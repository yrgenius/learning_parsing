from bs4 import BeautifulSoup
import requests

URL = 'https://auto.ria.com/newauto/marka-volkswagen/'
HEADER = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
HOST = 'https://auto.ria.com'

def get_response(url, params=None):
    r = requests.get(url, headers=HEADER, params=params)
    print('Получили объект - \t\t\t\t', type(r))
    return r


def parse(resp):
    # html = get_response(URL)
    print('Получили объект - \t\t\t\t', type(resp))
    if resp.status_code == 200:
        print("Мы получили ответ с сайта:\t\t %s" % URL)
        get_content(resp.text)
    else:
        print('Сайт не ответил')


def get_content(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    print('Получили объект - \t\t\t\t', type(soup))
    items = soup.find_all('a', class_="na-card-item na-card-item--list")
    print('Получили список значений по ключу объекта - ', type(items))
    cars = []
    for i in items:
        # Проверка на наличие значений цены
        usd_p = i.find('strong', class_='green')
        rub_p = i.find('span', class_='size15')
        if usd_p:
            usd_p = usd_p.get_text()
        else:
            usd_p = "Цена не указана"
        if rub_p:
            rub_p = rub_p.get_text().replace('•', '').replace('грн', 'rub').strip()
        else:
            rub_p = "Цена не указана"
        cars.append({
            'title': i.find('div', class_='na-card-name').get_text(strip=True),
            'link': HOST + i.find('span', class_='link').get('href'),
            'usd_price': usd_p,
            'rub_price': rub_p,
            'town': i.find('svg', class_='svg svg_i16_pin').find_next('span').text,
        })
    print('Получили список из словарей - {0} длинной - {1}'.format(type(cars),  len(cars)))
    return cars


parse(get_response(URL, HEADER))
