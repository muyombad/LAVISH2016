# Generated by Django 4.2.2 on 2023-10-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addmin', '0005_mtn_maker'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtn',
            name='campany',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
