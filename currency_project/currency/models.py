from django.db import models


class Currency(models.Model):
    char_code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField()

    class Meta:
        unique_together = ('currency', 'date')
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'

    def __str__(self):
        return f"{self.currency} - {self.date} - {self.value}"
