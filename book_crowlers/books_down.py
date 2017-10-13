import requests
from lxml import html
link = 'http://kitaptar.bashkort.org/catalog/'
alph = ['Ә', 'ә', 'Ө', 'ө', 'Ү', 'ү', 'Ҡ', 'ҡ', 'Ғ', 'ғ', 'Ҙ', 'ҙ', 'Ҫ', 'ҫ', 'Һ', 'һ', 'Ң', 'ң']
all_links = []
for num in range(1, 81):
    print('скачиваю страницу ', num)
    page = requests.get('http://kitaptar.bashkort.org/catalog/' + str(num))
    tree = html.fromstring(page.content)
    books = tree.xpath('//div[@id="books"]/a')
    for book in books:
        auth = book.xpath('.//div[@clas'
                          's="bookinfo"]//text()')
        b_desc = ''.join(auth)
        for i in alph:
            if i in b_desc:
                all_links.append(book.attrib['href'])
                break

with open('booklinks.txt', 'w', encoding='utf-8') as booklinks:
    print('заношу в документ')
    for i in all_links:
        booklinks.write(i + '\r')

print ('end')