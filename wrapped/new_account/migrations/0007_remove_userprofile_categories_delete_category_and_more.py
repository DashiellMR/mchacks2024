# Generated by Django 5.0.1 on 2024-01-28 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_account', '0006_remove_userprofile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='categories',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
