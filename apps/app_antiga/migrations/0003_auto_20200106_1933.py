# Generated by Django 2.2.7 on 2020-01-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_antiga', '0002_registrousuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrousuarios',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
