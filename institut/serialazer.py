from rest_framework import serializers
from .models import InstitutHaqida, InstitutMalumotlari, Kengash, Tuzilma, InstitutRekviziti, BankRekviziti, Qabulxona
from .models import KorupsiyagaXabar, PrizdentFarmonlari, Qonunlar, VazirlarMahkamasiQarorlari, IchkiMeyoriyHujatlar


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


class KorupsiyagaXabarSerializer(serializers.ModelSerializer):
    class Meta:
        model = KorupsiyagaXabar
        fields = '__all__'


class PrizdentFarmonlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrizdentFarmonlari
        fields = '__all__'


class QonunlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qonunlar
        fields = '__all__'


class VazirlarMahkamasiQarorlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = VazirlarMahkamasiQarorlari
        fields = '__all__'


class IchkiMeyoriyHujatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = IchkiMeyoriyHujatlar
        fields = '__all__'

