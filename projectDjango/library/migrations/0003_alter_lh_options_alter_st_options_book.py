# Generated by Django 4.0 on 2021-12-09 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_lh_full_name_alter_lh_short_name_st'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lh',
            options={'ordering': ['-short_Name'], 'verbose_name': 'Зал', 'verbose_name_plural': 'Список залов'},
        ),
        migrations.AlterModelOptions(
            name='st',
            options={'ordering': ['index'], 'verbose_name': 'Стеллаж', 'verbose_name_plural': 'Стеллажи'},
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
                ('listAuthor', models.TextField(max_length=50, verbose_name='Список авторов')),
                ('tom', models.FloatField(blank=True, null=True, verbose_name='Том')),
                ('part', models.FloatField(blank=True, null=True, verbose_name='Часть')),
                ('isbn', models.FloatField(verbose_name='Индекс ISBN')),
                ('year', models.FloatField(db_index=True, verbose_name='Год издания')),
                ('shelfSt', models.FloatField(verbose_name='Номер полки')),
                ('count', models.FloatField(verbose_name='Колличество')),
                ('index', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='library.st', verbose_name='Стеллаж')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['name'],
            },
        ),
    ]
