# Generated by Django 4.0 on 2022-01-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userIdentifierByLink', '0003_incorrectlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='incorrectlink',
            name='chat_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='incorrectlink',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
    ]
