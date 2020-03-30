from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
import json
from artwork.artwork_models import Artwork
from django.contrib.auth.decorators import login_required
from evaluation.models import D1A, D2, D1B, D3
from evaluation.forms_evaluation import FormD1A, FormD2, FormD1B, FormD3
import artwork
from artwork.artwork_forms import EntryForm
from account.models_account import ProjectUser


@login_required
def create_d1a(request):
    response_data = {}
    if request.method == 'POST':
        if request.POST['work_id'] is None or request.POST['work_id'] == '':
            response_data['errorResult'] = "Illegal access to the form, the work id is null."
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        artwork = get_object_or_404(Artwork, id=int(request.POST['work_id']))
        old_data = get_object_or_404(D1A, id=request.POST["id"])
        formd1A_form = FormD1A(request.POST, instance=old_data)
        if formd1A_form.is_valid():
            if artwork.status != 5:
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
        workid = int(request.GET.get("work_id", 0))
        if workid > 0:
            artwork = get_object_or_404(Artwork, id=workid)
        formid = int(request.GET.get("form_id", 0))
        if formid > 0 :
            formd1A_model = D1A.objects.get(id=formid)
            formd1A_form = FormD1A(instance=formd1A_model)
        else:
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
            update_worklist(int(request.POST['work_id']), int(request.POST['status']))
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
        workid = int(request.GET.get("work_id", 0))
        if workid > 0:
            artwork = get_object_or_404(Artwork, id=workid)
        formid = int(request.GET.get("form_id", 0))
        if formid > 0 :
            formd1B_model = D1B.objects.get(id=formid)
            artwork = formd1B_model.artwork
            formd1B_form = FormD1B(instance=formd1B_model)
        else:
            formd1B_form, form1B_obj = D1B.objects.get_or_create(author=request.user, artwork=artwork)
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
    if request.method == 'POST':
        response_data = {}
        if request.POST['work_id'] is None or request.POST['work_id'] == '':
            response_data['errorResult'] = "Illegal access to the form, the work id is null."
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        artwork = get_object_or_404(Artwork, id=int(request.POST['work_id']))
        old_data = get_object_or_404(D2, id=request.POST["id"])
        formd2_form = FormD2(request.POST, instance=old_data)
        math = request.POST.getlist('math')
        if formd2_form.is_valid():
            formd2_form = formd2_form.save(commit=False)
            formd2_form.author = request.user
            formd2_form.artwork = artwork
            formd2_form.math = math
            formd2_form.save()
            response_data['successResult'] = 'The evaluation form submitted successfully!'
            response_data['id'] = formd2_form.id
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResults'] = formd2_form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif request.method == 'GET':
#         artwork = get_object_or_404(Artwork, id=int(request.GET['work_id']))
        workid = int(request.GET.get("work_id", 0))
        if workid > 0:
            artwork = get_object_or_404(Artwork, id=workid)
        formid = int(request.GET.get("form_id", 0))
        if formid > 0 :
            formd2_model = D2.objects.get(id=formid)
            artwork = formd2_model.artwork
        else:
            formd2_model, form2_obj = D2.objects.get_or_create(author=request.user, artwork=artwork)
        formd2_form = FormD2(instance=formd2_model)
        context = {'form': formd2_form}
        return render(request, 'evaluationForms/D2_form.html', context)
    else:
        response_data['errorResult'] = "Illegal access to the form"
        return HttpResponse(json.dumps(response_data),
            content_type="application/json")

@login_required
def create_d3(request):
    if request.method == 'POST':
        response_data = {}
        if request.POST['work_id'] is None or request.POST['work_id'] == '':
            response_data['errorResult'] = "Illegal access to the form, the work id is null."
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        old_data = get_object_or_404(D3, id=request.POST["id"])
        formd3_form = FormD3(request.POST, instance=old_data)
        if formd3_form.is_valid():
            formd3_form = formd3_form.save(commit=False)
            artwork = get_object_or_404(Artwork, id=int(request.POST['work_id']))
            formd3_form.author = request.user
            formd3_form.artwork = artwork
            formd3_form.save()
            response_data['successResult'] = 'The evaluation form submitted successfully!'
            response_data['id'] = formd3_form.id
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResults'] = formd3_form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    elif request.method == 'GET':
#         artwork = get_object_or_404(Artwork, id=int(request.GET['work_id']))
        workid = int(request.GET.get("work_id", 0))
        if workid > 0:
            artwork = get_object_or_404(Artwork, id=workid)
#         if int(request.GET.get("author_id", 0)) > 0:
#             user = get_object_or_404(ProjectUser, id=int(request.GET.get("author_id", 0)))
#         else: 
#             user = request.user
#         try:
#             if request.user.user_type == 6 or request.user.user_type == 7:
#                 formd3_model = get_object_or_404(D3, artwork=artwork)
#             else:    
#             formd3_model = get_object_or_404(D3, author=user, artwork=artwork)
#             formd3_form = FormD3(instance=formd3_model)
#         except:
#             formd3_form, formd3_obj = D3.objects.get_or_create(author=user, artwork=artwork)
        formid = int(request.GET.get("form_id", 0))
        if formid > 0 :
            formd3_model = D3.objects.get(id=formid)
            artwork = formd3_model.artwork
        else:
            formd3_model = get_object_or_404(D3, author=request.user, artwork=artwork)
        formd3_form = FormD3(instance=formd3_model)
        context = {'form': formd3_form}
        return render(request, 'evaluationForms/D3_form.html', context)
    else:
        response_data['errorResult'] = "Illegal access to the form"
        return HttpResponse(json.dumps(response_data),
            content_type="application/json")


@login_required
def eval_forms_artwork(request):
    work = get_object_or_404(Artwork, id=request.GET.get('work_id'))
    d1as = D1A.objects.filter(artwork=work)
    d1bs = D1B.objects.filter(artwork=work)
    d2 = D2.objects.filter(artwork=work)
    d3 = D3.objects.filter(artwork=work)
    context = {'work': work, 'd1as': d1as, 'd1bs': d1bs, 'd2': d2, 'd3': d3}
    return render(request, 'evaluationForms/eval_forms.html', context)

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
