from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in

from django_countries.fields import CountryField


def update_previous_login(sender, user, **kwargs):
    """
    A signal receiver which updates the previous_login date for
    the user logging in, and the duplicated_last_login.
    The user of the duplicated_last_login is to ensure that the
    previous_login gets updated first.
    """
    user.previous_login = user.duplicated_last_login
    user.duplicated_last_login = timezone.now()
    user.save(update_fields=['previous_login', 'duplicated_last_login'])


user_logged_in.connect(update_previous_login)


class TrottoirUser(AbstractUser):
    """
    This is an extension to the AbstractUser and used to store address matching specifics
    The username and the email must be unique
    """
    previous_login = models.DateTimeField('Previous login', default=timezone.now)
    duplicated_last_login = models.DateTimeField('Duplicated last login', default=timezone.now)

    company_name = models.CharField(max_length=50, null=True, blank=True)
    company_address_first_line = models.CharField(max_length=50, null=True, blank=True)
    company_address_second_line = models.CharField(max_length=50, null=True, blank=True)
    company_address_third_line = models.CharField(max_length=50, null=True, blank=True)
    company_country = CountryField(null=True, blank=True)

    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    access_user_admin = models.BooleanField(verbose_name="Access user admin", default=False,
                                            help_text="This field should be ticked if the user should be able to "
                                                      "access the User admin section.")

    def __unicode__(self):
        return self.username

    def get_full_name_or_username(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        if full_name == ' ':
            return self.username

        return full_name.strip()
