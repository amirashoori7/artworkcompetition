'''
A view method acts as the C(ontroller) in an MVC Framework
Charged with handling incoming requests, applying business logic
and then routing requests with an appropriate response.
'''

from django.shortcuts import render, get_object_or_404
from .models_artwork import Artwork, School
from django.http import HttpResponse
import json
from artwork.forms_artwork import EntryForm, UserForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from account.models import ProjectUser


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


def aboutus(request):
    context = {}
    return render(request, 'aboutus.html', context)


def contactus(request):
    context = {}
    return render(request, 'contactus.html', context)


def faq(request):
    context = {}
    return render(request, 'faq.html', context)


def history(request):
    context = {}
    return render(request, 'history.html', context)


def howtoenter(request):
    context = {}
    return render(request, 'howtoenter.html', context)


def rules(request):
    context = {}
    return render(request, 'rules.html', context)


def gallery(request):
    context = {}
    return render(request, 'gallery.html', context)


def work_lists(request):
    works = Artwork.objects.all()
    context = {'works': works}
    return render(request, 'work_lists.html', context)
 

def work_details(request, id):
    if request.method == 'POST':
        Artwork.objects.filter(id=id).update(status='updated_name')
    work = get_object_or_404(Artwork, id=id)
    context = {'work': work}
    return render(request, 'work_details.html', context)


def work_detail_update(request):
    response_data = {}
    if request.method == 'POST':
        workapproved = request.POST.get('workapproved', '') == 'False'
        bioapproved = request.POST.get('bioapproved', '') == 'False'
        qapproved = request.POST.get('qapproved', '') == 'False'
        Artwork.objects.filter(id=request.POST['id']).update(status=request.POST['status'], workapproved=workapproved, 
                                                     bioapproved=bioapproved, qapproved=qapproved)
        response_data['successResult'] = 'Congratulations. You have submitted your artwork successfully!'
        
    return HttpResponse(json.dumps(response_data),
                content_type="application/json")

    
def signup_page(request):   
    context = {}
    return render(request, 'signup_page.html', context)

@login_required
@transaction.atomic
def entry_form(request):
    schools = School.objects.all()
    userModel = ProjectUser.objects.get(username=request.user)
    user_form = UserForm(instance=request.user)
    if request.method == 'POST':
        response_data = {}
        artwork_form = EntryForm(request.POST, request.FILES)
        if artwork_form.is_valid():
            artwork_form = artwork_form.save(commit=False)
            artwork_form.owner = request.user
            artwork_form.save()
            response_data['successResult'] = 'Congratulations. You have submitted your artwork successfully!'
            response_data['id'] = artwork_form.id
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResultWork'] = artwork_form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif userModel.user_type == 1:
        artwork_model = Artwork.objects.get(owner=request.user)
        artwork_form = EntryForm(instance=artwork_model)
    else:
        artwork_form = EntryForm()
    context = {'form': artwork_form, 'schools': schools, 'user_form': user_form}
    return render(request, 'entry_form.html', context)
    