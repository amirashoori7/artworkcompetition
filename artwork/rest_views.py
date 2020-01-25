from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from .serializer import ArtworkSerializer
from .models_artwork import Artwork

def worklists(request):
    works = Artwork.objects.all()
    serializer = ArtworkSerializer(works, many=True)
    return JsonResponse(serializer.data, safe=False)
'''
class WorkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer = ArtworkSerializer
'''
