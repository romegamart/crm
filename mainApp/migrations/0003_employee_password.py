# Generated by Django 5.0.6 on 2024-09-16 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_employee_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
