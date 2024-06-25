from rest_framework import serializers 
from .models import Jamoatchilik, Madaniy, Oquv, Akademik, Ilmiy, Yoshlar


class JamoatchilikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jamoatchilik
        fields = '__all__'
        

class MadaniySerializer(serializers.ModelSerializer):
    class Meta:
        model = Madaniy
        fields = '__all__'        


class OquvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oquv
        fields = '__all__'        


class AkademikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Akademik
        fields = '__all__'


class IlmiySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ilmiy
        fields = '__all__'
        


class YoshlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yoshlar
        fields = '__all__'
        

