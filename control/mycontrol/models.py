from django.db import models
from django.utils import timezone



class Budget(models.Model):
    title = models.CharField('Название транзакции', max_length=100, unique=True)
    value = models.FloatField('Бюджет', blank=True, default=0.0)
    consumption = models.FloatField('Расход', blank=True, default=0.0)
    pub_date = models.DateTimeField('Дата транзакции', default=timezone.now)
    
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Бюджет'
        verbose_name_plural = 'Бюджеты'