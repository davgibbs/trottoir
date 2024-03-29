# Generated by Django 2.2.12 on 2020-05-03 18:17

from django.db import migrations
import macaddress.fields


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_auto_20200503_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='mac_address',
            field=macaddress.fields.MACAddressField(help_text='Unique Device MAC address for WIFI network card', integer=True, unique=True),
        ),
    ]
