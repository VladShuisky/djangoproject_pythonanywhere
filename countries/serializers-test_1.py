from rest_framework import serializers


class CapitalSerializer(serializers.Serializer):
    capital_city = serializers.CharField(max_length=30) #нет source тк название поля совпадает с названием поля ориг модели
    capital_population = serializers.IntegerField()     #здесь аналогично
    author = serializers.CharField(source='author.username', max_length=200)


class User:
    def __init__(self, username):
        self.username = username


class Capital:
    def __init__(self, country, capital_city, capital_population, user: User):
        self.country = country
        self.capital_city = capital_city
        self.capital_population = capital_population
        self.author = user


author_obj = User('test_user')

capital_1 = Capital('Norway', 'Oslo', 23123123500, author_obj)
capital_2 = Capital('ШВеция', 'Стокгольм', 232300, author_obj)
capital_3 = Capital('Россия', 'Москва', 2323, author_obj)
capital_4 = Capital('Украина', 'Киев', 65767500, author_obj)

queryset = [capital_1, capital_2, capital_3, capital_4]
serializer_obj = CapitalSerializer(instance=queryset, many=True)
print(serializer_obj.data)




