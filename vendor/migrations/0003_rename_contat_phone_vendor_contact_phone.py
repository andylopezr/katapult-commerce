# Generated by Django 4.1.5 on 2023-02-04 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_alter_vendor_contat_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='contat_phone',
            new_name='contact_phone',
        ),
    ]
