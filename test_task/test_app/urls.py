from django.urls import path
from .views import APIArticleView, APIProduct

urlpatterns = [
    path('', APIArticleView.as_view(), name='upload'),
    path('info', APIProduct.as_view(), name='info')

]
