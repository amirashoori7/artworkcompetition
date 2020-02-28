from .forms_account import UserRegistrationForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView
from account.forms_account import AdvancedUserRegistrationForm
from account.models_account import ProjectUser
from datetime import date
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail, send_mass_mail

class CustomPasswordChangeView(PasswordChangeView):
    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed.')
        return super().form_valid(form)


def projectUserList(request):
    userList = ProjectUser.objects.exclude(user_type=1)
    context = {'userlist': userList}
    return render(request, 'adminPages/user_list.html', context)


def login_form(request):
    response_data = {}
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
        except:
            response_data['errorResult'] = "Invalid username or password"
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    return render(request, 'login.html')

def forgot_psw(request):
    response_data = {}
    if request.method == 'POST':
        username = request.POST['username']
        cellno = request.POST['cellno']
        try:
            userObj = ProjectUser.objects.get(username=username, cellphone=cellno)
        except:
            userObj = None
        if userObj is None:
            response_data['errorResult'] = "The email address does not match the cell phone number"
        else:
            response_data['successResult'] = "The new password is sent to your email address"
    return HttpResponse(json.dumps(response_data),
        content_type="application/json")

def registration(request):
    response_data = {}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form = form.save()
            response_data['successResult'] = 'Registration succeed'
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username = username, password=password)
            login(request, user)
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            subject = "MathArt Portal - Registration Successful"
            message = "Dear {0} {1}, you have successfully registered in MathArt competition.\n\n Please go on and finish your artwork submission".format(fname, lname)
            mailmsg1 = (subject, message, 'mathart.co.za@gmail.com', [username])
            send_mail(subject, message, 'mathart.co.za@gmail.com', [username])
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResults'] = form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def registerJudge(request):
    response_data = {}
    if request.method == 'POST':
        form = AdvancedUserRegistrationForm(request.POST)
        if int(request.POST.get("id", 0)) > 0:
#                 school = get_object_or_404(School, id=request.POST["school"])
#                 artwork_form.school = school
#                 artwork_form.school_id = int(request.POST["school"])
            old_data = get_object_or_404(ProjectUser, id=request.POST["id"])
            form = AdvancedUserRegistrationForm(request.POST, request.FILES, instance=old_data)

        if form.is_valid():
            form = form.save()
#             CREATE OR UPDATE
            response_data['successResult'] = 'Registration succeed'
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResults'] = form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif request.method == 'GET' and 'username' in request.GET and request.GET['username'] is not None and request.GET['username'] != '':
        try:
            user_model = get_object_or_404(ProjectUser, username=request.GET["username"])
            form = AdvancedUserRegistrationForm(instance=user_model)
        except:
            form, user_obj = ProjectUser.objects.get_or_create(username=request.user)
    else:
        form = AdvancedUserRegistrationForm()
    context = {'form': form}
    return render(request, 'adminPages/registerJudge.html', context)


def registration_view(request):
    form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'adminPages/register_view.html', context)
