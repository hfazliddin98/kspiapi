from rest_framework import serializers
from .models import Yangilik, Elon, GalareyaTuri, Galareya

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


