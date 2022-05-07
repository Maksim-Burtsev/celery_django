from django.db import models


class Article(models.Model):
    """
    Статья
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    views = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(unique=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name if self.name else self.link
