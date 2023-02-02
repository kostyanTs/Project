# Generated by Django 4.1.6 on 2023-02-02 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='покупатель')),
                ('place', models.CharField(max_length=40, verbose_name='адрес')),
            ],
            options={
                'verbose_name': 'покупатель',
                'verbose_name_plural': 'покупатели',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Pen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='название')),
                ('size', models.PositiveIntegerField(max_length=8, verbose_name='размер(см)')),
                ('price', models.IntegerField(max_length='10', verbose_name='цена(тг)')),
                ('count', models.PositiveIntegerField(max_length=20, verbose_name='количество')),
            ],
            options={
                'verbose_name': 'модель ручки',
                'verbose_name_plural': 'модели ручки',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(max_length=10, verbose_name='количество')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.customer', verbose_name='покупать')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.pen', verbose_name='модель ручки')),
            ],
            options={
                'verbose_name': ('заказ',),
                'verbose_name_plural': 'заказы',
                'ordering': ('customer',),
            },
        ),
    ]