# Generated by Django 5.1.1 on 2024-11-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Univah', '0015_riderequest_phone_number_alter_driver_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riderequest',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='rider',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]