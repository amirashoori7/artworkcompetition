# Generated by Django 3.0 on 2020-01-30 23:23

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='D3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.IntegerField(blank=True, null=True)),
                ('q2', models.IntegerField(blank=True, null=True)),
                ('q3', models.IntegerField(blank=True, null=True)),
                ('q4', models.IntegerField(blank=True, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artwork.Artwork')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='D2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('math', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('1', '2 Dimensional Geometric Relationships'), ('2', '3 Dimensional Geometric Relationships'), ('3', 'Accuracy and Percision'), ('4', 'Analytical Geometry'), ('5', 'Antisymmetry'), ('6', 'Applied Mathematics'), ('7', 'Asymmetry'), ('8', 'Calculation'), ('9', 'Congruency'), ('10', 'Coordinating System'), ('11', 'Counting'), ('12', 'Curves'), ('13', ' Equation'), ('14', 'Ethnomathematics'), ('15', 'Fibonacci'), ('16', 'Formulate, Mathematical Symbols'), ('17', 'Fractals'), ('18', 'Golden Ratio'), ('19', 'Graph Equations'), ('20', 'Graphs'), ('21', 'Infinity'), ('22', 'Mathematical Thinking'), ('23', 'Mathematics in the Cosmos'), ('24', 'Measurement'), ('25', 'Linearity'), ('26', 'Numbers'), ('27', 'Patterns'), ('28', 'Planar Geometrical Objects'), ('29', 'Problem Solving'), ('30', 'Proof'), ('31', 'Proportions'), ('32', 'Pythagorean Theorem'), ('33', 'Reflection on Math Anxiety'), ('34', 'Reference to History of Math'), ('35', 'Reflection on Mathematics Education'), ('36', 'Sequences'), ('37', 'Singualarity'), ('38', 'Symmetry'), ('39', 'Tessellation'), ('40', 'Vector Calculus')], max_length=50, null=True), size=None)),
                ('q1', models.IntegerField(blank=True, null=True)),
                ('q2', models.IntegerField(blank=True, null=True)),
                ('q3', models.IntegerField(blank=True, null=True)),
                ('q4', models.IntegerField(blank=True, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artwork.Artwork')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='D1B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workis', models.IntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artwork.Artwork')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='D1A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgq', models.IntegerField(blank=True, null=True)),
                ('answersq', models.IntegerField(blank=True, null=True)),
                ('originq', models.IntegerField(blank=True, null=True)),
                ('revisit', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artwork.Artwork')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('create_D1A', 'can create D1A'), ('update_D1A', 'can update D1A'), ('view_D1A', 'can view D1A')),
            },
        ),
    ]
