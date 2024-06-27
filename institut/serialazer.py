from rest_framework import serializers
from .models import InstitutHaqida, InstitutMalumotlari, Kengash, Tuzilma, InstitutRekviziti, BankRekviziti, Qabulxona

class InstitutHaqidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutHaqida
        fields = '__all__'
        
class InstitutMalumotlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutMalumotlari
        fields = '__all__'

class KengashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kengash
        fields = '__all__'


class TuzilmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuzilma
        fields = '__all__'

class InstitutRekvizitiSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutRekviziti
        fields = '__all__'


class BankRekvizitiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankRekviziti
        fields = '__all__'


class QabulxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qabulxona
        fields = '__all__'

