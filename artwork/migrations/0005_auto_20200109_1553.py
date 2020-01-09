# Generated by Django 3.0 on 2020-01-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0004_auto_20200104_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='status',
            field=models.IntegerField(choices=[(0, 'Submitted Successfully'), (1, 'Revision Required'), (2, 'Rejected Stage 0'), (3, 'Accepted Stage 0'), (4, 'Waiting For Decision'), (5, 'Accepted Stage 1'), (6, 'Rejected Stage 1'), (7, 'Waiting For Artpost'), (8, 'Rejected Stage 2'), (9, 'Artpost Recieved'), (10, 'Rejected Stage 3'), (11, 'Winner')], default=0),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='workformulafile',
            field=models.FileField(blank='True', null=True, upload_to='formulas'),
        ),
    ]
