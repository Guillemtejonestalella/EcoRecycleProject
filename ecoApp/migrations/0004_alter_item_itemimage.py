# Generated by Django 5.0.3 on 2024-04-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoApp', '0003_alter_category_categoryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ItemImage',
            field=models.ImageField(upload_to='assets/img/', verbose_name='Item Image'),
        ),
    ]