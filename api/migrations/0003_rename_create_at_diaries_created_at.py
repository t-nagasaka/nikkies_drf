# Generated by Django 3.2.5 on 2021-10-17 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_create_at_user_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diaries',
            old_name='create_at',
            new_name='created_at',
        ),
    ]