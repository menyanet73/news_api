from django.db import models


class News(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title
