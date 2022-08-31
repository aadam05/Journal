from http import HTTPStatus
from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework import generics, status, viewsets

from app.serializers import ArticleSerializer
from .models import *

# Классы представлений
from rest_framework.views import APIView

# Ответы
from rest_framework.response import Response

# Декораторы дрф
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from app.permissions import IsAdminOrReadOnlyCustom, IsOwnerOrReadOnlyCustom




# Вот этот класс заменяет сразу 3 класса которые мы должны были бы прописать для CRUD
"""class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(methods=['GET'], detail=False)
    def category(self, request):
        categories = Category.objects.all()
        return Response({'categories': [ c.name for c in categories]})"""




# Вот этот класс с 2 строчками кода эквивалентен методам get() & post() класса ArticleAPI
class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )
    #permission_classes = (IsAuthenticatedOrReadOnly, )


class ArticleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnlyCustom, )
    
    # Определение метода аутентификации
    #authentication_classes = (TokenAuthentication, )


class ArticleAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnlyCustom, )



# Наглядный пример того как работает CRUD под капотом
"""class ArticleAPI(APIView):
    def get(self, request):
        fields = Article.objects.all()
        return Response({'journal': ArticleSerializer(fields, many=True).data})

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()   
        
        return Response({'journal': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})

        try:
            instanse = Article.objects.get(pk=pk)
        except:
            return Response({'error':'Objects does not exist'})

        serializer = ArticleSerializer(data=request.data, instance=instanse)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method DELETE not allowed'})

        try:
            instanse = Article.objects.get(pk=pk)
        except:
            return Response({'error':'Objects does not exist'})

        instanse.delete()
        return Response({'message':'article was deleted'}, status=status.HTTP_204_NO_CONTENT)"""
        




