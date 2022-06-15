from django.contrib import admin

from users import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'redaction')

class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'created')

admin.site.register(models.User, UserAdmin)
admin.site.register(models.AuthToken, AuthTokenAdmin)
