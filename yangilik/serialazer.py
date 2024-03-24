from rest_framework import serializers
from .models import Yangilik, Sinov, Malumot

class YangilikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangilik
        fields = '__all__'
        depth = 1
        
class SinovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinov
        fields = '__all__'
        depth = 1


class MalumotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malumot
        fields = '__all__'
        depth = 3

