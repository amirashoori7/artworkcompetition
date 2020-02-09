from django.urls import path
from . import rest_views
from artwork import views_artwork

app_name = 'artwork'

urlpatterns = [
    # re_path(r'^index/$', views.index, name='index'),
    path('rest_list', rest_views.worklists),
    path('get_school', rest_views.get_school),
    path('', views_artwork.index, name='index'),
    path('entry_form/', views_artwork.entry_form, name='entry_form'),
    path('entry_form_view/', views_artwork.entry_form_view, name='entry_form_view'),
    path('aboutus/', views_artwork.aboutus, name='aboutus'),
    path('contactus/', views_artwork.contactus, name='contactus'),
    path('faq/', views_artwork.faq, name='faq'),
    path('history/', views_artwork.history, name='history'),
    path('howtoenter/', views_artwork.howtoenter, name='howtoenter'),
    path('rules/', views_artwork.rules, name='rules'),
    path('signup_page/', views_artwork.signup_page, name='signup_page'),
    path('signup_page_view/', views_artwork.signup_page_view, name='signup_page_view'),
    path('home/', views_artwork.home, name='home'),
    path('gallery/', views_artwork.gallery, name='gallery'),
    path('work_lists/', views_artwork.work_lists, name='work_lists'),
    path('work_detail_update/', views_artwork.work_detail_update, name='work_detail_update'),
    path('<int:id>/', views_artwork.work_details, name='work_details'),
]
