# Generated by Django 3.1.2 on 2020-10-30 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessClubApp', '0007_auto_20201030_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]