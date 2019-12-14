from django.db import models
from multiselectfield import MultiSelectField
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
    ('2DGR', '2 Dimensional Geometric Relationships'),
    ('3DGR', '3 Dimensional Geometric Relationships'),
    ('AC', 'Accuracy and Percision'),
    ('AG', 'Analytical Geometry'),
    ('ANTISYM', 'Antisymmetry'),
    ('AMATH', 'Applied Mathematics'),
    ('ASYM', 'Asymmetry'),
    ('CAL', 'Calculation'),
    ('CONG', 'Congruency'),
    ('COOSYS', 'Coordinating System'),
    ('COUNT', 'Counting'),
    ('CURVES', 'Curves'),
    ('EQU', ' Equation'),
    ('ETHMATH', 'Ethnomathematics'),
    ('FIBO', 'Fibonacci'),
    ('FMATH', 'Formulate, Mathematical Symbols'),
    ('FRACT', 'Fractals'),
    ('GRT', 'Golden Ratio'),
    ('GEQU', 'Graph Equations'),
    ('GRPH', 'Graphs'),
    ('INFT', 'Infinity'),
    ('MTHK', 'Mathematical Thinking'),
    ('COSM', 'Mathematics in the Cosmos'),
    ('MSUM', 'Measurement'),
    ('LINE', 'Linearity'),
    ('NUM', 'Numbers'),
    ('PTT', 'Patterns'),
    ('PLGO', 'Planar Geometrical Objects'),
    ('PSOL', 'Problem Solving'),
    ('PRF', 'Proof'),
    ('PROP', 'Proportions'),
    ('PYTT', 'Pythagorean Theorem'),
    ('RFMA', 'Reflection on Math Anxiety'),
    ('RFHM', 'Reference to History of Math'),
    ('RFME', 'Reflection on Mathematics Education'),
    ('SEQ', 'Sequences'),
    ('SING', 'Singualarity'),
    ('SYMM', 'Symmetry'),
    ('TESS', 'Tessellation'),
    ('VCAL', 'Vector Calculus')
)

class EvalD1A(models.Model):
    biodetails = MultiSelectField(choices=VALIDATE_SUBMISSION, max_choices=1)
    picview = MultiSelectField(choices=VALIDATE_SUBMISSION, max_choices=1)
    paragraphsview = MultiSelectField(choices=VALIDATE_SUBMISSION,
                                      max_choices=1)
    comment = models.TextField(blank=True, max_length=200)

class EvalD1B(models.Model):
    workpicq = MultiSelectField(choices=QUALITY_SIFT, max_choices=1)
    answersq = MultiSelectField(choices=QUALITY_SIFT, max_choices=1)
    originq = MultiSelectField(choices=QUALITY_SIFT, max_choices=1)
    revisit = models.BooleanField(default=False)
    comment = models.TextField(blank=True, max_length=200)

class EvalD1C(models.Model):
    qualitysift = MultiSelectField(choices=QUALITY_SIFT, max_choices=1)
    comment = models.TextField(blank=True, max_length=200)

class EvalD2(models.Model):
    math = MultiSelectField(choices=MATH, max_choices=45)
    q1 = MultiSelectField(choices=WEIGHT, max_choices=1)
    q2 = MultiSelectField(choices=WEIGHT, max_choices=1)
    q3 = MultiSelectField(choices=WEIGHT, max_choices=1)
    q4 = MultiSelectField(choices=WEIGHT, max_choices=1)
    score = models.IntegerField(blank=True, max_length=20)

    #def save(self):
