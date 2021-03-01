# Generated by Django 3.0.2 on 2021-03-01 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20210217_1715'),
        ('book', '0002_bookorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookorder',
            name='issueBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='staff.Staff'),
        ),
    ]