from django.db import models


class Sex(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"


class Community(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сообщество"
        verbose_name_plural = "Сообщества"


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.ForeignKey(Sex, default=None,  on_delete=models.CASCADE)
    age = models.SmallIntegerField(default=None)
    communities = models.ManyToManyField(Community, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"