# Generated by Django 4.2.11 on 2024-03-14 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener_app', '0003_alter_freeshortedurls_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeGeneratedQR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_url', models.CharField(max_length=2000)),
                ('url_in_db', models.CharField(max_length=10, unique=True)),
                ('added', models.DateTimeField(default=django.utils.timezone.now)),
                ('ttl', models.IntegerField()),
                ('dead_link_time', models.IntegerField()),
                ('qr_code', models.ImageField(upload_to='', verbose_name='Картинка QR-кода')),
            ],
            options={
                'verbose_name': 'QR-код FREE',
                'verbose_name_plural': 'QR-коды FREE',
                'ordering': ['-added'],
            },
        ),
        migrations.AlterModelOptions(
            name='freeshortedurls',
            options={'ordering': ['-added'], 'verbose_name': 'Бесплатно укороченная ссылка', 'verbose_name_plural': 'Бесплатно укороченные ссылки'},
        ),
    ]
