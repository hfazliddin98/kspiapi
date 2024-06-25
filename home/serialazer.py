from rest_framework import serializers # type: ignore
from .models import Yangilik, Elon, GalareyaTuri, Galareya, Fikr, Statistika, Hamkorlarimiz, Talaba, ElektronKutubxona, VideoMaruzalar, VirtualQabulxona, MasofaviyTalim
from .models import Boglanish, Vakansiya
from tuzilma.models import Fakultet
from tuzilma.serialazer import FakultetSerializer


class YangilikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangilik
        fields = '__all__'
        

class ElonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elon
        fields = '__all__'
        


class GalareyaTuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalareyaTuri
        fields = '__all__'
        


class GalareyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galareya
        fields = '__all__'


class FikrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fikr
        fields = '__all__'
        


class StatistikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistika
        fields = '__all__'
        

class HamkorlarimizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamkorlarimiz
        fields = '__all__'
        

class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'
        

class ElektronKutubxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElektronKutubxona
        fields = '__all__'


class VirtualQabulxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualQabulxona
        fields = '__all__'

class MasofaviyTalimSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasofaviyTalim
        fields = '__all__'


class VideoMaruzalarSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoMaruzalar
        fields = '__all__'


class BoglanishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boglanish
        fields = '__all__'


class VakansiyaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vakansiya
        fields = '__all__'

