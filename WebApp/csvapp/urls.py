from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^(\w+)$',views.home),
    url('',views.default),
]