from django.http import JsonResponse
from .serializer import ArtworkSerializer
from artwork.artwork_models import Artwork
from artwork.artwork_models import School
import json
from django.http.response import HttpResponse
from django.db.models.functions.text import Lower
from django.shortcuts import get_object_or_404
from artwork.artwork_forms import EntryForm

def worklists(request):
    works = Artwork.objects.all()
    serializer = ArtworkSerializer(works, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_school(request):
    if request.GET['reason'] == '1':#gets all the provinces
        data = list(School.objects.order_by().values_list("province").distinct("province"))
    elif request.GET['reason'] == '2':#gets all the schools
        data = list(School.objects.filter(province=request.GET['prov'],name__icontains=request.GET['schooltxt']).order_by().values_list())
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