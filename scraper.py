import requests
import string
import os
from bs4 import BeautifulSoup
# os.mkdir('Folder')
# number_page = 1
# article_key = 'News'
number_page = int(input())
article_key = input()
url = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020'

for num in range(1,number_page+1):
    folder_name = 'Page_' + str(num)
    os.mkdir(folder_name)
    soup = BeautifulSoup(requests.get(url, params={'page':num}).content, 'html.parser')
    article_news = []

    for li in soup.find_all('li',{'class':'app-article-list-row__item'}):
        if li.find('span',{'class':'c-meta__type'}).text == article_key:
            article_news.append('https://www.nature.com'+str(li.find('a',{'data-track-action':'view article'})['href']))

    for article in article_news:
        soup_article = BeautifulSoup(requests.get(article).content, 'html.parser')
        title = soup_article.find('h1', {'class':'c-article-magazine-title'})

        with open(f'{folder_name}/'+'_'.join(title.text.strip(string.punctuation).split())+'.txt', 'w', encoding='utf-8') as f:
            f.write(soup_article.find('div', {'class': 'c-article-body'}).text.strip())
print('Saved all articles.')