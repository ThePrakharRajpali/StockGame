# Generated by Django 3.0.1 on 2020-01-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='cat',
            field=models.CharField(default='tec', max_length=25),
        ),
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.CharField(default='max cap', max_length=25),
        ),
    ]
