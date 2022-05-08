from django.test import TestCase, override_settings

from django_celery_beat.models import PeriodicTask

from main.tasks import add_name_and_views, update_views
from main.models import Article


class TaskTestCase(TestCase):

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def test_add_name_and_views(self):
        link = 'https://habr.com/ru/post/655921/'
        article = Article.objects.create(link=link)

        result = add_name_and_views.delay(link)
        article.refresh_from_db()

        self.assertTrue(result.successful())
        self.assertIsNone(result.get())
        self.assertTrue(PeriodicTask.objects.filter(name=link).exists())
        self.assertEqual(
            article.name, 'Три вещи, которые сделают тебя продуктивнее')

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def test_add_name_and_views_wrong(self):
        link = 'https://habr.com/ru/post/655921324/'
        article = Article.objects.create(link=link)

        result = add_name_and_views.delay(link)
        article.refresh_from_db()

        self.assertTrue(result.successful())
        self.assertIsNone(result.get())
        self.assertFalse(PeriodicTask.objects.filter(name=link).exists())
        self.assertEqual(article.name, 'Страница не найдена')


    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def test_update_views(self):
        link = 'https://habr.com/ru/post/655921/'
        article = Article.objects.create(link=link)
        result = update_views.delay(link)

        self.assertTrue(result.successful())
        self.assertIsNone(result.get())

        self.assertIsNone(article.views)
        article.refresh_from_db()
        self.assertIsNotNone(article.views)
