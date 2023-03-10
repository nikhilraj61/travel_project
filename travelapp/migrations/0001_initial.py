# Generated by Django 4.1.4 on 2022-12-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='picture')),
                ('desc', models.TextField(max_length=300)),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='testmonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='picture')),
            ],
        ),
    ]
