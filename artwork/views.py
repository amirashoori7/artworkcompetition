'''
A view method acts as the C(ontroller) in an MVC Framework
Charged with handling incoming requests, applying business logic
and then routing requests with an appropriate response.
'''

from django.shortcuts import render, get_object_or_404
from .models import Artwork, School
from .forms import EntryForm
from django.http import HttpResponse

def index(request):
    num_works = Artwork.objects.all().count()
    num_schools = School.objects.all().count()
    context = {
        'num_works': num_works,
        'num_schools': num_schools,
    }
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)


def work_lists(request):
    works = Artwork.objects.all()
    context = {'works': works}
    return render(request,
                  'work_lists.html', context)
    '''
    school = None
    schools = School.objects.all()
    works = Artwork.objects.all()
    if school:
        school = get_object_or_404(School)
        works = works.filter(school=school)
    return render(request,
                  'works/list.html',
                   {'school':school,
                    'schools':schools,
                    'works':works})
    '''

def work_detail(request, id, surname):
    work = get_object_or_404(Artwork, id=id, surname=surname)
    return render('works/work_detail.html', {'work': work})

def entry_form(request):
    schools = School.objects.all()
    form = EntryForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form, 'schools': schools}
    return render(request, 'entry_form.html', context)