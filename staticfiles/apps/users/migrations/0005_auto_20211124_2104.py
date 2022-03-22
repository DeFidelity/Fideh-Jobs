# Generated by Django 3.1.7 on 2021-11-24 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211124_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='available',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='field',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='qualification',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
    ]