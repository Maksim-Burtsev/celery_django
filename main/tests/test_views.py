from django.test import TestCase, override_settings
from django.urls import reverse

from main.models import Article
from main.serializers import ArticleGetSerializer


class MainViewTestCase(TestCase):

    def test_get_article(self):

        article = Article.objects.create(
            link='https://habr.com/ru/post/655921/'
        )

        response = self.client.get(reverse('get_article', args=(1,)))
        self.assertEqual(response.status_code, 200)

        serializer = ArticleGetSerializer(article)
        self.assertEqual(response.data, serializer.data)

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def test_create_article(self):

        response = self.client.post(reverse('create_article'), {
                                    'link': 'https://habr.com/ru/post/655921/'})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data, {'link': 'https://habr.com/ru/post/655921/'})

        article = Article.objects.get(pk=1)
        self.assertEqual(
            article.name, 'Три вещи, которые сделают тебя продуктивнее')

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def test_create_invalid_article(self):

        wrong_link = 'https://habr.com/ru/post/6559211234567/'

        response = self.client.post(
            reverse('create_article'), {'link': wrong_link}
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {'link': wrong_link})

        article = Article.objects.get(pk=1)
        self.assertEqual(article.name, 'Страница не найдена')

    def test_create_exists_article(self):
        
        Article.objects.create(link='https://habr.com/ru/post/655921/')

        response = self.client.post(reverse('create_article'), {
                                    'link': 'https://habr.com/ru/post/655921/'})

        self.assertEqual(response.status_code, 400)
