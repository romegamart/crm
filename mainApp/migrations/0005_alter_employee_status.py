# Generated by Django 5.0.6 on 2024-09-16 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(blank=True, default='active', max_length=30, null=True),
        ),
    ]
