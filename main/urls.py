from django.urls import path

from main.views import ArticleCreateAPIView, ArticleRetrieveAPIView


urlpatterns = [
    path('add/', ArticleCreateAPIView.as_view(), name='create_article'),
    path('get/<int:pk>/', ArticleRetrieveAPIView.as_view(), name='get_article'),
]
