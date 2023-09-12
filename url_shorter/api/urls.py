from django.urls import path

from .views import ShortenLink, redirect_link


urlpatterns = [
    path('shorten_link/', ShortenLink.as_view(), name='shorten_link'),
    path('<str:short_link>', redirect_link, name='redirect_link'),
]
