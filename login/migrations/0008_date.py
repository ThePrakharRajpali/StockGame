# Generated by Django 3.0.1 on 2019-12-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20191227_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=3)),
                ('year', models.IntegerField(default=2019)),
                ('num', models.IntegerField(default=0)),
                ('day', models.IntegerField(default=0)),
                ('hour', models.IntegerField(default=0)),
                ('minute', models.IntegerField(default=0)),
            ],
        ),
    ]