from django.contrib.postgres.fields import ArrayField
from django.db import models
from artwork.artwork_models import Artwork
from account.models_account import ProjectUser

WEIGHT = (
    ('4', 'Excellent'),
    ('3', 'Good'),
    ('2', 'Average'),
    ('1', 'Minimal'),
    ('0', 'None')
)
MATH = (
    ('1', 'Mathematical Symbols'),
    ('2', 'Counting or Calculation of Numbers '),
    ('3', 'Formulae or Equations'),
    ('4', 'Number Patterns (e.g. Fibonacci pattern)'),
    ('5', 'Number Ratios (e.g. Golden Ratio)'),
    ('6', 'Infinity'),
    ('7', 'Other'),
    ('8', 'Curves and Graphs'),
    ('9', 'Locus of points'),
    ('10', 'Other'),
    ('11', 'Coordinate System'),
    ('12', 'Polygons'),
    ('13', 'Circles and theorems relating to circles'),
    ('14', 'Transformation (e.g. rotation, translation, etc)'),
    ('15', 'Symmetry'),
    ('16', 'Tessellation (Tiling) of Surfaces'),
    ('17', 'Fractals'),
    ('18', 'Similarity or Congruency of Shapes'),
    ('19', 'Other'),
    ('20', 'Scientific Notation'),
    ('21', 'Distances in Space'),
    ('22', 'Measurement of Shapes'),
    ('23', 'Other'),
    ('24', 'Angles'),
    ('25', 'Ratios of Side-lengths'),
    ('26', 'Other'),
    ('27', 'Data Collection'),
    ('28', 'Probability'),
    ('29', 'Other'),
#     ('30', 'Proof'),
#     ('31', 'Proportions'),
#     ('32', 'Pythagorean Theorem'),
#     ('33', 'Reflection on Math Anxiety'),
#     ('34', 'Reference to History of Math'),
#     ('35', 'Reflection on Mathematics Education'),
#     ('36', 'Sequences'),
#     ('37', 'Singualarity'),
#     ('38', 'Symmetry'),
#     ('39', 'Tessellation'),
#     ('40', 'Vector Calculus')
)


class D1A(models.Model):
    artwork = models.ForeignKey(Artwork, blank=False, null=False, on_delete=models.CASCADE)
    imgq = models.IntegerField(blank=True, null=True)
    answersq = models.IntegerField(blank=True, null=True)
    originq = models.IntegerField(blank=True, null=True)
    revisit = models.BooleanField(default=False)
    comment = models.TextField(blank=True)
    author = models.ForeignKey(ProjectUser, blank=False, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ('create_D1A', 'can create D1A'),
            ('update_D1A', 'can update D1A'),
            ('view_D1A', 'can view D1A'),
        )


class D1B(models.Model):
    artwork = models.ForeignKey(Artwork, blank=False, null=False, on_delete=models.CASCADE)
    workis = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True)
    author = models.ForeignKey(ProjectUser, blank=False, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class D2(models.Model):
    artwork = models.ForeignKey(Artwork, blank=False, null=False, on_delete=models.CASCADE)
    math = ArrayField(models.CharField(choices=MATH, max_length=50, blank=True, null=True), default=list)
    q1 = models.IntegerField(blank=True, null=True, default=0)
    q2 = models.IntegerField(blank=True, null=True, default=0)
    q3 = models.IntegerField(blank=True, null=True, default=0)
    q4 = models.IntegerField(blank=True, null=True, default=0)
    comment = models.TextField(blank=True)
    score = models.FloatField(null=True, blank=True)
    author = models.ForeignKey(ProjectUser, blank=False, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.score = self.q1 + self.q2 + self.q3 + self.q4
        super(D2, self).save(*args, **kwargs)

#     var weights=[
#         {q: "q1", w: 10},
#         {q: "q2", w: 30},
#         {q: "q3", w: 20},
#         {q: "q4", w: 25},
#         {q: "q5", w: 15}]
class D3(models.Model):
    artwork = models.ForeignKey(Artwork, blank=False, null=False, on_delete=models.CASCADE)
    q1 = models.IntegerField(blank=True, null=True, default=0)
    q2 = models.IntegerField(blank=True, null=True, default=0)
    q3 = models.IntegerField(blank=True, null=True, default=0)
    q4 = models.IntegerField(blank=True, null=True, default=0)
    q5 = models.IntegerField(blank=True, null=True, default=0)
    comment = models.TextField(blank=True)
    score = models.FloatField(null=True, blank=True)
    author = models.ForeignKey(ProjectUser, blank=False, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def save(self, *args, **kwargs):
        self.score = (self.q1 * 10/4) + (self.q2 * 30/4) + (self.q3 * 20/4) + (self.q4 * 25/4) + (self.q5 * 15/4)
        super(D3, self).save(*args, **kwargs)