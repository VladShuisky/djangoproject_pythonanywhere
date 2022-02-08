from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import random
import datetime
from transliterate import translit
from .other_functions import random_slug


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    slug = models.SlugField(max_length=30, unique=True, blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def save(self, *args, **kwargs):
        if not self.slug:
            en_text = translit(self.question_text, language_code='ru', reversed=True)
            self.slug = slugify(f'{random_slug()}-{en_text}')
        super(Question, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "Вариант выбора"
        verbose_name_plural = "Варианты выбора"





# Create your models here.
