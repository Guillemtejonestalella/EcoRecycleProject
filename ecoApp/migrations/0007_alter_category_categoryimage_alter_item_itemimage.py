# Generated by Django 5.0.3 on 2024-04-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoApp', '0006_alter_category_categoryimage_alter_item_itemimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CategoryImage',
            field=models.ImageField(upload_to='ecoApp/static/asstets/img', verbose_name='Category Image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='ItemImage',
            field=models.ImageField(upload_to='ecoApp/static/asstets/img', verbose_name='Item Image'),
        ),
    ]
