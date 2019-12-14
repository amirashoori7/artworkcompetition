from django.shortcuts import render
from django.http import JsonResponse
from artwork.models import Artwork
from . import models

def create_evald1a(request, id):
    work = get_object_or_404(Artwork, id=id)
    if request.POST.get('action') == 'post':
        #form = FormD1-A(request.POST or None)

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
