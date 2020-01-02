'''
A view method acts as the C(ontroller) in an MVC Framework
Charged with handling incoming requests, applying business logic
and then routing requests with an appropriate response.
'''

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Artwork, School
from .forms import EntryForm
from django.http import HttpResponse
from django.http.response import JsonResponse
import json
from django.core import serializers


def index(request):
    context = {}
    return render(request, 'index.html', context)


def home(request):
    num_works = Artwork.objects.all().count()
    num_schools = School.objects.all().count()
    context = {
        'num_works': num_works,
        'num_schools': num_schools}
    return render(request, 'home.html', context)


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)


def work_lists(request):
    works = Artwork.objects.all()
    context = {'works': works}
    return render(request, 'work_lists.html', context)
 

def work_details(request, id):
    work = get_object_or_404(Artwork, id=id)
    context = {'work': work}
    return render(request, 'work_details.html', context)


def signup_page(request):   
    context = {}
    return render(request, 'signup_page.html', context)


def entry_form(request):
    schools = School.objects.all()
    if request.method == 'POST':
        response_data = {}
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            response_data['successResult'] = 'The entry form submission is successful!'
            response_data['id'] = form.id
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResult'] = form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    else:
        form = EntryForm()
        context = {'form': form, 'schools': schools}
        return render(request, 'entry_form.html', context)
