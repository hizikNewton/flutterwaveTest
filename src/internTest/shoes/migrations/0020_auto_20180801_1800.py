# Generated by Django 2.0.5 on 2018-08-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0019_auto_20180801_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]