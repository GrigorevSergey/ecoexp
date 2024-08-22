from django.db import models
from django.utils import timezone


class PostValue(models.Model):

    CATEGORY_CHOICES = (
        ('Химические_показатели', 'Химические_показатели'),
        ('Определение_удельной_активности', 'Определение_удельной_активности'),
        ('Токсикологические_исследования', 'Токсикологические_исследования'),
        ('Гидробиологические_исследования', 'Гидробиологические_исследования'),
    )
    CATEGORY_CHOICES_Indicator = (
        ('Морская вода', 'Морская вода'),
        ('Донные отложения', 'Донные отложения'),
        ('Грунты', 'Грунты'),
        ('Почва', 'Почва'),
    )

    title = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name='Категория')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES_Indicator, verbose_name='Тип показателя')
    value = models.IntegerField(default=0, verbose_name='Значение')
    name_of_indicators = models.TextField(verbose_name='Наименование показателя')

    def __str__(self):
        return f'{self.category.name}: {self.value}, {self.name_of_indicators}'


class Post(models.Model):
    customer = models.CharField(max_length=255, null=False, blank=False, verbose_name='Заказчик')
    customer_address = models.CharField(max_length=255, null=False, blank=False,
                                        verbose_name='Адрес местонахождения Заказчика')
    name_official = models.CharField(max_length=255, null=False, blank=False, verbose_name='Должность',
                                     default='Директор Жигульский В.А')
    contract = models.CharField(max_length=255, verbose_name='Договор', null=False, blank=False)
    name_of_the_object = models.TextField(null=False, blank=False, verbose_name='Наименование объекта')
    location_object = models.TextField(null=False, blank=False, verbose_name='Место расположения объекта')
    the_presence_of_harmful_factors = models.BooleanField(default=False,
                                                          verbose_name='Наличие вредных производственных факторов')
    the_purpose_of_the_research = models.CharField(max_length=255, null=False, blank=False,
                                                   verbose_name='Цель проведения исследований')
    indicators = models.ManyToManyField(PostValue, verbose_name='Показатели')

    class Meta:
        ordering = ['-contract']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name_of_the_object
