from rest_framework import serializers
from .models import Artwork

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ['worktitle', 'surname', 'firstname',
                  'school', 'workfile', 'email',
                  'dob', 'age', 'parentname', 'parentemail',
                  'parentphone', 'learnergrade', 'teachername',
                  'teacheremail', 'teacherphone', 'testimonial',
                  'question1', 'question2', 'question3']
