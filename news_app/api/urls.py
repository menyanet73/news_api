from django.urls import include, path
from news.views import NewsViewset
from rest_framework import routers
from users.views import TokenCreateView, UserViewset


router = routers.SimpleRouter()
router.register(r'users', UserViewset, basename='users')
router.register(r'auth', TokenCreateView, basename='auth')
router.register(r'news', NewsViewset, basename='news')


urlpatterns = [
    path('', include(router.urls)),
]
