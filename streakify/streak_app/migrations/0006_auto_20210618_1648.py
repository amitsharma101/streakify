# Generated by Django 3.1.11 on 2021-06-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streak_app', '0005_auto_20210618_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streak',
            name='streak_type',
            field=models.IntegerField(choices=[(0, 'Definite'), (1, 'Indefinite')], default=0, verbose_name='Type of Streak'),
        ),
    ]