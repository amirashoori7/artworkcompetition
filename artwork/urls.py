from django.urls import path, re_path
from . import views
from . import rest_views

app_name = 'artwork'

urlpatterns = [
    #re_path(r'^index/$', views.index, name='index'),
    path('rest_list', rest_views.worklists),
    path('', views.index, name='index'),
    path('entry_form/', views.entry_form, name='entry_form'),
    path('home/', views.home, name='home'),
    path('work_lists/', views.work_lists, name='work_lists'),
    path('<school>/', views.work_lists,
          name='work_lists_by_school'),
    path('<int:id>/<surname>/', views.work_detail,
          name='work_detail'),
]
