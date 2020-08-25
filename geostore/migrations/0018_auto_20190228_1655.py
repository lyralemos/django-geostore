# Generated by Django 2.0.13 on 2019-02-28 16:55

try:
    from django.db.models import JSONField
except ImportError:  # TODO Remove when dropping Django releases < 3.1
    from django.contrib.postgres.fields import JSONField
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geostore', '0017_auto_20181114_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='properties',
            field=JSONField(blank=True, default=dict),
        ),
    ]
