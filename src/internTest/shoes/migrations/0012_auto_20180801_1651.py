# Generated by Django 2.0.5 on 2018-08-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0011_auto_20180801_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
