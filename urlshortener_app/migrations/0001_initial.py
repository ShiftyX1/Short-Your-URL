# Generated by Django 4.2.11 on 2024-03-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreeShortedUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_url', models.CharField(max_length=2000)),
                ('url_in_db', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
