# Generated by Django 5.0.3 on 2024-04-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CategoryImage',
            field=models.ImageField(upload_to='ecoApp/static/assets/img/', verbose_name='Category Image'),
        ),
    ]
