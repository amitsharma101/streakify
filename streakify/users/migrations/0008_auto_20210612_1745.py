# Generated by Django 3.1.11 on 2021-06-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210612_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Profile Image'),
        ),
    ]
