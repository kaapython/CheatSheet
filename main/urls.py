from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path
from django.conf import settings

from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.index, name='index'),
    path('category', views.category, name='category'),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )