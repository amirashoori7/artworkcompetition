from django.urls import path
from django.contrib.auth import views as auth_views
from . import views_account

app_name = 'account'

urlpatterns = [
    #path('userlogin/', views.userlogin, name='userlogin'),
#     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', views_account.login_form, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('change_password/',
          views_account.CustomPasswordChangeView.as_view(
            template_name='change_password.html', success_url="/"), name='change_password'),
    path('userlist/', views_account.projectUserList, name='userlist'),
    path('register/', views_account.registration, name='register'),
    path('register_judge/', views_account.registerJudge, name='registerJudge'),
    path('register_view/', views_account.registration_view, name='register_view'),
#     path('register_judge/<int:id>/', views_account.registerJudge),
]
