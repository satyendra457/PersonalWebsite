# Generated by Django 2.0.13 on 2019-08-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]