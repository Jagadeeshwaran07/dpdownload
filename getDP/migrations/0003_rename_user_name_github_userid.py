# Generated by Django 3.2.20 on 2023-09-16 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getDP', '0002_rename_githubuser_github_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='github',
            old_name='user_name',
            new_name='userid',
        ),
    ]
