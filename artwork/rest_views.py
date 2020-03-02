from django.http import JsonResponse
from .serializer import ArtworkSerializer
from artwork.artwork_models import Artwork
from artwork.artwork_models import School
import json
from django.http.response import HttpResponse
from django.db.models.functions.text import Lower

def worklists(request):
    works = Artwork.objects.all()
    serializer = ArtworkSerializer(works, many=True)
    return JsonResponse(serializer.data, safe=False)

# def get_school(request):
#     if request.GET['reason'] == '1':#gets all the provinces
#         data = list(School.objects.order_by().values_list("province").distinct("province"))
#     elif request.GET['reason'] == '2':#gets all the regions for a province
#         data = list(School.objects.filter(province=request.GET['prov']).order_by().values_list("region", flat=True).distinct("region"))
#     elif request.GET['reason'] == '3':#gets all the schools
#         data = list(School.objects.filter(province=request.GET['prov'], region=request.GET['reg']).order_by().values_list())
#     else:
#         data = list(School.objects.all())
#     return HttpResponse(json.dumps(data),
#                 content_type="application/json")



def get_school(request):
    if request.GET['reason'] == '1':#gets all the provinces
        data = list(School.objects.order_by().values_list("province").distinct("province"))
#     elif request.GET['reason'] == '2':#gets all the regions for a province
#         data = list(School.objects.filter(province=request.GET['prov']).order_by().values_list("region", flat=True).distinct("region"))
    elif request.GET['reason'] == '2':#gets all the schools
        data = list(School.objects.filter(province=request.GET['prov'],name__icontains=request.GET['schooltxt']).order_by().values_list())
    else:
        data = list(School.objects.all())
    return HttpResponse(json.dumps(data),
                content_type="application/json")
