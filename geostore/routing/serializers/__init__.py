from django.contrib.gis.geos import LineString
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_gis import serializers as geo_serializers


class RoutingRequestSerializer(serializers.Serializer):
    geom = geo_serializers.GeometryField(help_text=_("A linestring with ordered waypoints."),
                                         read_only=True)
    callback_id = serializers.CharField(required=False, read_only=True,
                                        help_text=_("Optional callback id to match with your request."))


class RoutingSerializer(RoutingRequestSerializer):
    request = RoutingRequestSerializer(read_only=True)
    geom = geo_serializers.GeometryField(help_text=_("A linestring with ordered waypoints."),
                                         write_only=True)
    callback_id = serializers.CharField(required=False, write_only=True,
                                        help_text=_("Optional callback id to match with your request."))
    route = serializers.JSONField(read_only=True)
    way = geo_serializers.GeometryField(read_only=True)

    def validate_geom(self, value):
        if not isinstance(value, LineString):
            raise ValidationError(_("Geometry should be a LineString object."))
        return value
