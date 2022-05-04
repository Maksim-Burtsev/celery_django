from django.urls import path

from main.views import ArticleCreateAPIView


urlpatterns = [
    path('add/', ArticleCreateAPIView.as_view(), name='create_article'),
]
