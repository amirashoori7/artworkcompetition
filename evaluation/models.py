from django.contrib.postgres.fields import ArrayField
from django.db import models
from artwork.artwork_models import Artwork
from account.models_account import ProjectUser
from django.template.defaultfilters import default

WEIGHT = (
    ('5', 'Excellent'),
    ('4', 'Good'),
    ('3', 'Average'),
    ('2', 'Minimal'),
    ('1', 'None')
)
MATH = (
    ('1', '2 Dimensional Geometric Relationships'),
    ('2', '3 Dimensional Geometric Relationships'),
    ('3', 'Accuracy and Percision'),
    ('4', 'Analytical Geometry'),
    ('5', 'Antisymmetry'),
    ('6', 'Applied Mathematics'),
    ('7', 'Asymmetry'),
    ('8', 'Calculation'),
    ('9', 'Congruency'),
    ('10', 'Coordinating System'),
    ('11', 'Counting'),
    ('12', 'Curves'),
    ('13', 'Equation'),
    ('14', 'Ethnomathematics'),
    ('15', 'Fibonacci'),
    ('16', 'Formulate, Mathematical Symbols'),
    ('17', 'Fractals'),
    ('18', 'Golden Ratio'),
    ('19', 'Graph Equations'),
    ('20', 'Graphs'),
    ('21', 'Infinity'),
    ('22', 'Mathematical Thinking'),
    ('23', 'Mathematics in the Cosmos'),
    ('24', 'Measurement'),
    ('25', 'Linearity'),
    ('26', 'Numbers'),
    ('27', 'Patterns'),
    ('28', 'Planar Geometrical Objects'),
    ('29', 'Problem Solving'),
    ('30', 'Proof'),
    ('31', 'Proportions'),
    ('32', 'Pythagorean Theorem'),
    ('33', 'Reflection on Math Anxiety'),
    ('34', 'Reference to History of Math'),
    ('35', 'Reflection on Mathematics Education'),
    ('36', 'Sequences'),
    ('37', 'Singualarity'),
    ('38', 'Symmetry'),
    ('39', 'Tessellation'),
    ('40', 'Vector Calculus')
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
    math = ArrayField(models.CharField(choices=MATH, max_length=50, blank=True, null=True), default=[])
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


class D3(models.Model):
    artwork = models.ForeignKey(Artwork, blank=False, null=False, on_delete=models.CASCADE)
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
