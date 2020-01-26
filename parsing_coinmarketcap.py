# https: // coinmarketcap.com / all / views / all /
import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://coinmarketcap.com/all/view/all/'
HEADER = {":authority": "coinmarketcap.com", ":method": "GET", ":path": "/all/views/all/", ":scheme": "https",
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
          "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
          "cache-control": "max-age=0",
          "cookie": "__cfduid=d596618d431c58ccc852274b7b8bb54d51579579218; gtm_session_first=%222020-01-21T09%3A59%3A51.797Z%22; _ga=GA1.2.1792912806.1579600793; _fbp=fb.1.1579600793616.542646902; __gads=ID=e4134f40ff95c52d:T=1579579221:S=ALNI_MZ_TXjPNooazq1fCSNCKB2LHkddVA; _gid=GA1.2.733181555.1580024194; cmc_gdpr_hide=1; gtm_session_last=%222020-01-26T12%3A51%3A34.071Z%22; _gat=1",
          "sec-fetch-mode": "navigate",
          "sec-fetch-site": "same-origin",
          "sec-fetch-user": "?1",
          "upgrade-insecure-requests": "1"}


def get_response(url, params=None):
    """Получаем ответ со страницы с url"""
    r = requests.get(url, HEADER)       # response получаем все со страницы

    if r.status_code == 200:
        print("Получен ответ с сайта: ", url)
    else:
        print("НЕТ ОТВЕТА с сайта: \t\t", url)
        print("КОД ошибки:         \t\t", r.status_code)
    print('Получили объект - \t\t\t', type(r))
    # print(r.text)
    return r


def parse_text(resp):
    """Ищем в тексте ссылки"""
    links = []
    soup = BeautifulSoup(resp.text, 'html.parser')
    print('Получили объект - \t\t\t', type(soup))
    items = soup.find_all('tr', class_="cmc-table-row")
    print(len(items))



def get_all_links(html):
    """ищем ссылки в коде html"""
    links = []                  # список ссылок
    all_text = BeautifulSoup(html.content, 'html.parser')
    # rows = all_text.find('div', class_='cmc-table__table-wrapper-outer')
    # rows = all_text.find("table", id="currencies-all").find_all('td', class_="currency-name").text()
    # rows = all_text.find_all('td', attrs={'class': "currency-name"})
    rows = all_text.find_all("tr", class_="cmc-table-row")   # список объектов супа

    for r in rows:
        a = r.find('a').get('href').text    # берем строку, ищем тег "a" и берем ссылку "href"
        print(a)
        links.append(a)
    return links


def get_data_html(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        data = soup.find('a', class_='cmc_link').text.split()
    except:
        data = 'Данныые не найдены'

    return data


def write_csv(data):
    with open('coin_out.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        print(data)


def print_links(links):
    for i in links:
        print(i)


def main():
    # all_html_like_string = get_html(url)
    # all_links = get_all_links(all_html_like_string)
    # print_links(all_links)

    resp = get_response(URL)
    parse_text(resp)


if __name__ == "__main__":
    main()