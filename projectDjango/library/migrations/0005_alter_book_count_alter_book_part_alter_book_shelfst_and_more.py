# Generated by Django 4.0 on 2021-12-09 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='count',
            field=models.IntegerField(verbose_name='Колличество'),
        ),
        migrations.AlterField(
            model_name='book',
            name='part',
            field=models.IntegerField(blank=True, null=True, verbose_name='Часть'),
        ),
        migrations.AlterField(
            model_name='book',
            name='shelfSt',
            field=models.IntegerField(verbose_name='Номер полки'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tom',
            field=models.IntegerField(blank=True, null=True, verbose_name='Том'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(db_index=True, verbose_name='Год издания'),
        ),
    ]
