import logging
import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ipware import get_client_ip
import paho.mqtt.client as mqtt

from .serializers import ControlSerializer
from .models import Control

logger = logging.getLogger(__name__)

MQTT_TOPIC = 'hello/world'
MQTT_HOSTNAME = 'localhost'


def index(request):
    """
    Base index on what to show when user comes to base
    :param request: request object
    :return: redirect to the correct page depending if user is logged in
    """
    return render(request, 'controls/index.html', {})


def about(request):
    """
    Base index on what to show when user comes to base
    :param request: request object
    :return: redirect to the correct page depending if user is logged in
    """
    return render(request, 'controls/about.html', {})


@login_required
def app(request):
    """
    Base index on what to show when user comes to base
    :param request: request object
    :return: redirect to the correct page depending if user is logged in
    """
    client_ip, _ = get_client_ip(request)
    address_matching_user = request.user
    address_matching_user.last_login_ip = client_ip
    address_matching_user.save(update_fields=['last_login_ip'])
    return render(request, 'controls/app.html', {})


class ControlsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows address match users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Control.objects.all().order_by('created_dt')
    serializer_class = ControlSerializer


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated, ))
def update_state(request):
    duration = request.data['duration']
    control_id = request.data['controlId']
    logger.info('Turn on control id %s for %s seconds' % (control_id, duration))

    iot_client = mqtt.Client()
    iot_client.connect(MQTT_HOSTNAME, port=1883, keepalive=60)
    message = json.dumps({'duration': duration, 'controlId': control_id})
    iot_client.publish(MQTT_TOPIC, message)

    return Response(status=status.HTTP_200_OK)

