# Generated by Django 2.1.1 on 2018-10-06 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upvote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Altcoin',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='post',
            name='Main_Pair',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_feed',
            field=models.CharField(max_length=20),
        ),
    ]
