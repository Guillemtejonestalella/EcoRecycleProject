# Generated by Django 5.0.3 on 2024-05-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_orderhomepickup_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='OrderDelivery',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='OrderDeliveryAddress',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
