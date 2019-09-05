# Generated by Django 2.0.13 on 2019-05-03 15:26

from django.db import migrations, models
import terra.models


class Migration(migrations.Migration):

    dependencies = [
        ('terra', '0022_auto_20190417_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='geom_type',
            field=models.IntegerField(choices=[(terra.models.GeometryTypes(0), 0), (terra.models.GeometryTypes(1), 1), (terra.models.GeometryTypes(3), 3), (terra.models.GeometryTypes(4), 4), (terra.models.GeometryTypes(5), 5), (terra.models.GeometryTypes(6), 6), (terra.models.GeometryTypes(7), 7)], null=True),
        ),
    ]
