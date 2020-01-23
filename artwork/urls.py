from django.urls import path, re_path
from . import views
from . import rest_views

app_name = 'artwork'

urlpatterns = [
    # re_path(r'^index/$', views.index, name='index'),
    path('rest_list', rest_views.worklists),
    path('', views.index, name='index'),
    path('entry_form/', views.entry_form, name='entry_form'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('faq/', views.faq, name='faq'),
    path('history/', views.history, name='history'),
    path('howtoenter/', views.howtoenter, name='howtoenter'),
    path('rules/', views.rules, name='rules'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('home/', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('work_lists/', views.work_lists, name='work_lists'),
    path('work_detail_update/', views.work_detail_update, name='work_detail_update'),
    path('<int:id>/', views.work_details, name='work_details'),
    path('<school>/', views.work_lists,
          name='work_lists_by_school'),
]
