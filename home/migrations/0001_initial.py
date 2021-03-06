# Generated by Django 4.0.1 on 2022-06-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contt',
            fields=[
                ('contid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=80)),
                ('phone_no', models.IntegerField()),
                ('doubts', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='pt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('imag', models.ImageField(default='', upload_to='ForHome')),
                ('description', models.CharField(default='this is the detail information about the product you choosed', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='signop',
            fields=[
                ('signid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=40)),
                ('email', models.EmailField(max_length=80)),
                ('pwOne', models.CharField(max_length=100)),
                ('pwTwo', models.CharField(max_length=100)),
            ],
        ),
    ]
