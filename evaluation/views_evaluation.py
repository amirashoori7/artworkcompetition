from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
import json
from artwork.models_artwork import Artwork
from django.contrib.auth.decorators import login_required
from account.models_account import ProjectUser
from evaluation.models import D1A
from evaluation.forms_evaluation import FormD1A

@login_required
def create_d1a(request):
    userModel = ProjectUser.objects.get(username=request.user)
    artwork = get_object_or_404(Artwork, id=int(request.GET['work_id']))
    if request.method == 'POST':
        response_data = {}
        formd1A_form = FormD1A(request.POST, request.FILES)
        if formd1A_form.is_valid():
            formd1A_form = formd1A_form.save()
            response_data['successResult'] = 'D1A form submitted successfully!'
            response_data['id'] = formd1A_form.id
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResult'] = formd1A_form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif userModel.user_type == 1:
        try:
            formd1A_model = get_object_or_404(D1A, author=request.user)
            formd1A_form = FormD1A(instance=formd1A_model)
        except:
            formd1A_form, formd1A_obj = D1A.objects.get_or_create(author=request.user, artwork=artwork)
    else:
        formd1A_form = FormD1A()
    context = {'form': formd1A_form}
    return render(request, 'evaluationForms/D1A_form.html', context)


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
