# Generated by Django 3.1.7 on 2021-11-24 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_conversation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ['-created_on']},
        ),
    ]
