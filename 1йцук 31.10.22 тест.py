from bs4 import BeautifulSoup
import requests
import time

url = 'https://habr.com'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'}

response = requests.get(url, headers=HEADERS)
time.sleep(3)
# response.close()

text = response.text
soup = BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all('div', class_="tm-articles-list__item")
    hubs = [hub.text.strip() for hub in hubs]
    date = article.find('time').text
    title = article.find('a', 'tm-article-snippet__title-link')
    span_title = title.text
    for hub in hubs:
        if hub in KEYWORDS:
            href = article.find(class_='tm-article-spinnet__title-link').attrs['href']
            result = f'Название статьи {span_title} ===> Дата статьи {date} ===> {url+href}'
            print(result)



