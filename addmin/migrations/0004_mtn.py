# Generated by Django 4.2.2 on 2023-10-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addmin', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Credit', models.CharField(max_length=200)),
                ('Debit', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=100)),
                ('R_Number', models.ImageField(upload_to='')),
                ('Phone_N', models.CharField(max_length=15)),
                ('Available_Balance', models.CharField(max_length=5000)),
                ('Time', models.TimeField()),
            ],
        ),
    ]
