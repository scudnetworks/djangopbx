# Generated by Django 4.0.4 on 2023-11-08 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ivrmenus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ivrmenus',
            old_name='lanuage',
            new_name='language',
        ),
    ]
