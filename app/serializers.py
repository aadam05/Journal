from dataclasses import fields
from rest_framework import serializers
from .models import Article

from django.utils import timezone


from rest_framework.renderers import JSONRenderer



class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Article
        fields = '__all__'



# Не хороший способ, приходится писать много лишнего кода с полями БД, получше будет ModelSerializer
"""class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    text = serializers.CharField()
    date = serializers.DateTimeField(default=timezone.now, read_only=True)
    categ_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.date = validated_data.get('date', instance.date)
        instance.categ_id = validated_data.get('categ_id', instance.categ_id)
        instance.save()

        return instance"""



# class ArticleModel:
#     def __init__(self, title, text):
#         self.title = title
#         self.text = text

# default=timezone.now
    