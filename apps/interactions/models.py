from django.db import models

ACTION_TYPES = (
    ('ON', 'Turn On'),
    ('OF', 'Turn Off'),
)


class Interaction(models.Model):
    duration = models.PositiveIntegerField(verbose_name="Duration")
    action = models.CharField(choices=ACTION_TYPES, max_length=2,
                              help_text='The action required')
