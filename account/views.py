from django.views.generic import ListView
from .models import ProjectUser
from .forms import UserRegistrationForm

class ProjectUserList(ListView):
    model = ProjectUser

def registration(request):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        user = form.save()
        return render(request, 'register.html', {'user': user})
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)
