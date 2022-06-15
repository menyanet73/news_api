from django.contrib import admin

from news import models


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created')

admin.site.register(models.News, NewsAdmin)
