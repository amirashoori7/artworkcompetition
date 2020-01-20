from django.shortcuts import render, get_object_or_404
from artwork.models import Artwork
from evaluation.forms import FormD1A
from django.http.response import HttpResponse
import json

def create_d1a(request):
#     work = get_object_or_404(Artwork, id=id)
    if request.method == 'POST':
        response_data = {}
        form = FormD1A(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            response_data['successResult'] = 'D1A form submitted successfully!'
            response_data['id'] = form.id
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
        else:
            response_data['errorResult'] = form.errors.as_json(True)
            return HttpResponse(json.dumps(response_data),
                content_type="application/json")
    else:
        form = FormD1A()
        context = {'form': form}
        return render(request, 'D1A_form.html', context)


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
