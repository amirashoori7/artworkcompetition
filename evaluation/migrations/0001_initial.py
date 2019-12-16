# Generated by Django 2.2.6 on 2019-12-16 22:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvalD1A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biodetails', models.CharField(blank=True, choices=[('ACCEPT', 'work submission is accepted'), ('REJECT', 'work submission is rejected'), ('REVISE', 'work submission must be revised')], max_length=50, null=True)),
                ('picview', models.CharField(blank=True, choices=[('ACCEPT', 'work submission is accepted'), ('REJECT', 'work submission is rejected'), ('REVISE', 'work submission must be revised')], max_length=50, null=True)),
                ('paragraphsview', models.CharField(blank=True, choices=[('ACCEPT', 'work submission is accepted'), ('REJECT', 'work submission is rejected'), ('REVISE', 'work submission must be revised')], max_length=50, null=True)),
                ('comment', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EvalD1B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workpicq', models.CharField(blank=True, choices=[('IN', 'work in'), ('OUT', 'work out'), ('MAYBE', 'maybe work in')], max_length=50, null=True)),
                ('answersq', models.CharField(blank=True, choices=[('IN', 'work in'), ('OUT', 'work out'), ('MAYBE', 'maybe work in')], max_length=50, null=True)),
                ('originq', models.CharField(blank=True, choices=[('IN', 'work in'), ('OUT', 'work out'), ('MAYBE', 'maybe work in')], max_length=50, null=True)),
                ('revisit', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EvalD1C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualitysift', models.CharField(blank=True, choices=[('IN', 'work in'), ('OUT', 'work out'), ('MAYBE', 'maybe work in')], max_length=50, null=True)),
                ('comment', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EvalD2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('math', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('1', '2 Dimensional Geometric Relationships'), ('2', '3 Dimensional Geometric Relationships'), ('3', 'Accuracy and Percision'), ('4', 'Analytical Geometry'), ('5', 'Antisymmetry'), ('6', 'Applied Mathematics'), ('7', 'Asymmetry'), ('8', 'Calculation'), ('9', 'Congruency'), ('10', 'Coordinating System'), ('11', 'Counting'), ('12', 'Curves'), ('13', ' Equation'), ('14', 'Ethnomathematics'), ('15', 'Fibonacci'), ('16', 'Formulate, Mathematical Symbols'), ('17', 'Fractals'), ('18', 'Golden Ratio'), ('19', 'Graph Equations'), ('20', 'Graphs'), ('21', 'Infinity'), ('22', 'Mathematical Thinking'), ('23', 'Mathematics in the Cosmos'), ('24', 'Measurement'), ('25', 'Linearity'), ('26', 'Numbers'), ('27', 'Patterns'), ('28', 'Planar Geometrical Objects'), ('29', 'Problem Solving'), ('30', 'Proof'), ('31', 'Proportions'), ('32', 'Pythagorean Theorem'), ('33', 'Reflection on Math Anxiety'), ('34', 'Reference to History of Math'), ('35', 'Reflection on Mathematics Education'), ('36', 'Sequences'), ('37', 'Singualarity'), ('38', 'Symmetry'), ('39', 'Tessellation'), ('40', 'Vector Calculus')], max_length=50, null=True), size=None)),
                ('q1', models.IntegerField(choices=[('5', 'Excellent'), ('4', 'Good'), ('3', 'Average'), ('2', 'Minimal'), ('1', 'None')])),
                ('q2', models.IntegerField(choices=[('5', 'Excellent'), ('4', 'Good'), ('3', 'Average'), ('2', 'Minimal'), ('1', 'None')])),
                ('q3', models.IntegerField(choices=[('5', 'Excellent'), ('4', 'Good'), ('3', 'Average'), ('2', 'Minimal'), ('1', 'None')])),
                ('q4', models.IntegerField(choices=[('5', 'Excellent'), ('4', 'Good'), ('3', 'Average'), ('2', 'Minimal'), ('1', 'None')])),
                ('score', models.IntegerField(blank=True)),
            ],
        ),
    ]