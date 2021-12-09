from django.db import models

# Create your models here.

class Lh(models.Model):
    short_Name = models.CharField(max_length=50, verbose_name='Название зала')
    full_Name = models.CharField(max_length=50, verbose_name='Полное название зала')
    
    def __str__(self):
        return self.short_Name

    class Meta:
        verbose_name_plural = 'Список залов'
        verbose_name = 'Зал'
        ordering = ['-short_Name']

class St(models.Model):
    index = models.CharField(max_length=20, db_index=True,verbose_name='Индекс')
    short_Name = models.ForeignKey('Lh', null=True, on_delete=models.PROTECT, verbose_name='Зал')
    
    def __str__(self):
        return self.index

    class Meta:
        verbose_name_plural = 'Стеллажи'
        verbose_name = 'Стеллаж'
        ordering = ['index']

class Book(models.Model):
    name = models.CharField(max_length=20, db_index=True,verbose_name='Название')
    listAuthor = models.TextField(max_length=50, verbose_name='Список авторов')
    tom = models.IntegerField(null=True, blank=True, verbose_name='Том')
    part = models.IntegerField(null=True, blank=True, verbose_name='Часть')
    isbn = models.CharField(max_length=30, verbose_name='Индекс ISBN')
    year = models.IntegerField(db_index = True, verbose_name='Год издания')
    index = models.ForeignKey('St', null=True, on_delete=models.PROTECT, verbose_name='Стеллаж')
    shelfSt = models.IntegerField(verbose_name='Номер полки')
    count = models.IntegerField(verbose_name='Колличество')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        ordering = ['name']

