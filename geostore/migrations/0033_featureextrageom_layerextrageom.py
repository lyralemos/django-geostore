# Generated by Django 2.2.6 on 2019-11-15 12:56

import django.contrib.gis.db.models.fields
try:
    from django.db.models import JSONField
except ImportError:  # TODO Remove when dropping Django releases < 3.1
    from django.contrib.postgres.fields import JSONField
from django.db import migrations, models
import django.db.models.deletion
import geostore
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('geostore', '0032_auto_20191016_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayerExtraGeom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('settings', JSONField(blank=True, default=dict)),
                ('geom_type', models.IntegerField(choices=[(0, geostore.GeometryTypes(0)), (1, geostore.GeometryTypes(1)), (3, geostore.GeometryTypes(3)), (4, geostore.GeometryTypes(4)), (5, geostore.GeometryTypes(5)), (6, geostore.GeometryTypes(6)), (7, geostore.GeometryTypes(7))], null=True)),
                ('slug', models.SlugField(editable=False)),
                ('title', models.CharField(max_length=250)),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_geometries', to='geostore.Layer')),
            ],
            options={
                'unique_together': {('layer', 'title'), ('layer', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='FeatureExtraGeom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('properties', JSONField(blank=True, default=dict)),
                ('identifier', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_geometries', to='geostore.Feature')),
                ('layer_extra_geom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='geostore.LayerExtraGeom')),
            ],
            options={
                'unique_together': {('feature', 'layer_extra_geom')},
            },
        ),
    ]
