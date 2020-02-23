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

def registration(request):
    response_data = {}
    if request.method == 'POST':
        if date.today() < date(2020,3,3) and request.POST.get('req','') != "dev":
            response_data['successResult'] = 'The registration opens Tuesday 3rd of March, 2020.'
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form = form.save()
            response_data['successResult'] = 'Registration succeed'
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
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
