# Generated by Django 4.2 on 2023-07-28 23:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Whisper', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profile',
            new_name='proffile',
        ),
    ]
