# Generated by Django 4.2.2 on 2023-10-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addmin', '0007_alter_mtn_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='AIRTELL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campany', models.CharField(max_length=30, null=True)),
                ('Credit', models.CharField(max_length=200)),
                ('Debit', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=100)),
                ('R_Number', models.ImageField(upload_to='')),
                ('Phone_N', models.CharField(max_length=15)),
                ('Available_Balance', models.CharField(max_length=5000)),
                ('Time', models.DateTimeField()),
                ('Maker', models.CharField(max_length=100)),
            ],
        ),
    ]
