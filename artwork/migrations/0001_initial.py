# Generated by Django 2.2.6 on 2019-12-16 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('address', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'school',
                'verbose_name_plural': 'schools',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worktitle', models.CharField(max_length=300)),
                ('surname', models.CharField(db_index=True, max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('workfile', models.ImageField(upload_to='works')),
                ('email', models.EmailField(max_length=100)),
                ('dob', models.DateField(null=True)),
                ('age', models.IntegerField(editable=False, null=True)),
                ('parentname', models.CharField(blank=True, max_length=200)),
                ('parentphone', models.CharField(blank=True, max_length=100, null=True)),
                ('parentemail', models.EmailField(blank=True, max_length=100)),
                ('learnergrade', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('teachername', models.CharField(blank=True, max_length=300)),
                ('teacherphone', models.CharField(blank=True, max_length=100, null=True)),
                ('teacheremail', models.EmailField(blank=True, max_length=100)),
                ('testimonial', models.BooleanField(default=False)),
                ('question1', models.TextField(blank=True)),
                ('question2', models.TextField(blank=True)),
                ('question3', models.TextField(blank=True)),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='artwork.School')),
            ],
            options={
                'ordering': ['surname'],
                'index_together': {('id', 'surname')},
            },
        ),
    ]
