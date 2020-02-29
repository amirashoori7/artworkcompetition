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
    path('reset_password/',
          auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html', 
            from_email = 'mathart.co.za@gmail.com',
            subject_template_name='registration/password_reset_subject.txt', 
            email_template_name='registration/password_reset_email.html', 
            success_url="registration/password_reset_done.html"), name='reset_password'),
    path('reset_password_confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/reset_password_confirm.html'), name='reset_password_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
         name='password_reset_done'),
    path('/', include('django.contrib.auth.urls')),
    path('userlist/', views_account.projectUserList, name='userlist'),
    path('register/', views_account.registration, name='register'),
    path('register_judge/', views_account.registerJudge, name='registerJudge'),
]
