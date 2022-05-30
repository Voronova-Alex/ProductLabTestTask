from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializer, ProductSerializer
from .models import Product
from rest_framework import generics
import pandas
from .tasks import create_product


class APIArticleView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = ArticleSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            info = pandas.read_excel(file_serializer.data['article_base'][1:], usecols=[0], header=None)
            create_product.delay(info[0].tolist())
            return Response({**file_serializer.data, **{'получить двнные': 'http://127.0.0.1:8000/info'}}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
