# Generated by Django 3.1.2 on 2020-10-28 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitnessClubApp', '0005_remove_fitdata_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitdata',
            name='Email',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
