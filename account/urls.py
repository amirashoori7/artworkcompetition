from django.urls import path
from django.contrib.auth import views as auth_views
from . import views_account
from django.urls.conf import include

app_name = 'account'

urlpatterns = [
    path('login/', views_account.login_form, name='login'),
    path('forgotpsw/', views_account.forgot_psw, name='forgotpsw'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('change_password/',
          views_account.CustomPasswordChangeView.as_view(
            template_name='change_password.html', success_url="/"), name='change_password'),
    path('reset_password_confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(
            template_name='reset_password_confirm.html', success_url="/?message=The%20password%20is%20successfully%20changed&T=false"), name='reset_password_confirm'),
    path('reset_password/',
          auth_views.PasswordResetView.as_view(
            template_name='reset_password.html',
            email_template_name='reset_password_email.html', success_url="/?message=A%20confirmation%20email%20is%20sent%20to%20your%20email%20address&T=false"), name='reset_password'),
    path('userlist/', views_account.projectUserList, name='userlist'),
    path('register/', views_account.registration, name='register'),
    path('register_judge/', views_account.registerJudge, name='registerJudge'),
]
