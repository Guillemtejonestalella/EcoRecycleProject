# Generated by Django 5.0.3 on 2024-05-14 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderlineItem', models.CharField(max_length=70)),
                ('OrderlineUnits', models.IntegerField(blank=True, null=True)),
                ('OrderlineWeight', models.IntegerField(blank=True, null=True)),
                ('OrderlineBrand', models.CharField(blank=True, max_length=50, null=True)),
                ('OrderlineHeight', models.IntegerField(blank=True, null=True)),
                ('OrderlineDepth', models.IntegerField(blank=True, null=True)),
                ('OrderlineWidth', models.IntegerField(blank=True, null=True)),
                ('OrderlineStatus', models.CharField(max_length=70)),
                ('OrderlineObservations', models.CharField(blank=True, max_length=300, null=True)),
                ('OrderlinePoints', models.IntegerField()),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
