# Generated by Django 3.0.2 on 2021-02-17 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='user_id',
            new_name='user',
        ),
    ]
