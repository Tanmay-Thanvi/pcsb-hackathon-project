# Generated by Django 3.2.8 on 2021-11-19 20:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_extendeduser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='sigs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None),
        ),
    ]
