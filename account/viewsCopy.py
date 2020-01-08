from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .backends import EmailAuthBackend
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

'''
#this is custom test login view, which is replaced by using django auth_views

def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
 
    context = {'form': form}
    return render(request, 'login.html', context)
'''
