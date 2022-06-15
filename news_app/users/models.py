import binascii
import os

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    redaction = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.username


class AuthToken(models.Model):
    token = models.CharField(max_length=40, primary_key=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='auth_token')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Токен авторизации'
        verbose_name_plural = 'Токены авторизации'
        
    def __str__(self):
        return self.user


    def save(self, *args, **kwargs):
        if not self.token:
            self.token = binascii.hexlify(os.urandom(20)).decode()
        return super().save(*args, **kwargs)
