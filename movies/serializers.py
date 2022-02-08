from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    tagline = serializers.CharField(max_length=50)
    description = serializers.CharField()
    year = serializers.IntegerField()
    country = serializers.CharField(max_length=50)
    world_premiere = serializers.DateField()
    budget = serializers.IntegerField()
    fees_in_usa = serializers.IntegerField()
    fess_in_world = serializers.IntegerField()
    category = serializers.CharField(source='category.name', max_length=100)