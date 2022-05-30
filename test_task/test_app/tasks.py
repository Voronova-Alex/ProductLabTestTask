import requests
from .models import Product


def create_product(list):
    for article in list:
        try:
            url_name = f"https://wbx-content-v2.wbstatic.net/ru/{article}.json"
            url_brand = f"https://wbx-content-v2.wbstatic.net/sellers/{article}.json"
            response_name = f'{requests.get(url_name).json()["imt_name"]}/{requests.get(url_name).json()["selling"]["brand_name"]}'
            response_brand = requests.get(url_brand).json()["trademark"]
            if Product.objects.filter(article=article).exists():
                product = Product.objects.get(article=article)
                product.title = response_name
                product.brand = response_brand
                product.save()
            else:
                product = Product(article=article, title=response_name, brand=response_brand)
                product.save()

        except ValueError:
            if Product.objects.filter(brand=f'Error {article}').exists() == False:
                product = Product(article=0, title='Product not found', brand=f'Error {article}')
                product.save()
