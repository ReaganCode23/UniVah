# Generated by Django 5.1.1 on 2024-10-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Univah', '0009_rename_dropoff_location_riderequest_dropoff_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='password',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='rider',
            name='password',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
