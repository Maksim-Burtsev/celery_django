from rest_framework import serializers

from main.models import Article


class ArticleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('link',)


class ArticleGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('name', 'link', 'views')

