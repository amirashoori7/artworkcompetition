from django.shortcuts import render
from django.http import JsonResponse
from artwork.models import Artwork
from .import models
from .import forms

def evalpage(request, id):
    work = get_object_or_404(Artwork, id)
    eval = EvalD1A.objects.filter(work_id=id)
    if not eval.exists():
        form = FormD1A()
    context = {'eval':eval, 'work':work}
    return render(request, 'evalstat.html', context)

def create_evald1a(request, id):
    work = get_object_or_404(Artwork, id=id)
    form = FormD1A(request.POST or None)
    if form.is_valid():
        form.save()
    eval = EvalD1A.objects.filter(work_id=id)
    context = {'eval':eval, 'work':work}
    return render(request, 'evalstat.html', context)

'''
def create_evald1b(request, id):
    work = get_object_or_404(Artwork, id=id)
    if request.POST.get('action') == 'post':
        #form = FormD1-B(request.POST or None)

def create_evald1c(request, id):
    work = get_object_or_404(Artwork, id=id)
    if request.POST.get('action') == 'post':
        #form = FormD1-B(request.POST or None)

def create_evald2(request, id):
    work = get_object_or_404(Artwork, id=id)
    if request.POST.get('action') == 'post':
        #form = FormD1-B(request.POST or None)
'''
