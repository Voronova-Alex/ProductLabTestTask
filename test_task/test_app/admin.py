from django.contrib import admin
from .models import Article, Product

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_base', 'remark', 'time')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'brand', 'title')
# Register your models here.
