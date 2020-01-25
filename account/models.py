from django.contrib.auth.models import AbstractUser
from django.db import models

class ProjectUser(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'judge1'),
      (4, 'judge2'),
      (5, 'judge3'),
      (6, 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(null=True, choices=USER_TYPE_CHOICES, default=1)
