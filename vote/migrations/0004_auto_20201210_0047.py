# Generated by Django 3.1.3 on 2020-12-09 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0003_auto_20201209_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='voter',
        ),
        migrations.AddField(
            model_name='votes',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='voter',
            name='birthday',
            field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='voter',
            name='secure_pin',
            field=models.CharField(max_length=7),
        ),
    ]
