from rest_framework import generics

from main.serializers import ArticleCreateSerializer, ArticleGetSerializer
from main.models import Article
from main.tasks import add_name_and_views


class ArticleCreateAPIView(generics.CreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

    def perform_create(self, serializer):
        serializer.save()
        link = serializer.validated_data.get('link')
        add_name_and_views.delay(link)


class ArticleRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleGetSerializer
