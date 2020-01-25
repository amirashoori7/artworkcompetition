from django.urls import path
from . import views_evaluation

app_name = 'evaluation'

urlpatterns = [
    # re_path(r'^index/$', views.index, name='index'),
    path('formd1a/', views_evaluation.create_d1a, name='formd1a'),
]
