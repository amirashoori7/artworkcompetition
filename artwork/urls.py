from django.urls import path
from . import rest_views
from artwork import artwork_view

app_name = 'artwork'

urlpatterns = [
    # re_path(r'^index/$', views.index, name='index'),
    path('rest_list', rest_views.worklists),
    path('get_school', rest_views.get_school),
    path('', artwork_view.index, name='index'),
    path('entry_form/', artwork_view.entry_form, name='entry_form'),
    path('aboutus/', artwork_view.aboutus, name='aboutus'),
    path('contactus/', artwork_view.contactus, name='contactus'),
    path('faq/', artwork_view.faq, name='faq'),
    path('history/', artwork_view.history, name='history'),
    path('manager_console/', artwork_view.managerConsole, name='manager_console'),
    path('howtoenter/', artwork_view.howtoenter, name='howtoenter'),
    path('rules/', artwork_view.rules, name='rules'),
    path('signup_page/', artwork_view.signup_page, name='signup_page'),
    path('home/', artwork_view.home, name='home'),
    path('gallery/', artwork_view.gallery, name='gallery'),
    path('work_lists/', artwork_view.work_lists, name='work_lists'),
    path('work_detail_update/', artwork_view.work_detail_update, name='work_detail_update'),
    path('<int:id>/', artwork_view.work_details, name='work_details'),
]
