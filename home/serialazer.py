from rest_framework import serializers # type: ignore
from .models import Yangilik, Elon, GalareyaTuri, Galareya, Fikr, Statistika, Hamkorlarimiz, Talaba

class YangilikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangilik
        fields = '__all__'
        depth = 3

class ElonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elon
        fields = '__all__'
        depth = 3


class GalareyaTuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalareyaTuri
        fields = '__all__'
        depth = 3


class GalareyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galareya
        fields = '__all__'
        depth = 3

class FikrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fikr
        fields = '__all__'
        depth = 3


class StatistikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistika
        fields = '__all__'
        depth = 3

class HamkorlarimizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamkorlarimiz
        fields = '__all__'
        depth = 3

class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'
        depth = 3





