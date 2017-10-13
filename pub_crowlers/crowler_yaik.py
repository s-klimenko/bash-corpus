
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

numb = 988

def get_article(art, link):
    global numb
    try:
        url = link
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        try:
            for br in soup.find_all("br"):
                br.replace_with("\n")
            soup = soup.find('div', {'id':'news'})
            text = soup.find('div', {'class': 'n_text'}).get_text().strip('\r\n').strip('\t')
            lenght = len(text.split())
            if lenght > 5:
                numb = numb + 1
                a = Article(lenght)
                a.newspaper = 'Яйык'
                a.title = soup.find('h1').get_text().strip('\r\n')
                a.date = soup.find('small').get_text().strip('\r\n')
                a.path = 'D://yaik/yaik{}.txt'.format(str(numb))
                art.append(a)
                with open('./yaik/yaik{}.txt'.format(str(numb)), 'w', encoding='utf-8') as f:
                    f.write(text)
        except AttributeError:
            pass
    except requests.exceptions.ConnectionError:
        print('Ошибка :(')

def get_links(page):
    art = []
    url = 'http://yaikrb.ru/lastnews/page/{}/'.format(page)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    all_articles = soup.find('div', {'id': 'dle-content'})
    articles = all_articles.find_all('a', {'class':'greatbtn'})
    for i in articles:
        get_article(link=i['href'], art=art)
    return art

def get_all():
    f = pd.DataFrame(columns=['Газета', 'Автор', 'Название', 'Дата', 'Путь', 'Длина'])
    rows_list = []        # get input row in dictionary format
    for page in range(100,144):
        print('обрабатываю страницу {}'.format(page))
        for i in get_links(page):
            dict1 = {'Газета':i.newspaper, 'Автор':i.author, 'Название':i.title, 'Дата':i.date, 'Путь':i.path, 'Длина':i.lenght}#  key = col_name
            rows_list.append(dict1)
    df = pd.DataFrame(rows_list)
    df.to_excel('meta_yaik3.xlsx')
