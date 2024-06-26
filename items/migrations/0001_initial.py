# Generated by Django 5.0.3 on 2024-05-03 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=70, verbose_name='Item')),
                ('ItemImage', models.ImageField(upload_to='ecoApp/static/asstets/img', verbose_name='Item Image')),
                ('ItemDescription', models.TextField(max_length=999, verbose_name='Item Description')),
                ('Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'db_table': 'Items',
                'ordering': ['id'],
            },
        ),
    ]
