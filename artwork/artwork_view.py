from django.shortcuts import render, get_object_or_404
from artwork.artwork_models import Artwork, School, convert_to_df
from django.http import HttpResponse
import json
from artwork.artwork_forms import EntryForm, UserForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from account.models_account import ProjectUser
from _datetime import date
import csv
import os
from _io import StringIO
from django.core.files.base import File
from django.http.response import StreamingHttpResponse


def index(request):
    context = {}
    return render(request, 'index.html', context)


def managerConsole(request):
    context = {}
    return render(request, 'adminPages/admin_console.html', context)


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
    works = Artwork.objects.filter(status__gte=0).exclude(status=1)
    context = {'works': works}
    return render(request, 'adminPages/work_lists.html', context)

 
def getfile(request):  
    artworks = Artwork.objects.filter(status__gte=0)
    fields = ['owner__username', 'owner__first_name', 'owner__last_name', 'owner__cellphone', 'owner__dob', 'owner__parentname', 'owner__parentemail', 'owner__parentphone', 'learnergrade']
    df = convert_to_df(artworks, fields=fields)
    filename = os.path.dirname(os.path.abspath(__file__)) + '\\artworks.csv'
    df.to_csv(filename)
    with open(filename, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
    return response


def work_details(request, id):
    if request.method == 'POST':
        Artwork.objects.filter(id=id).update(status='updated_name')
    work = get_object_or_404(Artwork, id=id)
    context = {'work': work}
    return render(request, 'adminPages/work_details.html', context)


def work_detail_update(request):
    response_data = {}
    if request.method == 'POST':
        workapproved = request.POST.get('workapproved', '') == 'False'
        bioapproved = request.POST.get('bioapproved', '') == 'False'
        qapproved = request.POST.get('qapproved', '') == 'False'
        comment = request.POST.get('comment', '')
        Artwork.objects.filter(id=request.POST['id']).update(status=request.POST['status'], workapproved=workapproved,
                                                     bioapproved=bioapproved, qapproved=qapproved, comment=comment)
        response_data['successResult'] = 'Successful.'
    return HttpResponse(json.dumps(response_data),
                content_type="application/json")

    
def signup_page(request):   
    context = {}
    return render(request, 'signup_page.html', context)


# @login_required
# @transaction.atomic
def entry_form(request):
    response_data = {}
    if request.user.is_anonymous:
        userModel = None
    else:
        userModel = ProjectUser.objects.get(username=request.user)
        user_form = UserForm(instance=request.user)
    if request.method == 'POST':
        old_data = get_object_or_404(Artwork, id=request.POST["id"])
        artwork_form = EntryForm(request.POST, request.FILES, instance=old_data)
        if artwork_form.is_valid():
            artwork_form = artwork_form.save(commit=False)
            artwork_form.owner = request.user
            if request.POST.get('status', '-1') != '-1':
                artwork_form.status = request.POST.get("status")
            if int(request.POST.get("school", 0)) > 0:
                school = get_object_or_404(School, id=request.POST["school"])
                artwork_form.school = school
                artwork_form.school_id = int(request.POST["school"])
            artwork_form.save()
            response_data['successResult'] = 'Saved successfully!'
            response_data['id'] = artwork_form.id
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResults'] = artwork_form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif userModel is not None and userModel.user_type == 1:
        try:
            artwork_model = get_object_or_404(Artwork, owner=request.user)
            artwork_form = EntryForm(instance=artwork_model)
        except:
            artwork_form, artwork_obj = Artwork.objects.get_or_create(owner=request.user)
    else:
        artwork_form = EntryForm()
        user_form = UserForm()
    context = {'form': artwork_form, 'user_form': user_form}
    return render(request, 'entry_form.html', context)
    

class Echo:

    def write(self, value):
        return value
