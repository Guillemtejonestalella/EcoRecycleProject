# Generated by Django 5.0.3 on 2024-04-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoApp', '0007_alter_category_categoryimage_alter_item_itemimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='CategoryBrands',
            field=models.JSONField(default=list),
        ),
    ]
