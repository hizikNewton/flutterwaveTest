# Generated by Django 2.0.5 on 2018-08-01 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0017_shoe_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='slug',
            new_name='nslug',
        ),
    ]