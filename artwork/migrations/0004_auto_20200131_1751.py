# Generated by Django 3.0 on 2020-01-31 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0003_auto_20200131_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='artwork.School'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='workfile',
            field=models.FileField(blank=True, null=True, upload_to='works'),
        ),
    ]
