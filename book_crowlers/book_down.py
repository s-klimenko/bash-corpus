import urllib
import pandas as pd
import requests
from lxml import html
import urllib.parse
from datetime import datetime
from xml import etree
from xml.etree.ElementTree import tostring

class Book():
    def __init__(self):
        self.link = []
        self.auth = ''
        self.title = ''
        self.file_desc = ''
        self.path = []





extentions = ['.txt', '.docx', '.doc', '.fb2', '.epub', '.djvu']
b = open("booklinks.txt", 'r', encoding='utf-8')
links = b.readlines()
b.close()
n = 500
m = 10
chunks = [links[x:x+50] for x in range(500, len(links), 50)]
for links in chunks:
    m += 1
    print('Скачиваю группу ' + str(m) + '...')
    print('Время:' + str(datetime.now()))
    all_links = []
    all_books = []
    for link in links:
        n += 1
        print(n, link)
        page = requests.get(link.strip())
        tree = html.fromstring(page.content)
        books = tree.xpath('//div[@class="book container"]')
        for book in books:
            d_links = []
            links = book.xpath('//div[@class="downloads"]/a')
            for link in links:
                for i in extentions:
                    if link.attrib['href'].endswith(i):
                        d_links.append(link.attrib['href'])
                    if d_links != []:
                        break
            if d_links != []:
                b = Book()
                paths = []
                b.title = book.xpath('//div[@class="bookinfo large"]/h1[@class="booktitle"]/text()')
                b.auth = book.xpath('//div[@class="bookinfo large"]/p[@class="author"]/text()')
                b.file_desc = book.xpath('//div[@class="bookinfo large"]/p[@class="description"]/text()')
                b.link = d_links
                testfile = urllib.request.URLopener()
                for d_link in d_links:
                    nam = d_link.split('/')[-1]
                    path = nam
                    paths.append(path)
                    print('Скачиваю файл...\r')
                    try:
                        testfile.retrieve(urllib.parse.quote(d_link, safe='/:'), path)
                    except urllib.error.HTTPError:
                        paths = 'СКАЧАЙ ВРУЧНУЮ!'
                    except OSError:
                        testfile.retrieve(urllib.parse.quote(d_link, safe='/:'), str(n))
                b.path = paths
                all_books.append(b)
    print('Создаю документ...\r')
    f = pd.DataFrame(columns=['Автор', 'Название', 'Описание', 'Путь', 'Ссылка'])
    rows_list = []
    for i in all_books:
        dict1 = {'Автор':' ,'.join(i.auth), 'Название':' ,'.join(i.title), 'Описание':' ,'.join(i.file_desc), 'Путь':' ,'.join(i.path), 'Ссылка':' ,'.join(i.link)}
        # get input row in dictionary format
        #  key = col_name
        rows_list.append(dict1)
    df = pd.DataFrame(rows_list)
    df.to_excel(str(m) + '_books.xlsx')

