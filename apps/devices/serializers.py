from rest_framework import serializers

from .models import Device


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('id', 'created_dt', 'added_by_user', 'name', 'mac_address', 'hardware', 'location', 'last_checkin_dt')
        read_only_fields = ['id', 'created_dt', 'added_by_user', 'name', 'mac_address', 'hardware', 'location',
                            'last_checkin_dt']
