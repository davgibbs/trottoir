from django.db import models
from django.conf import settings

from macaddress.fields import MACAddressField


HARDWARE_TYPES = (
    ('RP', 'Raspberry Pi 4 Model B'),
)


class Device(models.Model):
    """
    This is the particular IoT device, for example 'My Raspberry Pi'.
    The mac address should be unique and also the combination of adder_by_user and name
    """
    created_dt = models.DateTimeField(verbose_name='Created date and time', auto_now_add=True)
    added_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Maybe unique on name?
    name = models.CharField(max_length=100, help_text='Device name to identify')
    # maybe list of MACs in case have wifi and wired
    mac_address = MACAddressField(unique=True, help_text='Unique Device MAC address for WIFI network card')
    hardware = models.CharField(choices=HARDWARE_TYPES, max_length=10, default='RP')
    location = models.CharField(max_length=100, help_text='Device Location for weather data, etc')

    last_checkin_dt = models.DateTimeField(verbose_name='Last Check-in from device to platform', null=True, blank=True)

    def __str__(self):
        return self.name
