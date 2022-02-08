from django.db import models
from django.conf import settings
from django.utils import timezone


class Country(models.Model):
    country = models.CharField(max_length=30)
    capital_city = models.CharField(max_length=30)
    capital_population = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"



