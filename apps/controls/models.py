from django.db import models

PIN_TYPES = (
    ('PU', 'Pump'),
    ('BU', 'Button'),
)


class Control(models.Model):
    """
    This is the particular IoT device, for example "My Raspberry Pi".
    The mac address should be unique and also the combination of device and pin number
    """
    device = models.ForeignKey('devices.Device', on_delete=models.CASCADE)
    created_dt = models.DateTimeField(verbose_name="Created date and time", auto_now_add=True)
    pin_number = models.PositiveIntegerField(help_text="This is the Device GPIO pin number that will be used")

    name = models.CharField(max_length=100, help_text='Control name to identify. For example: "Pump 2"')
    type = models.CharField(choices=PIN_TYPES, max_length=10, default='PU',
                            help_text='The type of object over which the GPIO pin will have control.')

    state = models.BooleanField(default=False, help_text='This is the current state (on/off) of this control.')
    last_changed = models.DateTimeField(help_text='The last time that the "state" value was updated.', null=True,
                                        blank=True)
    user_last_changed = models.DateTimeField(help_text='The last time that the "state" value was updated by user.',
                                             null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('device', 'pin_number',)

# class Pump(models.Model):
#     """
#     Class to contain information on the pump-type control
#     """
#     duration = models.PositiveIntegerField(verbose_name="Duration")
#     datalog_frequency = models.PositiveIntegerField(verbose_name="Frequency of the logging of the state")


# class Datalog(models.Model):
#     """
#     Timeseries log of the state of a control. one to one log with a control?
#     """
#     dt = models.DateTimeField(verbose_name="Created date and time", auto_now_add=True)
#     state = models.DateTimeField(verbose_name="Value", )
#     # poll every 10 secs?
