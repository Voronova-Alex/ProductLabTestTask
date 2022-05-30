from django.db import models


class Article(models.Model):
    article_base = models.FileField(blank=False, null=False, verbose_name='Article base')
    remark = models.CharField(max_length=20, verbose_name='Remark')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Product(models.Model):
    article = models.PositiveIntegerField(verbose_name='Article')
    brand = models.CharField(max_length=50, verbose_name='Brand')
    title = models.CharField(max_length=255, verbose_name='Title')

    def __str__(self):
        return f'{self.article}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

