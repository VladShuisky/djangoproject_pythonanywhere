from rest_framework import serializers


class CapitalSerializer(serializers.Serializer):
    capital_city = serializers.CharField(max_length=30) #нет source тк название поля совпадает с названием поля ориг модели
    capital_population = serializers.IntegerField()     #здесь аналогично
    author = serializers.CharField(source='author.username', max_length=200)
