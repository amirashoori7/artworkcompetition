from django.urls import path
from django.contrib.auth import views as auth_views
from account.views_account import ProjectUserList
from . import views_account

app_name = 'account'

urlpatterns = [
    #path('userlogin/', views.userlogin, name='userlogin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('userlist', ProjectUserList.as_view()),
    path('register/', views_account.registration, name='register'),
    path('register_view/', views_account.registration_view, name='register_view'),
]

