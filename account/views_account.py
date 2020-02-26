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
from django.core.mail import send_mail, send_mass_mail

class CustomPasswordChangeView(PasswordChangeView):
    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed.')
        return super().form_valid(form)


def projectUserList(request):
    userList = ProjectUser.objects.all()
    context = {'userlist': userList}
    return render(request, 'adminPages/user_list.html', context)


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
            email1 = form.cleaned_data['username']
            email2 = form.cleaned_data['parentemail']
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            subject = "Mathart Registeration Successful"
            message = "Dear {0} {1}, you have successfully registered in mathartcompetition.\n\nPlease go on and finish your artwork submission".format(fname, lname)
            send_mass_mail(subject, message, 'admin@mathart.co.za', [email1, email2])
            response_data['successResult'] = 'Registration succeed'
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResult'] = form.errors.as_json(True)
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
        if form.is_valid():
            form = form.save()
#             CREATE OR UPDATE
            response_data['successResult'] = 'Registration succeed'
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResult'] = form.errors.as_json(True)
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
