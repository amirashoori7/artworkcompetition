from django.http import JsonResponse
from .serializer import ArtworkSerializer
from .models_artwork import Artwork
from artwork.models_artwork import School

def worklists(request):
    works = Artwork.objects.all()
    serializer = ArtworkSerializer(works, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_school(request):
    schools = School.objects.all()
    schools = School.objects.order_by().values_list('province').distinct()
    response_data = {}
    print(schools)
'''
class WorkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer = ArtworkSerializer
'''
