
import requests
from bs4 import BeautifulSoup
import pandas as pd

class Article:

    def __init__(self, lenght, newspaper='-', title='-', date='-', author='-', path = '-'):
        self.newspaper = newspaper
        self.title = title
        self.date = date
        self.author = author
        self.lenght = lenght
        self.path = path

numb = 1464

def get_article(art, link):
    global numb
    try:
        url = 'http://kulturarb.ru{}'.format(link)
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        try:
            text = soup.find('div', {'class': 'item-text'}).get_text().strip('\r\n').strip('\t')
            lenght = len(text.split())
            if lenght > 5:
                numb = numb + 1
                a = Article(lenght)
                a.newspaper = 'Башҡортостандың мәҙәни донъяһы'
                a.title = soup.find('h1', {'class': 'item-title'}).get_text().strip('\r\n')
                a.date = soup.find('div', {'class': 'data'}).get_text().split(', ')[1].strip('\r\n')
                a.path = 'D://oldkulturarb/oldkulturarb{}.txt'.format(str(numb))
                art.append(a)
                with open('./oldkulturarb/oldkulturarb{}.txt'.format(str(numb)), 'w', encoding='utf-8') as f:
                    f.write(text)
        except AttributeError:
            pass
    except requests.exceptions.ConnectionError:
        print('Ошибка :(')

def get_links(page):
    art = []
    url = 'http://kulturarb.ru/ba/news/arkhiv-novostej/{}'.format(page)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    all_articles = soup.find('div', {'class': 'items items-col-1 uk-article-divider'})
    articles = all_articles.find_all('a', {'class':None})
    for i in articles:
        get_article(link=i['href'], art=art)
    return art

def get_all():
    f = pd.DataFrame(columns=['Газета', 'Автор', 'Название', 'Дата', 'Путь', 'Длина'])
    rows_list = []        # get input row in dictionary format
    for page in range(100, 150):
        print('обрабатываю страницу {}'.format(page))
        for i in get_links(page):
            dict1 = {'Газета':i.newspaper, 'Автор':i.author, 'Название':i.title, 'Дата':i.date, 'Путь':i.path, 'Длина':i.lenght}#  key = col_name
            rows_list.append(dict1)
    df = pd.DataFrame(rows_list)
    df.to_excel('meta5.xlsx')

get_all()