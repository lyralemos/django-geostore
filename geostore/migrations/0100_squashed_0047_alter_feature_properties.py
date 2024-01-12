# Generated by Django 5.0.1 on 2024-01-12 11:12

import django.contrib.gis.db.models.fields
import django.contrib.postgres.indexes
import django.contrib.postgres.operations
import django.core.serializers.json
import django.db.migrations.operations.special
import django.db.models.deletion
import django.utils.timezone
import geostore
import geostore.validators
import uuid
from django.db import migrations, models


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# geostore.migrations.0013_auto_20180919_1146
# geostore.migrations.0027_layergroup

class Migration(migrations.Migration):
    replaces = [
        ('geostore', '0001_initial'), ('geostore', '0011_auto_20180711_0831'),
        ('geostore', '0013_auto_20180919_1146'), ('geostore', '0014_auto_20180918_1210'),
        ('geostore', '0015_auto_20181005_1302'), ('geostore', '0016_auto_20181120_1059'),
        ('geostore', '0017_auto_20181114_0806'), ('geostore', '0018_auto_20190326_1049'),
        ('geostore', '0018_auto_20190228_1655'), ('geostore', '0019_merge_20190329_1056'),
        ('geostore', '0020_auto_20190401_1139'), ('geostore', '0021_auto_20190415_0945'),
        ('geostore', '0022_auto_20190417_1610'), ('geostore', '0023_layer_type_geom'),
        ('geostore', '0024_layer_geom_type'), ('geostore', '0025_auto_20190613_1341'),
        ('geostore', '0026_auto_20190613_1529'), ('geostore', '0027_layergroup'),
        ('geostore', '0028_remove_layer_group'), ('geostore', '0029_auto_20190926_0803'),
        ('geostore', '0030_auto_20191007_1459'), ('geostore', '0031_layer_authorized_groups'),
        ('geostore', '0032_auto_20191016_0844'), ('geostore', '0033_featureextrageom_layerextrageom'),
        ('geostore', '0034_auto_20191209_0902'), ('geostore', '0035_layerextrageom_editable'),
        ('geostore', '0036_auto_20200116_0926'), ('geostore', '0037_auto_20200127_1357'),
        ('geostore', '0038_auto_20200128_1442'), ('geostore', '0039_auto_20200131_1758'),
        ('geostore', '0037_auto_20200624_1440'), ('geostore', '0038_auto_20200625_1244'),
        ('geostore', '0040_merge_20200625_1508'), ('geostore', '0041_auto_20200625_1515'),
        ('geostore', '0042_layer_routable'), ('geostore', '0042_auto_20201015_1328'),
        ('geostore', '0043_merge_20201023_1209'), ('geostore', '0044_auto_20201106_1638'),
        ('geostore', '0045_auto_20210429_0818'), ('geostore', '0046_auto_20211013_1334'),
        ('geostore', '0047_alter_feature_properties')
    ]

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('settings', models.JSONField(blank=True, default=dict)),
                ('geom_type', models.IntegerField(
                    choices=[(0, 'Point'), (1, 'LineString'), (3, 'Polygon'), (4, 'MultiPoint'), (5, 'MultiLineString'),
                             (6, 'MultiPolygon'), (7, 'GeometryCollection')], null=True)),
                ('routable', models.BooleanField(default=False, help_text='Used for make layer routable')),
                ('name', models.CharField(default=uuid.uuid4, max_length=256, unique=True, verbose_name='Name')),
                ('schema',
                 models.JSONField(blank=True, default=dict, validators=[geostore.validators.validate_json_schema],
                                  verbose_name='Schema')),
                ('authorized_groups',
                 models.ManyToManyField(blank=True, related_name='authorized_layers', to='auth.group',
                                        verbose_name='Authorized groups')),
            ],
            options={
                'ordering': ['id'],
                'permissions': (('can_manage_layers', 'Has all permissions on layers'),
                                ('can_export_layers', 'Is able to export layers'),
                                ('can_import_layers', 'Is able to import layers')),
            },
            bases=(geostore.import_export.imports.LayerImportMixin, geostore.import_export.exports.LayerExportMixin,
                   models.Model),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('source', models.IntegerField(blank=True, editable=False, help_text='Internal field used by pgRouting',
                                               null=True)),
                ('target', models.IntegerField(blank=True, editable=False, help_text='Internal field used by pgRouting',
                                               null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('identifier', models.CharField(default=uuid.uuid4, max_length=255, verbose_name='Identifier')),
                ('properties',
                 models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder,
                                  verbose_name='Properties')),
                ('layer',
                 models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.PROTECT, related_name='features',
                                   to='geostore.layer', verbose_name='Layer')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='LayerExtraGeom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('settings', models.JSONField(blank=True, default=dict)),
                ('geom_type', models.IntegerField(
                    choices=[(0, 'Point'), (1, 'LineString'), (3, 'Polygon'), (4, 'MultiPoint'), (5, 'MultiLineString'),
                             (6, 'MultiPolygon'), (7, 'GeometryCollection')], null=True)),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Order')),
                ('slug', models.SlugField(editable=False)),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('editable', models.BooleanField(default=True, verbose_name='Editable')),
                ('layer',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_geometries',
                                   to='geostore.layer', verbose_name='Layer')),
            ],
            options={
                'ordering': ('layer', 'order'),
            },
        ),
        migrations.CreateModel(
            name='FeatureExtraGeom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(spatial_index=False, srid=4326)),
                ('properties', models.JSONField(blank=True, default=dict, verbose_name='Properties')),
                ('identifier', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True,
                                                verbose_name='Identifier')),
                ('feature',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_geometries',
                                   to='geostore.feature', verbose_name='Feature')),
                ('layer_extra_geom',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features',
                                   to='geostore.layerextrageom', verbose_name='Feature')),
            ],
        ),
        migrations.CreateModel(
            name='LayerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(unique=True)),
                ('layers',
                 models.ManyToManyField(related_name='layer_groups', to='geostore.layer', verbose_name='Layers')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LayerRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False)),
                ('relation_type', models.CharField(blank=True, choices=[(None, 'Manual'), ('intersects', 'Intersects'),
                                                                        ('distance', 'Distance')],
                                                   default=(None, 'Manual'), max_length=25)),
                ('settings', models.JSONField(blank=True, default=dict)),
                ('exclude', models.JSONField(blank=True, default=dict,
                                             help_text='qs exclude (ex: {"pk__in": [...], "identifier__in":[...]}')),
                ('destination',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relations_as_destination',
                                   to='geostore.layer')),
                ('origin',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relations_as_origin',
                                   to='geostore.layer')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FeatureRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('properties', models.JSONField(blank=True, default=dict, verbose_name='Properties')),
                ('destination',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_as_destination',
                                   to='geostore.feature', verbose_name='Destination')),
                ('origin',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_as_origin',
                                   to='geostore.feature', verbose_name='Origin')),
                ('relation',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_features',
                                   to='geostore.layerrelation', verbose_name='Relation')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['layer'], name='geostore_fe_layer_i_71cad6_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['updated_at'], name='geostore_fe_updated_fcdc6b_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['updated_at', 'layer'], name='geostore_fe_updated_bdb823_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['layer', 'identifier'], name='geostore_fe_layer_i_141c81_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['id', 'layer'], name='geostore_fe_id_bb7476_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['source', 'layer'], name='geostore_fe_source_cdd710_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['target', 'layer'], name='geostore_fe_target_b00bb7_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['source', 'target', 'layer'], name='geostore_fe_source_155396_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=django.contrib.postgres.indexes.GistIndex(fields=['layer', 'geom'],
                                                            name='geostore_fe_layer_i_c3168f_gist'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=django.contrib.postgres.indexes.GinIndex(fields=['properties'], name='properties_gin_index'),
        ),
        migrations.AddConstraint(
            model_name='feature',
            constraint=models.CheckConstraint(check=models.Q(('geom__isvalid', True)), name='geom_is_valid'),
        ),
        migrations.AddConstraint(
            model_name='feature',
            constraint=models.CheckConstraint(check=models.Q(('geom__isempty', False)), name='geom_is_empty'),
        ),
        migrations.AlterUniqueTogether(
            name='layerextrageom',
            unique_together={('layer', 'slug'), ('layer', 'title')},
        ),
        migrations.AddIndex(
            model_name='featureextrageom',
            index=models.Index(fields=['layer_extra_geom', 'identifier'], name='geostore_fe_layer_e_aa3cea_idx'),
        ),
        migrations.AddIndex(
            model_name='featureextrageom',
            index=django.contrib.postgres.indexes.GistIndex(fields=['layer_extra_geom', 'geom'],
                                                            name='feg_geom_gist_index'),
        ),
        migrations.AddIndex(
            model_name='featureextrageom',
            index=django.contrib.postgres.indexes.GinIndex(fields=['properties'], name='feg_properties_gin_index'),
        ),
        migrations.AddConstraint(
            model_name='featureextrageom',
            constraint=models.CheckConstraint(check=models.Q(('geom__isvalid', True)), name='geom_extra_is_valid'),
        ),
        migrations.AddConstraint(
            model_name='featureextrageom',
            constraint=models.CheckConstraint(check=models.Q(('geom__isempty', False)), name='geom_extra_is_empty'),
        ),
        migrations.AlterUniqueTogether(
            name='featureextrageom',
            unique_together={('feature', 'layer_extra_geom')},
        ),
        migrations.AlterUniqueTogether(
            name='layerrelation',
            unique_together={('name', 'origin')},
        ),
    ]
