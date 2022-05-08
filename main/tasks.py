from time import sleep

from celery import shared_task

from main.models import Article
from main.services import (
    parse_article_data,
    create_every_hour_update_views_task
)


@shared_task
def add_name_and_views(link: str):
    """
    Парсит название и количество просмотров статьи, а затем обновляет запись
    """
    article = Article.objects.get(link=link)
    name, views = parse_article_data(link)

    if name != 'Страница не найдена':
        create_every_hour_update_views_task(link)

    article.name = name
    article.views = views

    article.save()

    return None


@shared_task
def update_views(link: str) -> None:
    """
    Обновляет количество просмотро статьи
    """
    article = Article.objects.get(link=link)
    _, views = parse_article_data(link)

    article.views = views

    article.save()

    return None
