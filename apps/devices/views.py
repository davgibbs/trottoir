from .models import Device

from rest_framework import viewsets, permissions, status

from .serializers import DeviceSerializer
from profiles.permissions import CanAccessUserAdmin


class DevicesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows address match users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated, )  # CanAccessUserAdmin,)
    queryset = Device.objects.all().order_by('created_dt')
    serializer_class = DeviceSerializer
