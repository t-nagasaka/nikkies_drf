# Generated by Django 3.2.5 on 2021-11-22 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20211123_0209'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Diaries',
            new_name='Diary',
        ),
        migrations.RenameModel(
            old_name='Pages',
            new_name='Page',
        ),
    ]