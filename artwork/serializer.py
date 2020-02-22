from rest_framework import serializers
from artwork.artwork_models import Artwork

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ['worktitle', 'surname', 'firstname',
                  'school', 'workfile', 'email',
                  'dob', 'parentname', 'parentemail',
                  'parentphone', 'learnergrade', 'teachername',
                  'teacheremail', 'teacherphone', 'testimonial',
                  'question1', 'question2', 'question3']
