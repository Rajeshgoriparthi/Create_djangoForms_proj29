# Generated by Django 4.1.7 on 2023-04-22 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='sid',
            new_name='id',
        ),
    ]