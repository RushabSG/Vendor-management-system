# Generated by Django 5.0 on 2023-12-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms_app', '0006_alter_vendormodel_average_response_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='order_date',
            field=models.DateTimeField(),
        ),
    ]
