from rest_framework import generics

from main.serializers import ArticleSerializer
from main.models import Article


class ArticleCreateAPIView(generics.CreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
