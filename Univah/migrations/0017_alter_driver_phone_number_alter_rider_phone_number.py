# Generated by Django 5.1.1 on 2024-11-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Univah', '0016_remove_riderequest_phone_number_rider_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='rider',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
