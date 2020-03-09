from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
import json
from artwork.artwork_models import Artwork
from django.contrib.auth.decorators import login_required
from account.models_account import ProjectUser
from evaluation.models import D1A, D2, D1B, D3
from evaluation.forms_evaluation import FormD1A, FormD2, FormD1B, FormD3
import artwork
from rest_framework import status
from artwork.artwork_forms import EntryForm


@login_required
def create_d1a(request):
    if request.method == 'POST':
        response_data = {}
        if request.POST['work_id'] is None or request.POST['work_id'] == '':
            response_data['errorResult'] = "Illegal access to the form, the work id is null."
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        artwork = get_object_or_404(Artwork, id=int(request.POST['work_id']))
        old_data = get_object_or_404(D1A, id=request.POST["id"])
        formd1A_form = FormD1A(request.POST, instance=old_data)
        if formd1A_form.is_valid():
            d1as = D1A.objects.filter(artwork=artwork)
            judges = ProjectUser.objects.filter(user_type=2)
            if len(d1as) == len(judges):
                update_worklist(int(request.POST['work_id']), 5)
            formd1A_form = formd1A_form.save(commit=False)
            formd1A_form.author = request.user
            formd1A_form.artwork = artwork
            formd1A_form = formd1A_form.save()
            response_data['successResult'] = 'D1A form submitted successfully!'
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResults'] = formd1A_form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif request.method == 'GET':
        artwork = get_object_or_404(Artwork, id=int(request.GET['work_id']))
        try:
            formd1A_model = get_object_or_404(D1A, author=request.user, artwork=artwork)
            formd1A_form = FormD1A(instance=formd1A_model)
        except:
            formd1A_form, formd1A_obj = D1A.objects.get_or_create(author=request.user, artwork=artwork)
        context = {'form': formd1A_form}
        return render(request, 'evaluationForms/D1A_form.html', context)
    else:
        response_data['errorResult'] = "Illegal access to the form"
        return HttpResponse(json.dumps(response_data),
            content_type="application/json")

@login_required
def create_d1b(request):
    if request.method == 'POST':
        response_data = {}
        if request.POST['work_id'] is None or request.POST['work_id'] == '':
            response_data['errorResult'] = "Illegal access to the form, the work id is null."
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        artwork = get_object_or_404(Artwork, id=int(request.POST['work_id']))
        old_data = get_object_or_404(D1B, id=request.POST["id"])
        formd1B_form = FormD1B(request.POST, instance=old_data)
        if formd1B_form.is_valid():
            formd1B_form = formd1B_form.save(commit=False)
            formd1B_form.author = request.user
            formd1B_form.artwork = artwork
            formd1B_form = formd1B_form.save()
            response_data['successResult'] = 'Evaluation form submitted successfully!'
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResults'] = formd1B_form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif request.method == 'GET':
        artwork = get_object_or_404(Artwork, id=int(request.GET['work_id']))
        try:
            formd1B_model = get_object_or_404(D1B, author=request.user, artwork=artwork)
            formd1B_form = FormD1B(instance=formd1B_model)
        except:
            formd1B_form, formd1B_obj = D1B.objects.get_or_create(author=request.user, artwork=artwork)
        context = {'form': formd1B_form}
        return render(request, 'evaluationForms/D1B_form.html', context)
    else:
        response_data['errorResult'] = "Illegal access to the form"
        return HttpResponse(json.dumps(response_data),
            content_type="application/json")


def update_worklist(workid, status):
    artwork = get_object_or_404(Artwork, id=workid)
    artwork_form = EntryForm(instance=artwork)
    artwork_form = artwork_form.save(commit=False)
    artwork_form.status = status
    artwork_form = artwork_form.save()


@login_required
def create_d2(request):
    userModel = ProjectUser.objects.get(username=request.user)
    artwork = get_object_or_404(Artwork, id=int(request.GET['work_id']))
    if request.method == 'POST':
        response_data = {}
        formd2_form = FormD2(request.POST, request.FILES)
        if formd2_form.is_valid():
            formd2_form = formd2_form.save()
            response_data['successResult'] = 'The evaluation form submitted successfully!'
            response_data['id'] = formd2_form.id
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResults'] = formd2_form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif userModel.user_type == 1:
        try:
            formd2_model = get_object_or_404(D2, author=request.user)
            formd2_form = FormD2(instance=formd2_model)
        except:
            formd2_form, formd2_obj = D2.objects.get_or_create(author=request.user, artwork=artwork)
    else:
        formd2_form = FormD2()
    context = {'form': formd2_form}
    return render(request, 'evaluationForms/D2_form.html', context)

@login_required
def create_d3(request):
    userModel = ProjectUser.objects.get(username=request.user)
    artwork = get_object_or_404(Artwork, id=int(request.GET['work_id']))
    if request.method == 'POST':
        response_data = {}
        formd3_form = FormD3(request.POST, request.FILES)
        if formd3_form.is_valid():
            formd3_form = formd3_form.save()
            response_data['successResult'] = 'The evaluation form submitted successfully!'
            response_data['id'] = formd3_form.id
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResults'] = formd3_form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif userModel.user_type == 1:
        try:
            formd3_model = get_object_or_404(D3, author=request.user)
            formd3_form = FormD3(instance=formd3_model)
        except:
            formd3_form, formd3_obj = D3.objects.get_or_create(author=request.user, artwork=artwork)
    else:
        formd3_form = FormD3()
    context = {'form': formd3_form}
    return render(request, 'evaluationForms/D3_form.html', context)

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

def evalpage(request, id):
    work = get_object_or_404(Artwork, id)
    eval = EvalD1A.objects.filter(work_id=id)
    if not eval.exists():
        form = FormD1A()
    context = {'eval':eval, 'work':work}
    return render(request, 'evalstat.html', context)
'''
