from django.urls import path, re_path
from . import views

app_name = 'evaluation'

urlpatterns = [
    # re_path(r'^index/$', views.index, name='index'),
    path('formd1a/', views.create_d1a, name='formd1a'),
]
