from rest_framework import serializers
from .models import Article, Product


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('article_base', 'remark')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('article', 'brand', 'title')