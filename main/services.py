import json

import requests
from bs4 import BeautifulSoup

from django_celery_beat.models import PeriodicTask, IntervalSchedule


def parse_article_data(link: str) -> tuple[str, str]:
    """
    Парсит название и количество просмотров статьи
    """
    
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        h1 = soup.find('h1')
        span = soup.find_all('span', {'class': 'tm-icon-counter__value'})

        name = h1.text
        views = span[0].text

    else:
        name = 'Страница не найдена'
        views = '-'

    return name, views


def create_every_hour_update_views_task(link: str) -> None:
    """
    Создаёт периодическую задачау update_views с интервалом 1 час
    """

    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.HOURS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name=link,
        task='main.tasks.update_views',
        args=json.dumps([link, ])
    )
