from artwork.artwork_models import Artwork
from artwork.artwork_models import School
import json
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from artwork.artwork_forms import EntryForm
from account.models_account import ProjectUser
from evaluation.models import D2


def worklists(request):
    grade = request.GET.get("grade", '')
    if grade != '':
        works = Artwork.objects.filter(learnergrade=grade, status=6).values_list('id', 'worktitle', 'learnergrade', 'thumbnail')
    else :
        works = Artwork.objects.all().values_list('id', 'worktitle', 'learnergrade', 'thumbnail')
    return HttpResponse(json.dumps(works),
                content_type="application/json")


def rest_work_list_judge(request):
    judge = request.GET.get("judge", '')
    if judge != '':
        judgeuser = ProjectUser.objects.get(username=judge)
        works = list(D2.objects.filter(author=judgeuser).values_list('id', 'score', 'artwork__id', 'artwork__worktitle', 'artwork__learnergrade', 'artwork__thumbnail'))
    return HttpResponse(json.dumps(works),
                content_type="application/json") 


def get_school(request):
    if request.GET['reason'] == '1':  # gets all the provinces
        data = list(School.objects.order_by().values_list("province").distinct("province"))
    elif request.GET['reason'] == '2':  # gets all the schools
        data = list(School.objects.filter(province=request.GET['prov'], name__icontains=request.GET['schooltxt']).order_by().values_list())
    else:
        data = list(School.objects.all())
    return HttpResponse(json.dumps(data),
                content_type="application/json")

def flag_work(request):
    wid = int(request.GET.get("work_id", 0))
    flag = int(request.GET.get("flag", -1))
    response_data = {}
    if wid > 0:
        artwork = get_object_or_404(Artwork, id=wid)
        artwork_form = EntryForm(instance=artwork)
        artwork_form = artwork_form.save(commit=False)
        if flag == 0 :
            artwork_form.flagged = False
        elif flag == 1:
            artwork_form.flagged = True
        else:
            response_data['errorResult'] = "Illegal flag value"
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        artwork_form = artwork_form.save()
    else:
        response_data['errorResult'] = "Illegal access to the artwork"
        return HttpResponse(json.dumps(response_data),
            content_type="application/json")
    response_data['successResult'] = "Successful"
    return HttpResponse(json.dumps(response_data),
            content_type="application/json")
    
def allocate_form(request):
    wid = int(request.GET.get("work_id", 0))
    judge = int(request.GET.get("judge", 0))
    response_data = {}
    if wid > 0:
        artwork = get_object_or_404(Artwork, id=wid)
        artwork_form = EntryForm(instance=artwork)
        artwork_form = artwork_form.save(commit=False)
        if flag == 1:
            artwork_form.flagged = True
        else:
            response_data['errorResult'] = "Illegal flag value"
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        artwork_form = artwork_form.save()
    else:
        response_data['errorResult'] = "Illegal access to the artwork"
        return HttpResponse(json.dumps(response_data),
            content_type="application/json")
    response_data['successResult'] = "Successful"
    return HttpResponse(json.dumps(response_data),
            content_type="application/json")
