from rest_framework import generics

from main.serializers import ArticleCreateSerializer, ArticleGetSerializer
from main.models import Article


class ArticleCreateAPIView(generics.CreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer


class ArticleRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleGetSerializer

