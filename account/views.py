from django.views.generic import ListView
from .models import ProjectUser
from .forms import UserRegistrationForm
from django.shortcuts import render
from django.http import HttpResponse
import json

class ProjectUserList(ListView):
    model = ProjectUser

def registration(request):
    form = UserRegistrationForm(request.POST)
    response_data = {}
    if request.method == 'POST':
        if form.is_valid():
            form = form.save()
            response_data['successResult'] = 'Congratulations. You have submitted your artwork successfully!'
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


def getUser(request):
    form = UserRegistrationForm(request.GET)
    if form.is_valid():
        user = form.save()
        return render(request, 'register.html', {'user': user})
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)
