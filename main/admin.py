from django.contrib import admin

from main.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'last_update', 'views')
