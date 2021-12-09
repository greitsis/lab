# Generated by Django 4.0 on 2021-12-08 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lh',
            name='full_Name',
            field=models.CharField(max_length=50, verbose_name='Полное название зала'),
        ),
        migrations.AlterField(
            model_name='lh',
            name='short_Name',
            field=models.CharField(max_length=50, verbose_name='Название зала'),
        ),
        migrations.CreateModel(
            name='St',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(db_index=True, max_length=20, verbose_name='Индекс')),
                ('short_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='library.lh', verbose_name='Зал')),
            ],
        ),
    ]
