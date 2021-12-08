# Generated by Django 3.1.7 on 2021-11-24 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211124_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contact',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='experience',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
