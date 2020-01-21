# https: // coinmarketcap.com / all / views / all /
import requests
from bs4 import BeautifulSoup


def get_html(url):
    """Получаем текст со страницы с url"""
    r = requests.get(url)       # response получаем все со страницы
    return r             # возвращаем только текст <class 'str'>


def get_all_links(html):
    """ищем ссылки в коде html"""
    all_text = BeautifulSoup(html.content, 'html.parser')
    # rows = all_text.find('div', class_='cmc-table__table-wrapper-outer')
    # rows = all_text.find("table", id="currencies-all").find_all('td', class_="currency-name").text()

    # rows = all_text.find_all('td', attrs={'class': "currency-name"})
    rows = all_text.find_all("tr", class_="cmc-table-row") # список объектов супа
    print(type(rows))
    links = []                                                  # список ссылок
    for r in rows:
        a = r.find('a').get('href')    # берем строку, ищем тег "a" и берем ссылку "href"
        links.append(a)
    return links


def print_links(links):
    for i in links:
        print(i)


def main():
    url = "https://coinmarketcap.com/all/view/all/"
    all_html_like_string = get_html(url)
    all_links = get_all_links(all_html_like_string)
    print_links(all_links)


if __name__ == "__main__":
    main()