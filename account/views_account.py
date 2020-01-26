from django.views.generic import ListView
from .models_account import ProjectUser
from .forms_account import UserRegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.contrib.auth import authenticate, login

class ProjectUserList(ListView):
    model = ProjectUser

def registration(request):
    response_data = {}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form = form.save()
            response_data['successResult'] = 'Registration succeed'
#             username = form.username
#             password = form.password
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home')
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


# def getUser(request):
#     form = UserRegistrationForm(request.GET)
#     if form.is_valid():
#         user = form.save()
#         return render(request, 'register.html', {'user': user})
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'register.html', context)
