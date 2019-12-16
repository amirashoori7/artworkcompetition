from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import *

VALIDATE_SUBMISSION = (
    ('ACCEPT', 'work submission is accepted'),
    ('REJECT', 'work submission is rejected'),
    ('REVISE', 'work submission must be revised')
)
QUALITY_SIFT = (
    ('IN', 'work in'),
    ('OUT', 'work out'),
    ('MAYBE', 'maybe work in')
)

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
    ('13', ' Equation'),
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

class EvalD1A(models.Model):
    biodetails = models.CharField(choices=VALIDATE_SUBMISSION,
                                  max_length=50, blank=True, null=True)
    picview = models.CharField(choices=VALIDATE_SUBMISSION,
                               max_length=50, blank=True, null=True)
    paragraphsview = models.CharField(choices=VALIDATE_SUBMISSION,
                                      max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, max_length=200)

class EvalD1B(models.Model):
    workpicq = models.CharField(choices=QUALITY_SIFT,
                                max_length=50, blank=True, null=True)
    answersq = models.CharField(choices=QUALITY_SIFT,
                                max_length=50, blank=True, null=True)
    originq = models.CharField(choices=QUALITY_SIFT,
                               max_length=50, blank=True, null=True)
    revisit = models.BooleanField(default=False)
    comment = models.TextField(blank=True, max_length=200)

class EvalD1C(models.Model):
    qualitysift = models.CharField(choices=QUALITY_SIFT,
                                   max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, max_length=200)

class EvalD2(models.Model):
    math = ArrayField(
        models.CharField(choices=MATH, max_length=50, blank=True, null=True),
    )
    q1 = models.IntegerField(choices=WEIGHT)
    q2 = models.IntegerField(choices=WEIGHT)
    q3 = models.IntegerField(choices=WEIGHT)
    q4 = models.IntegerField(choices=WEIGHT)
    score = models.IntegerField(blank=True)

    #def save(self):
