import json
from time import sleep

from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule


from main.models import Article
from main.services import parse_article_data


# TODO синхронизировать таски

@shared_task
def add_name_and_views(link: str):
    """
    Парсит название и количество просмотров статьи, а затем обновляет запись
    """
    sleep(5)
    article = Article.objects.get(link=link)
    name, views = parse_article_data(link)

    if name != 'Страница не найдена':
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

    article.name = name
    article.views = views

    article.save()

    return None


@shared_task
def update_views(link: str) -> None:
    """
    Обновляет количество просмотро статьи
    """
    sleep(5)
    article = Article.objects.get(link=link)
    _, views = parse_article_data(link)

    article.views = views

    article.save()
