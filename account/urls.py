from django.urls import path
from django.contrib.auth import views as auth_views
from . import views_account

app_name = 'account'

urlpatterns = [
    path('login/', views_account.login_form, name='login'),
    path('forgotpsw/', views_account.forgot_psw, name='forgotpsw'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('change_password/',
          views_account.CustomPasswordChangeView.as_view(
            template_name='change_password.html', success_url="/"), name='change_password'),
    path('userlist/', views_account.projectUserList, name='userlist'),
    path('register/', views_account.registration, name='register'),
    path('register_judge/', views_account.registerJudge, name='registerJudge'),
]
