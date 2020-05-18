from rest_framework import serializers

from .models import Control


class ControlSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source='device.name')

    class Meta:
        model = Control
        fields = ('id', 'created_dt', 'pin_number', 'name', 'device_name', 'state')
        read_only_fields = ['id', 'created_dt', 'pin_number', 'name', 'state']
