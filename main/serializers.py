from rest_framework import serializers

from main.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('link',)
