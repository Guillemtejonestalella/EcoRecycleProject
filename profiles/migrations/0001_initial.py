# Generated by Django 5.0.3 on 2024-05-03 11:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProfileName', models.CharField(blank=True, max_length=50)),
                ('ProfilePoints', models.IntegerField(default=0)),
                ('ProfileAdress', models.CharField(blank=True, max_length=70)),
                ('ProfilePerson', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
