# Generated by Django 3.0.1 on 2020-01-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20200116_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='feedback',
            field=models.CharField(default='Not Submitted', max_length=100),
        ),
        migrations.AlterField(
            model_name='date',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
