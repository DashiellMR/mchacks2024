# Generated by Django 5.0.1 on 2024-01-28 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_account', '0005_category_remove_userprofile_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
    ]