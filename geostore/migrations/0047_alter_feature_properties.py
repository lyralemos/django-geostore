# Generated by Django 3.2.18 on 2023-03-06 15:54

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geostore', '0046_auto_20211013_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='properties',
            field=models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, verbose_name='Properties'),
        ),
    ]
