# Generated by Django 5.0.3 on 2024-04-09 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=70, unique=True, verbose_name='Category')),
                ('CategoryPoints', models.IntegerField(verbose_name='Category Points')),
                ('CategoryImage', models.ImageField(upload_to='img/', verbose_name='Category Image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'Categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=70, verbose_name='Item')),
                ('ItemImage', models.ImageField(upload_to='img/', verbose_name='Item Image')),
                ('ItemDescription', models.TextField(max_length=999, verbose_name='Item Description')),
                ('Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecoApp.category')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'db_table': 'Items',
                'ordering': ['id'],
            },
        ),
    ]