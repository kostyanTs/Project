from django.db import models
from typing import Any

class Pen(models.Model):
    title = models.CharField(
        unique=True,
        max_length=40,
        verbose_name='название'
    )
    size = models.PositiveIntegerField(
     
        verbose_name='размер(см)'
    )
    price = models.IntegerField(
        verbose_name='цена(тг)',
      
    )
    count = models.PositiveIntegerField(
        verbose_name='количество',
    
    )

    class Meta:
        ordering = (
            'title',
        )
        verbose_name = 'модель ручки'
        verbose_name_plural = 'модели ручки'

    def save(
        self, 
        *args: Any, 
        **kwargs: Any
    ) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Customer(models.Model):
    title = models.CharField(
        max_length=40,
        verbose_name='покупатель'
    )
    place = models.CharField(
        max_length=40,
        verbose_name='адрес'
    )
    class Meta:
        ordering = (
            'title',
        )
        verbose_name = 'покупатель'
        verbose_name_plural = 'покупатели'

    def __str__(self) -> str:
        return self.title 

class Order(models.Model):
    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.PROTECT,
        verbose_name='покупать'

    )
    product = models.ForeignKey(
        to=Pen,
        on_delete=models.PROTECT,
        verbose_name='модель ручки'
    )
    count = models.PositiveIntegerField(
        verbose_name='количество',
    )

    class Meta:
        ordering = (
            'customer',
        )
        verbose_name = 'заказ',
        verbose_name_plural = 'заказы'
    

