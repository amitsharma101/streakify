# Generated by Django 3.1.11 on 2021-06-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streak_app', '0003_auto_20210616_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streak',
            name='streak_type',
            field=models.CharField(choices=[('definite', 'definite'), ('indefinite', 'indefinite')], max_length=50, verbose_name='Type of Streak'),
        ),
    ]
