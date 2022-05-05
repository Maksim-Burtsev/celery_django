from rest_framework import generics

from main.serializers import ArticleCreateSerializer, ArticleGetSerializer
from main.models import Article
from main.tasks import sleepy


class ArticleCreateAPIView(generics.CreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer


class ArticleRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleGetSerializer

    def get(self, request, *args, **kwargs):
        sleepy.delay(100)
        # sleepy(100)
        return super().get(request, *args, **kwargs)

