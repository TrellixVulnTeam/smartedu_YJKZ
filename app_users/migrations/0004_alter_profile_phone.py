# Generated by Django 3.2 on 2022-06-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_remove_profile_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
