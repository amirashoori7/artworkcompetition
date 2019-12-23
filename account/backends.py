from .models import ProjectUser
from django.contrib.auth.models import check_password

class EmailAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = ProjectUser.objects.get(email=username)
            if user.check_password(password):
                return user
            except ProjectUser.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return ProjectUser.objects.get(pk=user_id)
        except ProjectUser.DoesNotExist:
            return None
