# Generated by Django 5.1.1 on 2024-09-24 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_client_client_next_followup_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='status',
            new_name='empstatus',
        ),
    ]
