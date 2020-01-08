from django.views.generic import ListView
from .models import ProjectUser

class ProjectUserList(ListView):
    model = ProjectUser
