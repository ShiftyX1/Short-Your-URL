from django.db import models
from django.utils import timezone
import time

class FreeShortedUrls(models.Model):
    destination_url = models.CharField(max_length=2000)
    url_in_db = models.CharField(max_length=10, unique=True)
    added = models.DateTimeField(default=timezone.now)
    ttl = models.IntegerField()
    dead_link_time = models.IntegerField()


    class Meta:
        ordering = ['-added']
        verbose_name = "Бесплатно укороченная ссылка"
        verbose_name_plural = "Бесплатно укороченные ссылки"

    def __str__(self) -> str:
        return self.destination_url
    

class FreeGeneratedQR(models.Model):
    destination_url = models.CharField(max_length=2000)
    url_in_db = models.CharField(max_length=10, unique=True)
    added = models.DateTimeField(default=timezone.now)
    ttl = models.IntegerField()
    dead_link_time = models.IntegerField()
    qr_code = models.ImageField(verbose_name="Картинка QR-кода")

    class Meta:
        ordering = ['-added']
        verbose_name = "QR-код FREE"
        verbose_name_plural = "QR-коды FREE"

    def __str__(self) -> str:
        return self.destination_url

