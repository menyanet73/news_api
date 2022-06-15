from django.db import models


class News(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    text = models.TextField()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self) -> str:
        return self.title
