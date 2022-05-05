from time import sleep

from celery import shared_task

import requests
from bs4 import BeautifulSoup

from main.models import Article


@shared_task
def add_name_and_views(link: str):
    """
    Парсит название и количество просмотров статьи, а затем обновляет запись
    """
    sleep(5)
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        h1 = soup.find('h1')
        span = soup.find_all('span', {'class': 'tm-icon-counter__value'})

        name = h1.text
        views = span[0].text

        article = Article.objects.get(link=link)
        article.name = name
        article.views = views
        article.save()
    else:
        article = Article.objects.get(link=link)
        article.name = 'Страница не найдена'
        article.save()