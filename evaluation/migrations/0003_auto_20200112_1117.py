# Generated by Django 3.0 on 2020-01-12 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0006_auto_20200112_1117'),
        ('evaluation', '0002_auto_20191221_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='d1a',
            name='artwork',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artwork.Artwork'),
        ),
        migrations.AddField(
            model_name='d1b',
            name='artwork',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artwork.Artwork'),
        ),
        migrations.AddField(
            model_name='d2',
            name='artwork',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artwork.Artwork'),
        ),
        migrations.AddField(
            model_name='d3',
            name='artwork',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artwork.Artwork'),
        ),
    ]
