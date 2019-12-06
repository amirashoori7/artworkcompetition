from django.urls import path, re_path
from . import views

app_name = 'artwork'

urlpatterns = [
    #re_path(r'^index/$', views.index, name='index'),
    path('', views.index, name='index'),
    path('entry_form/', views.entry_form, name='entry_form'),
    path('work_lists/', views.work_lists, name='work_lists'),
    path('<school>/', views.work_lists,
          name='work_lists_by_school'),
    path('<int:id>/<surname>/', views.work_detail,
          name='work_detail'),
]
